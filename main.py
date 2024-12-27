from openai import OpenAI
import os
from dotenv import load_dotenv
from api.perplexity import make_perplexity_request
from supabase import create_client, Client

load_dotenv()

YOUR_API_KEY = os.getenv("OPENAI_API_KEY")

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

if __name__ == "__main__":
    if not YOUR_API_KEY:
        print("Error: PERPLEXITY_API_KEY not found in .env file")
    else:
        make_perplexity_request(YOUR_API_KEY)
