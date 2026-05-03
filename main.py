"""
AI Support Ticket Processor
----------------------------
Takes a raw customer support message and returns:
  - A short summary
  - A category (billing, bug, feature request, other)
  - A suggested next action

Uses the Anthropic API (Claude). Store your key in ANTHROPIC_API_KEY.
"""

import os
import json
import anthropic


def process_ticket(message: str) -> dict:
    """
    Send a support message to Claude and get back structured output.
    Returns a dict with: summary, category, next_action
    """
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    # The prompt tells Claude exactly what format to return
    prompt = f"""You are a customer support triage assistant.

Analyze the following support message and respond with ONLY a JSON object
(no markdown, no explanation) in this exact format:
{{
  "summary": "<one-sentence summary of the issue>",
  "category": "<one of: billing, bug, feature_request, other>",
  "next_action": "<one concrete suggested next step for the support team>"
}}

Support message:
\"\"\"{message}\"\"\"
"""

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract the text from the response
    raw_text = response.content[0].text.strip()

    # Parse the JSON Claude returned
    result = json.loads(raw_text)
    return result


def main():
    # --- Sample tickets to demonstrate the workflow ---
    sample_tickets = [
        "Hi, I was charged twice for my subscription this month. "
        "I see two charges of $29.99 on my credit card statement from the 3rd. Please help!",

        "The export to PDF button on the dashboard does nothing when I click it. "
        "I'm using Chrome 124 on Windows 11. This used to work last week.",

        "It would be really useful if you could add dark mode to the app. "
        "My eyes get tired at night and a lot of apps support this now.",
    ]

    print("=" * 60)
    print("AI SUPPORT TICKET PROCESSOR")
    print("=" * 60)

    for i, ticket in enumerate(sample_tickets, start=1):
        print(f"\n--- Ticket #{i} ---")
        print(f"Message: {ticket}\n")

        result = process_ticket(ticket)

        print(f"Summary     : {result['summary']}")
        print(f"Category    : {result['category']}")
        print(f"Next Action : {result['next_action']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
