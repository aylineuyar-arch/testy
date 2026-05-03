# AI Support Ticket Processor

An AI-powered workflow that reads raw customer support messages and automatically triages them — no manual review needed for the first pass.

---

## What It Does

Given a raw support message like:

> "I was charged twice for my subscription this month."

It returns:

```
Summary     : Customer reports a duplicate charge of $29.99 on their account.
Category    : billing
Next Action : Pull the customer's billing history and issue a refund for the duplicate charge.
```

---

## Why It's Useful

Support teams spend a lot of time reading and routing tickets before any real work begins. This prototype automates that first step — classification and triage — so agents can focus on resolution rather than sorting.

---

## How It Works

1. A support message is passed to Claude (Anthropic's AI model) via the API
2. A structured prompt asks Claude to return JSON with three fields: `summary`, `category`, and `next_action`
3. The JSON is parsed and printed — ready to be piped into a ticketing system, database, or Slack alert

```
User message → Prompt → Claude API → JSON response → Parsed output
```

---

## How to Run

**1. Clone or copy the project**

```bash
git clone <your-repo-url>
cd ai-workflow-demo
```

**2. Set your API key**

Get a key at [console.anthropic.com](https://console.anthropic.com). Then set it as an environment variable — never hardcode keys in source files.

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run it**

```bash
python main.py
```

---

## What I Would Build Next

- **REST API wrapper** — expose this as a `/triage` endpoint so any frontend or integration can call it
- **Confidence scoring** — ask Claude to rate how confident it is in the category, and flag low-confidence tickets for human review
- **Priority detection** — add an `urgency` field (low / medium / high) based on keywords and tone
- **CRM integration** — write triaged tickets directly to Zendesk, Linear, or a Postgres table
- **Batch processing** — use the Anthropic Batches API to process thousands of historical tickets at 50% cost for training data or analytics
- **Evaluation harness** — run 50 labeled tickets through the model and track category accuracy over time as the prompt evolves

---

## Project Structure

```
ai-workflow-demo/
├── main.py           # Core logic — prompt, API call, output
├── requirements.txt  # One dependency: anthropic
└── README.md         # This file
```
