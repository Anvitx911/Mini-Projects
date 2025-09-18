pip install pytesseract pillow
from PIL import Image
import pytesseract
import requests
from io import BytesIO
# URL of the image
image_path = "https://pbs.twimg.com/media/GeXohg4bsAEJunP.jpg"
# Download the image from the URL
response = requests.get(image_path)
response.raise_for_status()  # raise error if download failed
# Open image from bytes
img = Image.open(BytesIO(response.content))
img = img.convert("L")
text = pytesseract.image_to_string(img)
print("Extracted Text:\n")
print(text)
letters = list(text.replace("\n", ""))  
print("\nList of letters:\n", letters)
