# 🚨 Scam Job Detector

> AI-powered tool that analyzes job postings for fraud indicators using Google Gemini, rule-based detection, and domain analysis.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini-1.5_Flash-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## The Problem

Every year, thousands of Indian students and early-career developers lose money and time to fake job postings. These scams use:

- Upfront registration or training fees
- Unrealistic salary promises (₹50,000/month for freshers)
- Generic Gmail/Yahoo recruiter emails
- No-interview, instant-joining tactics
- Vague job roles with no verifiable company

No simple, free tool existed to quickly verify a job posting — until this.

---

## What It Does

Paste a job URL or description → the system analyzes it across four layers → returns a structured risk report.

```
Input (URL or Text)
        ↓
Content Extraction       — BeautifulSoup scrapes job page
        ↓
Feature Extraction       — emails, phone, salary, fee mentions
        ↓
Rule-Based Detection     — 10+ fraud pattern checks
        ↓
Domain Age Analysis      — WHOIS trust signal
        ↓
Gemini LLM Reasoning     — contextual scam analysis
        ↓
Structured Risk Report   — score, verdict, flags, recommendation
```

---

## Demo

| Input | Score | Verdict |
|-------|-------|---------|
| "Pay ₹500 fee, ₹60k/month, no experience, gmail recruiter" | 98/100 | 🔴 HIGH RISK |
| Microsoft Software Engineer Intern (official site) | 4/100 | 🟢 LOW RISK |

---

## Features

**AI Analysis**
- Google Gemini 1.5 Flash for contextual reasoning
- Outputs scam score, verdict, red flags, green flags, reasoning, recommendation

**Rule-Based Detection**
- Registration / processing fee mentions
- Generic free email providers (Gmail, Yahoo)
- Unrealistic salary claims
- No-experience + high-pay combinations
- Work-from-home scam patterns
- Urgency pressure language

**Feature Extraction**
- Email addresses and phone numbers
- Salary mentions and risk classification
- Fee indicator detection

**Domain Analysis**
- Domain age via WHOIS
- Domains under 30 days flagged as suspicious

**Dual Input Modes**
- URL mode: scrapes and analyzes any job posting page
- Text mode: paste job description directly (fallback for blocked sites)

**Graceful Error Handling**
- API quota fallback
- Scraping failure fallback
- Malformed JSON recovery

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React.js, Axios |
| Backend | FastAPI, Python |
| AI | Google Gemini 1.5 Flash |
| Scraping | BeautifulSoup4, Requests |
| Domain Check | python-whois |
| Config | python-dotenv |

---

## Project Structure

```
scam-job-detector/
├── backend/
│   ├── main.py          # FastAPI server, /analyze endpoint
│   ├── analyzer.py      # Gemini API integration
│   ├── scraper.py       # URL fetching, domain age check
│   ├── extractor.py     # Feature extraction
│   ├── rules.py         # Rule-based fraud detection
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── App.js            # Main app, state, API calls
│       └── components/
│           └── ResultCard.jsx
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- Google Gemini API key → [aistudio.google.com](https://aistudio.google.com)

### Backend Setup

```bash
git clone https://github.com/ajaykrixna/scam-job-detector.git
cd scam-job-detector/backend

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

Create `.env` file:
```env
GEMINI_API_KEY=your_api_key_here
```

Run backend:
```bash
uvicorn main:app --reload
# → http://localhost:8000
# → http://localhost:8000/docs  (Swagger UI)
```

### Frontend Setup

```bash
cd ../frontend
npm install
npm start
# → http://localhost:3000
```

---

## API Reference

### `POST /analyze`

**Request body:**
```json
{
  "url": "https://company.com/jobs/ml-engineer",
  "text": ""
}
```
Or with pasted text:
```json
{
  "url": "",
  "text": "Hiring ML Engineer. Pay ₹500 registration fee..."
}
```

**Response:**
```json
{
  "scam_score": 98,
  "verdict": "HIGH RISK",
  "red_flags": [
    "Requires upfront registration fee",
    "Gmail recruiter email",
    "Unrealistic salary for freshers"
  ],
  "green_flags": [],
  "recommendation": "Do not apply. Do not pay any fees.",
  "reasoning": "This posting exhibits multiple classic advance-fee scam patterns...",
  "domain_age": 12
}
```

---

## Limitations

- URL scraping may fail on sites that block bots (LinkedIn, Naukri) — use text mode as fallback
- Analysis depends on Gemini API availability and free-tier quota
- Domain age alone is not a definitive signal — new legitimate startups also have new domains
- This tool provides automated risk assessment only. Always independently verify before sharing personal information or making payments.

---

## Future Improvements

- [ ] Company name verification against MCA India / official registries
- [ ] Historical scam database for pattern matching
- [ ] Browser extension for one-click job page analysis
- [ ] Deployment on Vercel (frontend) + Render (backend)
- [ ] User reporting system to crowdsource known scam postings
- [ ] Confidence interval display alongside risk score

---

## Author

**Ajaykrishna** — B.Tech AI & Data Science, Jyothi Engineering College  
GitHub: [@ajaykrixna](https://github.com/ajaykrixna)

---

## Disclaimer

This tool provides automated risk assessment and should not be treated as a definitive judgment. Users should independently verify job opportunities before sharing personal information or making any payments.
