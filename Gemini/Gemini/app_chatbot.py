import google.generativeai as genai 

genai.configure(api_key="AIzaSyCG2c87mxzHBscZCmIPykKRPj4xiavV3XY")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

chat = model.start_chat(history=[])

response = chat.send_message("Quelle est la meilleure période pour visiter Tokyo et admirer les fleurs de cerisier ?")
print(response.text)

response = chat.send_message("Dois-je ensuite visiter Kyoto ?")
print(response.text)

print("_"*40)
print(chat.history)