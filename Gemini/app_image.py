import google.generativeai as genai 
import PIL

genai.configure(api_key="AIzaSyCG2c87mxzHBscZCmIPykKRPj4xiavV3XY")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
img = PIL.Image.open("images/fantasy.jpeg")

response = model.generate_content(["écris-moi une histoire fantastique pour un enfant d'après l'image", img])
print(response.text)