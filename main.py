import chainlit as cl
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ["OPEN_AI_API_KEY"]
print(openai_api_key)
openai.api_key = openai_api_key
tokens = 0

@cl.on_message
async def main(message: str):
    global tokens
    print('calling openai for response')
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "assistant", "content": "you are a helpful assistant"},
            {"role": "user", "content": message},
        ],
        temperature=1,
    )
    print('received response')
    tokens += response['usage']['total_tokens']
    print(tokens)
    await cl.Message(
        content=f"{response['choices'][0]['message']['content']}",
    ).send()
