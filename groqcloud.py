import os 
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
while True:
    content = input('>')
    if content == "exit": break
    chat = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": content
            }
        ],
        model="deepseek-r1-distill-llama-70b"
    )
    print(chat.choices[0].message.content)
