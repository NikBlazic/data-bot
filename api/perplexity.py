import requests
import json
import os

def make_perplexity_request(api_key: str):
    url = "https://api.perplexity.ai/chat/completions"
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": "Can you insert data into a database from a pdf file?"
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        print("Raw Response:", response.text)
        
        if response.text:
            try:
                response_json = response.json()
                print("\nFormatted Response:")
                print(json.dumps(response_json, indent=2))
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON response: {e}")
        else:
            print("Empty response received")
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        if hasattr(e.response, 'text'):
            print(f"Error response: {e.response.text}") 