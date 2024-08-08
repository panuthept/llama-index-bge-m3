# llama-index-bge-m3
Integrating BGE-M3 into Llama-index

# Installation

```
git clone https://github.com/panuthept/llama-index-bge-m3.git
cd llama-index-bge-m3

pip install -e .
```

# Usage
## Retrieve

```python
from llama_index.bge_m3 import BGEM3Index

index = BGEM3Index.from_documents(documents)
retriever = index.as_retriever()

nodes = retriever.retrieve("What is BGE-M3?")
print(nodes)
```

## Query

```python
from llama_index.bge_m3 import BGEM3Index

index = BGEM3Index.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is BGE-M3?")
print(response)
```
