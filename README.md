# 🌟 My Python Mini-Projects  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

Welcome to my repository! This repo contains six Python projects showcasing my skills in CLI applications, web scraping, OCR, task management, and data visualization

---

🧮 1. Simple Calculator

📌 Summary
A command-line calculator that performs basic arithmetic operations.

🎯 Use Case
Quickly perform arithmetic operations directly from the terminal.

✨ Key Features

Addition, subtraction, multiplication, division

Handles division by zero

Loop until exit

Input validation for choices and numbers

🛠️ Technical Details

Language: Python 3

Modules: Built-in

Flow: while True with if/elif

Errors: try/except for invalid numbers

✅ 2. Daily Task Manager

📌 Summary
A CLI-based to-do manager that creates daily checklists and saves tasks between sessions.

🎯 Use Case
Track tasks, mark them complete, and carry forward unfinished work.

✨ Key Features

Add tasks

Mark tasks complete/incomplete

JSON file persistence

Automatic date stamping

Move incomplete tasks to next day

Summary of all tasks

🛠️ Technical Details

Language: Python 3

Modules: json, os, datetime, sys, io

Data: List of dicts {task, date}

UI: Menu-driven CLI with 8 options

🌍 3. World GDP Map (Interactive Visualization)

📌 Summary
A Plotly-based choropleth map showing world GDP (2014) interactively.

🎯 Use Case
Visualize GDP across countries for analytics or dashboards.

✨ Key Features

Loads live data from GitHub

Interactive map (hover, zoom)

Reversed “Blues” color scale

Clean borders + annotation

🛠️ Technical Details

Language: Python 3

Modules: pandas, plotly.graph_objects

Output: Interactive map via fig.show()

📚 4. Book Scraper

📌 Summary
A web scraper that extracts book titles and prices from Books to Scrape and saves them to CSV.

🎯 Use Case
Collect pricing and title data for analysis or datasets.

✨ Key Features

Fetches page with requests

Parses HTML with BeautifulSoup

Extracts titles + prices

Saves to books.csv

Prints indexed list of books

🛠️ Technical Details

Language: Python 3

Modules: requests, bs4, csv

Process: GET → parse → extract → save

🔠 5. Letter Lift (OCR Tool)

📌 Summary
An OCR tool that extracts text and characters from an online image using Tesseract.

🎯 Use Case
Convert images into readable text or extract characters for analysis.

✨ Key Features

Downloads image from URL

Converts to grayscale

Performs OCR with pytesseract

Splits text into characters

Prints full text + letter list

🛠️ Technical Details

Language: Python 3

Modules: requests, PIL, pytesseract, io

Process: Download → open → grayscale → OCR → character list

🔍 6. Opti-Scan (OCR)

📌 Summary
Opti-Scan is an OCR tool that downloads an online image, displays it, extracts text using Tesseract, and produces a clean list of characters. Designed for quick testing and automation inside Google Colab.

🎯 Use Case
Extract readable text from any online image and analyze each character individually — useful for preprocessing datasets, automation, and OCR experimentation.

✨ Key Features

Downloads an image directly from a URL

Converts the image to grayscale for improved OCR accuracy

Displays the processed image using Matplotlib

Extracts text using pytesseract

Generates a list of all extracted characters (excluding newlines)

Handles errors gracefully

🛠️ Technical Details

Language: Python 3

Modules: requests, PIL, pytesseract, io, matplotlib

Process:

Install OCR dependencies

Download image from given URL

Convert to grayscale

Display using plt.imshow()

Extract text with Tesseract

Create character list

📊 Comparative Overview
Project	Domain	Key Skills Shown
🧮 Calculator	CLI Utility	Functions, loops, input validation

✅ Task Manager	CLI + File I/O	JSON persistence, menu UI, date handling

🌍 World Map	Data Visualization	Plotly, Pandas, interactive mapping

📚 Book Scraper	Web Scraping	Requests, BeautifulSoup, CSV export

🔠 Letter Lift	OCR Tool	Image handling, Tesseract OCR

🔍 Opti-Scan	OCR Tool	URL-based OCR, image display, character extraction

🚀 How to Run
# Clone the repository
git clone https://github.com/Anvitx911/Mini-Projects.git
cd yourrepo

# Run calculator
python calculator.py
# Run task manager
python task_manager.py
# Run world map
python world_map.py
# Run book scraper
python book_scraper.py
# Run Letter Lift
python letter_lift.py
# Run Opti-Scan
python opti_scan.py

