from agents.master_agent import run_agent

def test(data_path: str, llm):
    return run_agent(data_path, llm=llm)
