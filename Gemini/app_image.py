import google.generativeai as genai 
import PIL

genai.configure(api_key="Deine API_Key")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
img = PIL.Image.open("images/fantasy.jpeg")

response = model.generate_content(["Kannst das Bild analysieren?", img])
print(response.text)
