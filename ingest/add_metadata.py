# ingest/add_metadata.py

def add_metadata(chunks: list) -> list:
    """
    Add metadata to each chunks.
    """
    chunks_data = []
    for i, chunk in enumerate(chunks):
        lower_chunk = chunk.lower()

        if "refund" in lower_chunk:
            section = "refund"
        elif "return" in lower_chunk:
            section = "return"
        elif "warranty" in lower_chunk:
            section = "warranty"
        else:
            section = "general_chatbot_queries"
        
        chunks_data.append({
            "chunk_id": f"chunk_{i+1}",
            "section": section,
            "text": chunk
        })
    return chunks_data