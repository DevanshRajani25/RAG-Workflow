# embeddings/embed_chunks.py

from sentence_transformers import SentenceTransformer

def embed_chunks(chunks_with_metadata: list) -> list:
    """
    Converts chunks into vectors (embeddings)
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [chunk["text"] for chunk in chunks_with_metadata]

    embeddings = model.encode(texts)

    # Adding vectors in list of chunks_with_metadata
    for i, chunk in enumerate(chunks_with_metadata):
        chunk["embedding"] = embeddings[i].tolist()
    
    return chunks_with_metadata