# 🌟 My Python Mini-Projects  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

Welcome to my repository! This repo contains **five Python projects** that showcase my skills in CLI applications, web scraping, OCR, task management, and data visualization.  

---

## 🧮 1. Simple Calculator  

### 📌 **Summary**  
A clean **command-line calculator** that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

### 🎯 **Use Case**  
Quickly perform arithmetic operations directly from the terminal.

### ✨ **Key Features**  
- ➕ **Addition**, ➖ **Subtraction**, ✖️ **Multiplication**, ➗ **Division**  
- 🚫 Handles **division by zero** gracefully  
- 🔄 **Loop until exit** with user-friendly prompts  
- ✅ **Input validation** for choices and numbers  

### 🛠️ **Technical Details**  
- **Language:** Python 3  
- **Modules:** Built-in (`input`, `print`)  
- **Control Flow:** `while True` loop with `if/elif` branching  
- **Error Handling:** `try/except` for invalid numeric input  

---

## ✅ 2. Daily Task Manager  

### 📌 **Summary**  
A **CLI-based to-do manager** to create daily checklists, mark tasks complete/incomplete, and persist data between sessions.

### 🎯 **Use Case**  
Track daily tasks, review progress, and carry forward unfinished items.

### ✨ **Key Features**  
- 📝 Add tasks interactively  
- 🔎 Review tasks & mark **complete ✅** or **incomplete ❌**  
- 📂 **Persistent storage** in JSON file (`my_tasks.json`)  
- 📆 Automatic **date stamping** for task completion  
- ♻️ Move incomplete tasks to today’s checklist  
- 📊 Summary of all tasks  

### 🛠️ **Technical Details**  
- **Language:** Python 3  
- **Modules:** `json`, `os`, `datetime`, `sys`, `io`  
- **Data Structures:** Lists + dictionaries with `{task, date}`  
- **Persistence:** UTF-8 encoded JSON file  
- **UI:** Menu-driven CLI with 8 options  

---

## 🌍 3. World GDP Map (Interactive Visualization)  

### 📌 **Summary**  
An **interactive choropleth map** of global GDP (2014) using Plotly and Pandas.

### 🎯 **Use Case**  
Visualize GDP across countries; great for dashboards or analytics.

### ✨ **Key Features**  
- 📡 Fetches live data from **GitHub CSV**  
- 🗺️ Interactive **Plotly choropleth** (hover, zoom)  
- 🎨 Custom **color scale** (‘Blues’, reversed) with dark gray borders  
- 🔗 Annotation link to **CIA Factbook**  

### 🛠️ **Technical Details**  
- **Language:** Python 3  
- **Modules:** `pandas`, `plotly.graph_objects`  
- **Data Source:**  
  `https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv`  
- **Output:** `fig.show()` → opens interactive map  

---

## 📚 4. Book Scraper  

### 📌 **Summary**  
A **web scraper** that extracts book titles and prices from [Books to Scrape](http://books.toscrape.com/) and saves the data into a CSV file.

### 🎯 **Use Case**  
Collect pricing and title data for analysis, price comparison, or dataset building.

### ✨ **Key Features**  
- 🌐 Scrapes book titles and prices from an online bookstore  
- ⚡ Uses **requests** to fetch HTML and **BeautifulSoup** to parse content  
- 📄 Stores results in `books.csv` with **CSV writer**  
- 🔢 Prints all scraped books with their index  

### 🛠️ **Technical Details**  
- **Language:** Python 3  
- **Modules:** `requests`, `bs4` (BeautifulSoup), `csv`  
- **Process:**  
  1. GET request to the website  
  2. Parse HTML to find all books  
  3. Extract `title` and `price`  
  4. Save data into `books.csv` with headers  

---

## 🔠 5. Letter Lift (OCR Tool)  

### 📌 **Summary**  
An **OCR (Optical Character Recognition) tool** that extracts text and individual characters from an online image using Tesseract.

### 🎯 **Use Case**  
Convert images containing text into machine-readable content, or extract letters for analysis/training.

### ✨ **Key Features**  
- 🌐 Downloads an image from a URL automatically  
- 🖼️ Uses **Pillow (PIL)** to open and convert the image  
- 🔍 Applies **pytesseract** OCR to extract text  
- ✂️ Splits extracted text into individual letters for detailed processing  
- 📝 Prints the extracted text and letters  

### 🛠️ **Technical Details**  
- **Language:** Python 3  
- **Modules:** `requests`, `PIL` (Pillow), `pytesseract`, `io`  
- **Process:**  
  1. Download image from URL  
  2. Open with `Image.open(BytesIO(...))`  
  3. (Optional) Convert to grayscale for better OCR  
  4. Extract text with `pytesseract.image_to_string()`  
  5. Create list of letters by stripping newlines  

---

## 📊 Comparative Overview  

| Project | Domain | Key Skills Shown |
|---------|--------|------------------|
| 🧮 **Calculator** | CLI Utility | Functions, loops, input validation |
| ✅ **Task Manager** | CLI + File I/O | JSON persistence, modular design, date stamping, UTF-8 handling |
| 🌍 **World Map** | Data Visualization | Pandas, Plotly, interactive choropleth |
| 📚 **Book Scraper** | Web Scraping | Requests, BeautifulSoup, CSV export |
| 🔠 **Letter Lift** | OCR Tool | Image download, Pillow, Tesseract OCR |

---

## 🚀 How to Run  

```bash
# Clone this repository
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

# Run calculator
python calculator.py

# Run task manager
python task_manager.py

# Run world map visualization
python world_map.py

# Run book scraper
python book_scraper.py

# Run Letter Lift OCR tool
python letter_lift.py
