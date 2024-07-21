import csv
from bs4 import BeautifulSoup

# Read
html_filename = 'expanded.html'
with open(html_filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Print
print(html_content[:1000])

# Parse
soup = BeautifulSoup(html_content, 'lxml')

# Check total
items = soup.find_all('div', {'data-testid': 'gallery-item-item'})
print(f"Number of items found: {len(items)}")

# Extract the data
data = []
for item in items:
    try:
        print("Processing item:")
        print(item.prettify())

        # Find elements
        title_elem = item.find(attrs={'data-testid': 'gallery-item-title'})
        description_elem = item.find(attrs={'data-testid': 'gallery-item-description'})
        img_elem = item.find('img')

        # Extract
        title = title_elem.get_text(strip=True) if title_elem else ''
        description = description_elem.get_text(strip=True) if description_elem else ''
        img_src = img_elem['src'] if img_elem and 'src' in img_elem.attrs else ''
        
        data.append([title, description, img_src])
    
    except Exception as e:
        print(f"An error occurred while processing an item: {e}")

# Write
csv_filename = 'gallery_items.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Header
    writer.writerow(['Title', 'Description', 'Image Source'])
    # Rows
    writer.writerows(data)

print(f"Data successfully written to {csv_filename}")
