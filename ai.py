import google.generativeai as genai
import os

genai.configure(api_key=os.getenv(AIzaSyDsx3WGxuesJBKkid2xzGLoP_Sm-iXHKAs))

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Regarding carrier realted guidance")

print(response.text)
