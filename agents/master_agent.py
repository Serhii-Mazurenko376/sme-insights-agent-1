def run_agent(input_file_path: str, llm=None) -> dict:
    import pandas as pd
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain

    df = pd.read_csv(input_file_path)
    data_str = df.head().to_string(index=False)

    prompt = PromptTemplate.from_template("""
    You are a financial analyst. Given this dataset, provide:
    1. A business performance summary
    2. Any red flags or missed opportunities
    3. Actionable next steps

    Dataset:
    {data}
    """)

    # ✅ Use injected LLM from AgentOS or test harness
    if llm is None:
        raise ValueError("LLM must be passed from AgentOS or test harness")

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(data=data_str)

    return {"summary": result}
