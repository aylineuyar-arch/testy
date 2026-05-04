# AI Workflow Demo

Two AI-powered tools built with the Anthropic Claude API.

---

## Project 1 — Job Search Dashboard

Pulls live job postings from 80+ target companies and scores each one for fit and conversion likelihood using Claude.

### What It Does

- Searches **LinkedIn, Indeed, and Glassdoor** via JSearch API across NYC, SF, and London
- Queries **Greenhouse, Lever, and Ashby** job boards directly from 80+ high-growth companies (Anthropic, OpenAI, Ramp, Rippling, Databricks, Monzo, and more)
- Filters out irrelevant roles (engineering, admin, overly senior titles)
- Scores each job with Claude on two dimensions:
  - **Fit score** — how well the role matches the candidate's background
  - **Conversion score** — realistic offer likelihood based on company type and competition level
- Renders a **live web dashboard** with filter buttons, color-coded scores, and direct application links

### How to Run

```bash
export ANTHROPIC_API_KEY="your-key"
export RAPIDAPI_KEY="your-key"
pip install -r requirements.txt
python3 dashboard.py
```

Opens `dashboard.html` in your browser automatically.

### How It Works

```
JSearch API (LinkedIn/Indeed/Glassdoor)  ──┐
                                            ├──▶ Filter ──▶ Claude scoring ──▶ HTML dashboard
Greenhouse / Lever / Ashby (80 companies) ──┘
```

---

## Project 2 — AI Support Ticket Processor

An AI-powered REST API that reads raw customer support messages and automatically triages them.

### What It Does

Given a raw support message like:

> "I was charged twice for my subscription this month."

It returns:

```json
{
  "summary": "Customer reports a duplicate charge of $29.99 on their account.",
  "category": "billing",
  "next_action": "Pull the customer's billing history and issue a refund for the duplicate charge."
}
```

### How to Run

```bash
export ANTHROPIC_API_KEY="your-key"
python3 api.py
```

Then call it:

```bash
curl -X POST http://localhost:8080/triage \
  -H "Content-Type: application/json" \
  -d '{"message": "I was charged twice this month"}'
```

Live deployment: `https://testy-production-44ad.up.railway.app/triage`

### How It Works

```
POST /triage  →  Claude API  →  JSON (summary, category, next_action)
GET  /health  →  {"status": "ok"}
```

---

## Project Structure

```
ai-workflow-demo/
├── dashboard.py      # Fetches, scores, and renders the job dashboard
├── jobs.py           # Job fetching logic (JSearch + ATS APIs) + Claude scoring
├── dashboard.html    # Generated output — open in any browser
├── main.py           # Support ticket processor core logic
├── api.py            # REST API wrapper (http.server, no framework)
├── requirements.txt  # anthropic, requests
└── Procfile          # Railway deployment config
```

---

## Tech Stack

- **Claude API** (Anthropic) — claude-haiku-4-5 for fast, structured JSON scoring
- **JSearch via RapidAPI** — LinkedIn, Indeed, Glassdoor aggregation
- **Greenhouse / Lever / Ashby APIs** — free, no-auth job board APIs
- **Python stdlib only** — no Flask, no FastAPI, no framework
- **Deployed on Railway**
