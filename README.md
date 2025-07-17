<img width="1024" height="1024" alt="B7235C38-F097-45D1-BFF7-58D9AFAEEF58" src="https://github.com/user-attachments/assets/d1d7adbf-ca85-4680-9a3c-02438c7ec702" />
# 🧠 SME Insights Agent

**SME Insights Agent** is an AI-powered assistant designed to help small and medium enterprises quickly analyze financial documents and extract actionable business insights — without requiring technical knowledge.

🚀 Built for the GenAI Hackathon, this project uses **LangChain**, **AgentOS**, and the **built-in GenAI provider** to deliver a fully local, no-key-needed experience.

---

## ✅ Features

- 📄 Upload a financial document (PDF or CSV)
- 🧠 4-agent system:
  - **Orchestrator Agent**
  - **Financial Summarizer Agent**
  - **Risk & Opportunity Agent**
  - **Action Advisor Agent**
- 🔗 Powered by `agent.yaml` via **AgentOS UI**
- 🛠️ No OpenAI or external API keys required!

---

## 💻 How It Works

1. User uploads a document (e.g. income statement)
2. `agent.yaml` triggers AgentOS chain:
   - Agent A: **Summarizes** financial performance
   - Agent B: **Identifies risks/opportunities**
   - Agent C: **Suggests next steps**
3. Results are returned in an organized output

---

## 🛠️ Tech Stack

- Python 3
- LangChain
- AgentOS Protocol
- FastAPI
- Replit (for live prototyping)
- GitHub

---

## 📁 Repo Structure

```plaintext
├── agents/
│   ├── __init__.py
│   ├── master_agent.py
├── mlruns/
├── agent.yaml
├── test_agent.py
├── README.md
├── requirements.txt
└── …
```
Install dependencies:

```
pip install -r requirements.txt
```
Run the app (example):

```
python3 -m agents.test_agent
```

Optionally run via AgentOS UI (agent.yaml based)


📁 File Structure
```
├── agents/
│   ├── __init__.py
│   ├── master_agent.py
├── mlruns/
├── agent.yaml
├── test_agent.py
├── requirements.txt
├── README.md
```

👥 Team – PennyPilot

Serhii Mazurenko – Project Lead, Developer, Agent Logic & Replit Integration
Led design of the multi-agent logic, integrated Replit and GitHub, and coordinated the hackathon submission.

Jing Li – Product Strategy & Documentation Support
Provided feedback and review on agent workflow, coordinated via Discord & Trello, and supported communication with mentors.

Wasif Saeed – Initial Contributor (Research & Setup)
Participated in early-stage development and initial research for LangChain and document processing. Contributed to early discussions and experimentation.


✅ Submission Highlights
```
✅ AgentOS Protocol fully integrated
✅ Built-in GenAI provider (no OpenAI keys needed)
✅ Public GitHub repo & Replit test environment
✅ Discord, GitHub, and Trello collaboration
```
🚧 Note: Due to time constraints and integration issues, the live system is not fully functional.
However, the codebase includes:
- A working multi-agent chain via `agent.yaml`
- A file upload interface via FastAPI
- Test scripts to simulate document analysis

We would continue post-hackathon to bring it to production quality.
