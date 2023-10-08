import chainlit as cl
import openai
import os

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
