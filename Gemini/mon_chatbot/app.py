import chainlit as cl
import google.generativeai as genai 

genai.configure(api_key="")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

chat = model.start_chat(history=[]) 

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    response = chat.send_message(message.content, stream=True)

    for chunk in response:
        await msg.stream_token(chunk.text)

    await msg.update()
