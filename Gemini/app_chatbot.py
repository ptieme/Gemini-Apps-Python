import google.generativeai as genai 

genai.configure(api_key="deine API_Key hier")
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

chat = model.start_chat(history=[])

response = chat.send_message("zu welchem Zeipunkt soll man Kamerun besuchen ?")
print(response.text)

response = chat.send_message("soll ich demnächst Afrika besuchen  ?")
print(response.text)

print("_"*40)
print(chat.history)
