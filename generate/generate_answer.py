from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def generate_answer(user_query: str, retrieved_chunks: list) -> str:
    """
    Generates answer strictly from retrieved chunks.
    """
    context = ""
    for score, chunk in retrieved_chunks:
        context += f" - {chunk['text']}\n"
        messages = [
            {
                "role": "system",
                "content": ("""
                    You are a customer support bot.
                    You have to give answer of user's question only from the below provided information.
                    If the answer is not present, then say: 
                    "I don't have enough context to answer this question!"
                    End answer with asking to user that any other queries?
                """
                )
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{user_query}
"""
            }
        ]
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content.strip()