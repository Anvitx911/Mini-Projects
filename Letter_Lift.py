!pip install pytesseract
# Run & Install it 
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
img = img.convert("L")  # Convert to grayscale for better OCR results
# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(img)
print("Extracted Text:\n")
print(text)
# Create a list of all letters (excluding newlines)
letters = list(text.replace("\n", ""))
print("\nList of all letters:\n", letters)
