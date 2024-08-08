# llama-index-bge-m3
Integrating BGE-M3 into Llama-index

# Installation

```
git clone https://github.com/panuthept/llama-index-bge-m3.git
cd llama-index-bge-m3

pip install -e .
```

# Usage

```python
from llama_index.bge_m3 import BGEM3Index

index = BGEM3Index.from_documents(documents)
retriever = index.as_retriever()

nodes = retriever.retrieve("What is BGE-M3?")
```
