# String-Api-Asm

Searches Pixabay for a photo, sends it to **SAM 3** (via Roboflow) to segment objects from text prompts, and saves the image with colored mask outlines and labels.

## Setup
Clone the whole repo.

1. **Install dependencies** (Python 3):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Get API keys** (both free):
   - **Pixabay:** make an account, then copy your key from the [Pixabay API page](https://pixabay.com/service/about/api/).
   - **Roboflow (for SAM 3):** make an account, create a new workspace, then follow [Find your Roboflow API key](https://docs.roboflow.com/reference/authentication/authentication/find-your-roboflow-api-key).

3. **Add your keys** in `keys/.env` (this folder is git-ignored):
   ```
   PIXABAY_KEY=your_pixabay_key
   SAM_KEY=your_roboflow_key
   ```

## Run

```bash
python pixabay_sam.py
```

Output: `pixabay_download.jpg` (the original photo) and `Sam_output.png` (with masks), both saved in the folder you run the script from.

## Docs

- [Pixabay API](https://pixabay.com/api/docs/)
- [SAM 3 on Roboflow (concept segmentation)](https://docs.roboflow.com/models/supported-models/sam3#sam3-concept-segmentation-pcs)
