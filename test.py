from llama_index.bge_m3 import BGEM3Index


if __name__ == "__main__":
    from llama_index.core import Settings
    from llama_index.core import Document

    Settings.llm = None
    Settings.chunk_size = 512

    # Load Documents
    sentences = [
        "BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.", 
        "BM25 is a bag-of-words retrieval function that ranks a set of documents based on the query terms appearing in each document"
    ]
    documents = [Document(doc_id=i, text=s) for i, s in enumerate(sentences)]
    # Create Index
    index = BGEM3Index.from_documents(documents, weights_for_different_modes=[0.4, 0.2, 0.4])
    # Get retriever
    retriever = index.as_retriever()
    nodes = retriever.retrieve("What is BGE M3?")
    print(nodes)

    query_engine = index.as_query_engine()
    response = query_engine.query(
        "What is BGE-M3?"
    )
    print(response)

    print("All tests passed!")
