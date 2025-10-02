import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all('article', class_='product_pod')
book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    book_data.append({'title': title, 'price': price})
for i, book in enumerate(book_data, start=1):
    print(f"{i}. {book['title']} - {book['price']}")
import csv
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['title', 'price'])
    writer.writeheader()
    writer.writerows(book_data)
print("Data is saved to books.csv")
