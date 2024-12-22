import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=openai_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)