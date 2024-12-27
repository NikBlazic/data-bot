from openai import OpenAI
import os
from dotenv import load_dotenv
from api.perplexity import make_perplexity_request

load_dotenv()

YOUR_API_KEY = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    if not YOUR_API_KEY:
        print("Error: PERPLEXITY_API_KEY not found in .env file")
    else:
        make_perplexity_request(YOUR_API_KEY)
