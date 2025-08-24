import chainlit as cl
import google.generativeai as genai 

genai.configure(api_key="")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

@cl.on_chat_start
async def on_chat_start():
    file_input = cl.AskFileMessage(
        content = "Télécharger une image",
        accept=["image/*"],
        max_size_mb=5
    )

    files = None
    while files == None:
        files = await file_input.send()

    # Réinitialiser la demande d'image
    file_input.content = ""
    await file_input.update()

    image_file = files[0]

    cl.user_session.set("uploaded_image", image_file.path)

    image = cl.Image("image1", display="inline", path=image_file.path)

    await cl.Message(
        content=f"`{image_file.name}` téléchargée ! Tu peux maintenant poser ta question concernant l'image",
        elements=[image]
    ).send()

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    # Obtenir le chemin d'accès à l'image à partir de la session utilisateur
    image_path = cl.user_session.get("uploaded_image")
    image = genai.upload_file(path=image_path)

    await cl.sleep(1)

    response = model.generate_content([
        message.content,
        image 
    ])

    msg.content = response.text
    await msg.update()
