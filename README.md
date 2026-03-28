# 🏥 MedGuard AI: Specialized Healthcare Operations Agent

MedGuard AI is a domain-specific agent designed to automate **Prior Authorization** workflows in healthcare while staying strictly within regulatory policy guardrails.

## 🚀 The Problem
Medical billing and prior authorization are manually intensive. 15% of claims are denied due to coding errors, costing hospitals billions and delaying patient care.

## 🧠 The Solution
MedGuard uses a **Multi-Agent Orchestration** (LangGraph) to:
1. **Intake Agent:** Extracts CPT/ICD-10 codes from clinical notes.
2. **Policy Auditor:** Validates codes against a JSON-based Payer Policy database (The Guardrail).
3. **Audit Trail:** Generates a step-by-step reasoning log for human review.

## 🏗️ Architecture
- **Orchestration:** LangGraph (Stateful Agentic Workflow)
- **Logic:** Rule-based Compliance Engine (`tools.py`)
- **Memory:** Shared `AgentState` for auditable decision making.

## 📈 Impact Model (Quantified)
*Based on a mid-sized clinic processing 1,000 requests/month:*
- **Time Saved:** Manual process (45 mins) → AI process (5 mins). **~600 hours saved/month.**
- **Cost Reduction:** Labor cost reduced from $26k/mo to under $3k/mo.
- **Revenue Recovery:** 10% reduction in billing errors leads to **~$150k recovered revenue** annually.

## 🛠️ Setup Instructions
1. Clone this repo.
2. `python -m venv venv` and activate it.
3. `pip install -r requirements.txt`
4. Run the agent: `python -m src.main`
