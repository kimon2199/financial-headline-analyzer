import os
from dotenv import load_dotenv
from transformers import pipeline
from huggingface_hub import login

# Log into Hugging Face using the token
load_dotenv()
huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
login(huggingface_token)

# Load the sentiment analysis pipeline with FinBERT
pipe = pipeline("text-classification", model="yiyanghkust/finbert-tone")

def analyze_sentiment(headlines):
    if isinstance(headlines, str):
        headlines_list = headlines.strip().split('\n')
    else:
        headlines_list = headlines
    sentiment_results = pipe(headlines_list)

    output = []
    for headline, sentiment in zip(headlines_list, sentiment_results):
        output.append((sentiment['label'], headline))
    
    return output
