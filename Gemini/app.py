import google.generativeai as genai 

genai.configure(api_key="Deine API_Key")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


response = model.generate_content("Listet mal 5 Zutaten mit dem man ein Pizza machen kann.", stream=True)
for chunk in response:
    print(chunk.text)
