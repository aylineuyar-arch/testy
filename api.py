"""
AI Support Ticket Processor — REST API
----------------------------------------
Exposes a single endpoint:

  POST /triage
  Body: {"message": "your support message here"}
  Returns: {"summary": "...", "category": "...", "next_action": "..."}

Run with:
  python3 api.py

Then test with:
  curl -X POST http://localhost:8000/triage \
    -H "Content-Type: application/json" \
    -d '{"message": "I was charged twice this month"}'
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from main import process_ticket  # reuse the logic we already built


class TriageHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Only handle /triage
        if self.path != "/triage":
            self._send(404, {"error": "Not found"})
            return

        # Read and parse the request body
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._send(400, {"error": "Invalid JSON"})
            return

        message = data.get("message", "").strip()
        if not message:
            self._send(400, {"error": "Missing 'message' field"})
            return

        # Call Claude
        try:
            result = process_ticket(message)
            self._send(200, result)
        except Exception as e:
            self._send(500, {"error": str(e)})

    def do_GET(self):
        # Health check endpoint
        if self.path == "/health":
            self._send(200, {"status": "ok"})
        else:
            self._send(404, {"error": "Not found"})

    def _send(self, status: int, data: dict):
        body = json.dumps(data, indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # Silence the default request logging (optional — remove to see logs)
    def log_message(self, format, *args):
        print(f"  {self.address_string()} → {args[0]}")


def run():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("", port), TriageHandler)
    print(f"Server running on http://localhost:{port}")
    print(f"POST /triage  — process a support ticket")
    print(f"GET  /health  — health check")
    print(f"\nPress Ctrl+C to stop\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    run()
