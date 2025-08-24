import chainlit as cl
import google.generativeai as genai 

genai.configure(api_key="AIzaSyCG2c87mxzHBscZCmIPykKRPj4xiavV3XY")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

@cl.on_chat_start
async def on_chat_start():
    file_input = cl.AskFileMessage(
        content="Télécharger un audio",
        accept=["audio/*"],
        max_size_mb=15
    )

    files = None
    while files == None:
        files = await file_input.send()

    # Réinitialiser la demande d'audio
    file_input.content = ""
    await file_input.update()

    audio_file = files[0]

    cl.user_session.set("uploaded_audio", audio_file.path)

    audio = cl.Audio(name="audio1", display="inline", path=audio_file.path)

    await cl.Message(
        content=f"`{audio_file.name}` téléchargée ! Tu peux maintenant poser ta question concernant l'audio",
        elements=[audio]
    ).send()

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    # Obtenir le chemin d'accès à l'audio à partir de la session de l'utilisateur
    audio_path = cl.user_session.get("uploaded_audio")
    audio = genai.upload_file(path=audio_path)

    await cl.sleep(1)

    response = model.generate_content([
        message.content,
        audio
    ])

    msg.content = response.text
    await msg.update()