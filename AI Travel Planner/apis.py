from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

from google import genai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (ports/websites) to connect
    allow_credentials=True,
    allow_methods=["*"],  # Crucial: Allows OPTIONS, POST, GET, etc.
    allow_headers=["*"],  # Crucial: Allows Content-Type headers
)

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )

client = genai.Client(api_key="AQ.Ab8RN6LRM7Q-JcCQ1GlY_Qa3s0HBXB1fThchuDZVpHanM4t-kA")


@app.post("/trip-plan")
def getData(data: dict):
    print(data)
    print(data["destination"])
    print(data["days"])
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Suggest a " + data["days"] + " days itenary for" + data["destination"] + "."
    )
    # response = client.responses.create(
    #     model="gpt-5",
    #     input="Suggest 3 places to visit in Rishikesh."
    # )
    return {
        "message": response.text
    }



# openai key:  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