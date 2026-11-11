from pathlib import Path
from dotenv import load_dotenv
import os
import requests

env_path = Path(__file__).parent / "keys" / ".env"
load_dotenv(env_path)

sam_key = os.getenv("SAM_KEY")
pixabay_key = os.getenv("PIXABAY_KEY")

search_key_word = "otter family"

pixabay_url =f"https://pixabay.com/api/?key={pixabay_key}&q={search_key_word}&image_type=photo"

response = requests.get(pixabay_url) 
pixabay_data = response.json()
print (pixabay_data["hits"][3]["pageURL"])

