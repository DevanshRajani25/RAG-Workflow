# ingest/chunks_text.py

def chunk_text(text: str) -> list:
    """
    Splits text into chunks using paragraphs.
    """
    chunks = []
    for para in text.split("\n\n"):
        para = para.strip()
        if len(para) > 0:
            chunks.append(para)
    return chunks