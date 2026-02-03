from ingest.load_data import load_data
from ingest.chunk_text import chunk_text
from ingest.add_metadata import add_metadata
import json
from embeddings.embed_chunks import embed_chunks
from retrieve.similarity_search import similarity_search
from generate.generate_answer import generate_answer

file_path = r"Data\raw\policy_support.txt"
chunk_path = r"Data\processed\chunks.txt"
chunk_with_metadata_path = r"Data\processed\chunks_with_metadata.json"
chunk_metadata_with_embeddings_path = r"Data\processed\chunks_metadata_with_embeddings.json"

# # Loading data
# try:
#     data = load_data(file_path)
#     if len(data) > 0:
#         print("Data loaded successfully!")
# except Exception as e:
#     print(f"Something went wrong while loading data: {e}")
#     exit()

# Dividing into chunks
# try:
#     chunked_data = chunk_text(data)
#     if len(chunked_data) > 0:
#         with open(chunk_path, "w", encoding="utf-8") as f:
#             for i, chunk in enumerate(chunked_data):
#                 f.write(f"Chunk {i+1} : \n{chunk}\n\n")
#         print(f"Text divided & loaded into chunks successfully! Length of chunks: {len(chunked_data)}")
# except Exception as e:
#     print(f"Something went wrong in dividing text into chunks: {e}")
#     exit()

# # Add metadata
# try:
#     chunks_with_metadata = add_metadata(chunked_data)
#     with open(chunk_with_metadata_path, "w", encoding="utf-8") as f:
#         json.dump(chunks_with_metadata, f, indent=4)
#     print(f"Chunked data with metadata loaded into file!")
# except Exception as e:
#     print(f"Something went wrong while adding metadata into chunks: {e}")
#     exit()

# Add embeddings(vectors) in chunks with metadata
# try:
#     chunks_metadata_with_embeddings = embed_chunks(chunks_with_metadata)
#     with open(chunk_metadata_with_embeddings_path, "w", encoding="utf-8") as f:
#         json.dump(chunks_metadata_with_embeddings, f, indent=4)
#         print("Embeddings generated & stored successfully!")
# except Exception as e:
#     print(f"Something went wrong in generating embeddings: {e}") 

# load chunks with embeddings & similarity search
with open(chunk_metadata_with_embeddings_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)

query = input("Please enter your Query: ")

results = similarity_search(query, chunks, top_k=3)
# print("\nTop Matching Chunks:\n")
# for score, chunk in results:
#     print(f"Score: {score:.4f}")
#     print(f"Section: {chunk['section']}")
#     print(chunk["text"])
#     print("-" * 50)

answer = generate_answer(query, results)

print(f"Answer : {answer}")