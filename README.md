# RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for customer support queries on policies like refunds, returns, and warranties.

## Features

- **Data Ingestion**: Loads text data, chunks it by paragraphs, and adds metadata based on keywords (refund, return, warranty, general).
- **Embeddings**: Uses Sentence Transformers (`all-MiniLM-L6-v2`) to generate vector embeddings for chunks.
- **Retrieval**: Performs cosine similarity search to find top-k relevant chunks for user queries.
- **Generation**: Uses Azure OpenAI to generate answers strictly from retrieved context.

## Project Structure

- `main.py`: Main script to run the RAG pipeline.
- `ingest/`: Data loading, chunking, and metadata addition.
- `embeddings/`: Embedding generation.
- `retrieve/`: Similarity search.
- `generate/`: Answer generation using Azure OpenAI.
- `Data/`: Raw and processed data files.

## Requirements

- Python 3.x
- sentence-transformers
- openai
- python-dotenv
- numpy

Install dependencies:
```
pip install sentence-transformers openai python-dotenv numpy
```

## Setup

1. Place your policy text data in `Data/raw/policy_support.txt`.
2. Set up Azure OpenAI environment variables in a `.env` file:
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_API_VERSION`
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_DEPLOYMENT_NAME`
3. Run ingestion steps (uncomment in `main.py` if needed) to process data.
4. Run `python main.py` and enter your query.

## Usage

Run the main script and input a customer support query. The system will retrieve relevant policy chunks and generate an answer.
