import csv
from bs4 import BeautifulSoup

html_filename = 'content.html'
with open(html_filename, 'r', encoding='utf-8') as file:
    html_content = file.read()
    
soup = BeautifulSoup(html_content, 'lxml')

items = soup.find_all('div', {'data-testid': 'gallery-item-item'})
print(f"Number of items found: {len(items)}")