# SME Insights Agent

SME Insights Agent is a multi-agent AI assistant that analyzes financial documents (e.g., income statements) and provides clear, actionable insights.

Built using [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/), and [AgentOS](https://agentos.org/), it simulates a team of analysts who:
- Summarize business performance
- Detect risks and missed opportunities
- Suggest next steps for growth

## 🚀 How It Works

1. You provide a financial document (CSV or PDF)
2. AgentOS loads the multi-agent chain:
   - **Financial Summarizer Agent**
   - **Risk & Opportunity Agent**
   - **Action Advisor Agent**
3. Output is returned in structured format (JSON)

## 🛠️ How to Run (in Replit or locally)

```bash
pip install -r requirements.txt

# Run the agent on a sample file
agentos run agent.yaml test_data/sample_income.csv
```


📂 Folder Structure
agents/             → LangChain agent logic
test_data/          → Sample CSV input files
agent.yaml          → AgentOS config
requirements.txt    → Dependencies



🤖 Technologies
AgentOS 🧠


LangChain 🧩
OpenAI GPT-4o ⚙️
Python 3.11 🐍


🧑‍💻 Team
Built by the PennyPilot Team for the GenAI Hackathon.
