# Install required packages
!apt install tesseract-ocr -y
!pip install pytesseract pillow
from PIL import Image
import pytesseract
from google.colab import files
# Upload an image
print("Upload an image:")
uploaded = files.upload()
# Get the filename
filename = list(uploaded.keys())[0]
print("Image uploaded:", filename)
# Open the image and convert to grayscale
img = Image.open(filename).convert("L")
# Extract text with Tesseract
text = pytesseract.image_to_string(img)
# Print the extracted text
print("\nExtracted Text:\n")
if text.strip():
    print(text)
else:
    print("(No readable text found)")
# Create a list of characters (excluding newlines)
letters = list(text.replace("\n", ""))
print("\nList of letters:")
print(letters)
