# Example stub
from langchain.chains import load_chain_from_yaml

# Load your file chunks
chunks = ["Revenue increased by 15%...", "..."]

# Load agent chain from agent.yaml
chain = load_chain_from_yaml("agent.yaml")

# Run the chain
result = chain.run({"input": "\n".join(chunks)})
print(result)
