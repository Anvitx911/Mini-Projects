# 🌟 My Python Mini-Projects  

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
  4. Save data into
