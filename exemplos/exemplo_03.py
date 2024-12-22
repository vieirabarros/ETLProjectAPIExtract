import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization":"Bearer xxxx"

}

data ={
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "What is the capital of Brazil?"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
