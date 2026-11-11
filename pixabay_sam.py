from pathlib import Path
from dotenv import load_dotenv
import io, os, requests, webbrowser
from PIL import Image, ImageDraw
import requests

env_path = Path(__file__).parent / "keys" / ".env"
load_dotenv(env_path)

sam_key = os.getenv("SAM_KEY")
pixabay_key = os.getenv("PIXABAY_KEY")

search_key_word = "otters"

pixabay_url =f"https://pixabay.com/api/?key={pixabay_key}&q={search_key_word}&image_type=photo"

response = requests.get(pixabay_url) 
pixabay_data = response.json()
pixabay_img= pixabay_data["hits"][2]["webformatURL"]
with open("pixabay_download.jpg","wb")as file:
     file.write(requests.get(pixabay_img).content)


payload = {
    "image": {"type": "url", "value": pixabay_img},
    "prompts": [
        {"type": "text", "text": "otter"},
        {"type": "text", "text": "eyes"},
    ],
    "output_prob_thresh": 0.5,
    "format": "polygon", 
}

sam_response = requests.post(
    "https://serverless.roboflow.com/sam3/concept_segment",
    headers={"Authorization": f"Bearer {sam_key}"},
    json=payload,
)
sam_response.raise_for_status()
sam_data = sam_response.json()

result_img = Image.open(io.BytesIO(requests.get(pixabay_img).content)).convert("RGBA")
overlay = Image.new("RGBA", result_img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

colors = [(255, 80, 80), (80, 160, 255), (80, 220, 120), (255, 200, 60)]

for i, prompt_result in enumerate(sam_data["prompt_results"]):
    label = prompt_result["echo"]["text"]
    r, g, b = colors[i % len(colors)]
    print(label, len(prompt_result["predictions"]), "instances")

    for pred in prompt_result["predictions"]:
        for polygon in pred["masks"]:
            pts = [tuple(p) for p in polygon]
            if len(pts) < 3:
                continue
            draw.polygon(pts, fill=(r, g, b, 90), outline=(r, g, b, 255), width=3)
        # label near the first point
        if pred["masks"] and pred["masks"][0]:
            x, y = pred["masks"][0][0]
            draw.text((x, y - 12), f'{label} {pred["confidence"]:.2f}', fill=(r, g, b, 255))

result = Image.alpha_composite(result_img, overlay).convert("RGB")

result.save("Sam_output.png")
print("Sam return img saved to", os.path.abspath("Sam_output.png"))
result.show()   