# AI Job Search Dashboard

An AI-powered job search tool that aggregates live postings across 130+ target companies, scores each role for fit and realistic offer likelihood using Claude, and surfaces results in a filterable web dashboard — built for MBA candidates targeting Strategy & Operations roles in tech.

---

## The Problem

Job searching at the MBA level is noisy. LinkedIn surfaces hundreds of irrelevant postings. Company career pages require checking 50+ sites individually. And most job boards don't tell you what actually matters: *is this role worth your time to apply to?*

This tool solves that by pulling from multiple sources simultaneously, filtering aggressively, and using Claude to score each role on two honest dimensions — how well it fits your background, and how realistic an offer actually is.

---

## What It Does

**Aggregates from multiple sources:**
- **LinkedIn, Indeed, and Glassdoor** via JSearch API — broad market coverage across NYC, SF, and London
- **Greenhouse, Lever, and Ashby** — queried directly from 130+ hand-curated target companies, including AI labs, fintech, SaaS, health tech, marketplaces, and VC firms

**Filters intelligently:**
- Excludes engineering, design, legal, and admin roles by title
- Excludes overly senior titles (VP, Managing Director, Head of, SVP) not appropriate for early-career MBA hires
- Deduplicates across sources so the same role doesn't appear twice

**Scores every role with Claude:**
- **Fit score (0–100)** — how well the role and company match the candidate's background, industry, and stated goals
- **Conversion score (0–100)** — realistic offer likelihood, calibrated by company type:
  - Big Tech: 25–45 (mass applicant pools, structured recruiting)
  - Mid Tech: 40–60
  - High-growth startups: 50–75 (MBA backgrounds valued, smaller teams)
  - VC firms: 45–65 (highly selective, but MBA-preferred for CoS and ops)
  - Enterprise: 20–40 (slow-moving, poor MBA-startup fit)
- **Apply recommendation** — flagged only when fit ≥ 65 and conversion ≥ 50

**Renders a live web dashboard:**
- Color-coded scores (green / orange / red)
- Filter by city (NYC, SF, London), company type, or apply status
- Direct application links — no job board middleman
- Stats bar showing total roles, apply-now count, startup count, and average fit score

---

## Target Companies

130+ companies across:

| Category | Examples |
|---|---|
| AI / ML | Anthropic, OpenAI, Scale AI, Cohere, Perplexity, Glean, ElevenLabs, Harvey, Cognition |
| Fintech | Ramp, Brex, Plaid, Chime, Carta, Mercury, Deel, Gusto, Klarna, Affirm |
| SaaS / Productivity | Rippling, Notion, Figma, Airtable, Miro, Retool, Lattice, Intercom, Discord |
| Data / Infra | Databricks, Confluent, dbt Labs, Fivetran, HashiCorp, Cockroach Labs |
| Security | Snyk, Wiz, Vanta, Drata, Abnormal Security, CrowdStrike |
| Health Tech | Hinge Health, Lyra Health, Spring Health, Modern Health, Ro, Hims & Hers |
| VC Firms | a16z, Sequoia, Accel, Index Ventures, Atomico, Balderton, Lightspeed, General Catalyst |
| London / Europe | Monzo, Revolut, Wise, Checkout.com, Wayve, Synthesia, Starling Bank, Deliveroo |

---

## How to Run

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Set API keys**

```bash
export ANTHROPIC_API_KEY="your-key"   # console.anthropic.com
export RAPIDAPI_KEY="your-key"        # rapidapi.com → subscribe to JSearch
```

**3. Run**

```bash
python3 dashboard.py
```

Opens `dashboard.html` in your browser automatically. Full run takes 3–5 minutes depending on how many roles are found.

---

## Architecture

```
JSearch API (LinkedIn / Indeed / Glassdoor)  ──┐
                                                ├──▶ Deduplicate & filter
Greenhouse API (100+ companies)               ──┤
Lever API                                     ──┤        │
Ashby API                                     ──┘        ▼
                                               Claude (fit + conversion scoring)
                                                          │
                                                          ▼
                                                   dashboard.html
```

Each source is queried independently. Greenhouse, Lever, and Ashby are free public APIs — no authentication required. JSearch requires a RapidAPI key (free tier available).

---

## Project Structure

```
ai-workflow-demo/
├── dashboard.py      # Orchestrates fetch → score → render pipeline
├── jobs.py           # All fetching logic (JSearch + ATS) and Claude scoring
├── dashboard.html    # Generated output — open in any browser, no server needed
├── requirements.txt  # anthropic, requests
└── Procfile          # Deployment config
```

---

## Tech Stack

- **Claude API** (Anthropic) — `claude-haiku-4-5` for fast, cost-efficient structured JSON scoring
- **JSearch via RapidAPI** — aggregates LinkedIn, Indeed, Glassdoor into one API
- **Greenhouse / Lever / Ashby** — free public ATS APIs with no rate limits
- **Python standard library** — no Flask, no FastAPI, no web framework
- **Static HTML output** — no server required to view the dashboard
