import os
import asyncio
from llama_api_client import LlamaAPIClient
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("LLAMA_api_key")
client = LlamaAPIClient(
    api_key= api_key,
    base_url="https://api.llama.com/v1/",
)


async def main(msg) -> None|str:
    completion = client.chat.completions.create(
        model="Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[
        {
          "role": "system",
          "content": f"Your the News Editor Who's task read the {msg} and genrate the 10 headlines in controversial style to attract the audience"
        },
        {
            "role":"user",
            "content":msg
        }
        ],
        )
    print(completion.completion_message.content.text) # type: ignore

msg = input("Enter the news: ")
asyncio.run(main(msg))