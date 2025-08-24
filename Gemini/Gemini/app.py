import google.generativeai as genai 

genai.configure(api_key="AIzaSyCG2c87mxzHBscZCmIPykKRPj4xiavV3XY")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


response = model.generate_content("Liste 5 ingrédients pour faire un bon Ramen.", stream=True)
for chunk in response:
    print(chunk.text)