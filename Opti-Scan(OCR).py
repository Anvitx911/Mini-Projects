# Install required packages (run once in Colab)
!apt install tesseract-ocr -y
!pip install pytesseract pillow requests
from PIL import Image
import pytesseract
import requests
from io import BytesIO
import matplotlib.pyplot as plt
# Image URL 
image_url = "https://images.unsplash.com/photo-1608999383953-d61f5d9c1ace?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
try:
    # Download the image
    response = requests.get(image_url)
    response.raise_for_status()
    # Open the image and convert to grayscale
    img = Image.open(BytesIO(response.content)).convert("L")
    # Show the image
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.show()
    # Extract text from the image
    text = pytesseract.image_to_string(img)
    print("\nExtracted Text:\n")
    if text.strip():
        print(text)
    else:
        print("(No readable text found)")
    # List all characters (excluding newlines)
    letters = list(text.replace("\n", ""))
    print("\nList of letters:\n", letters)
except Exception as e:
    print("Error:", e)
