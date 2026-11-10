from pathlib import Path #read .env stuff
from dotenv import load_dotenv
import os

import requests

env_path = Path(__file__).parent / "keys" / ".env"
load_dotenv(env_path)

sam_key = os.getenv("SAM_KEY")
pixabay_key = os.getenv("PIXABAY_KEY")

search_key_word = "puppies"

# pixabay_url = "https://pixabay.com/api/?key={pixabay_key}&q={search_key_word}&image_type=photo"
# response = requests.get(pixabay_url)
# pixabay_data= response.json()
# print(pixabay_data)gut

params = {
    "key": pixabay_key,
    "q": search_key_word,
    "image_type": "photo",
}

response = requests.get("https://pixabay.com/api/", params=params)

print(response.status_code)
print(response.text)

data = response.json()