# retrieve/similartity_search.py

import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )

def similarity_search(query: str, chunks: list, top_k: int = 3):
    # create model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # embed user query
    user_query_embedding = model.encode(query)

    # retrieve relevent chunks for user query
    scores = []
    for chunk in chunks:
        score = cosine_similarity(
            user_query_embedding,
            np.array(chunk["embedding"])
        )
        scores.append((score, chunk))
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:top_k]
