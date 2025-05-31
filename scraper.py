import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set the URL of the website to scrape
URL = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
# Create a session
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Create 'images' directory if not exists
if not os.path.exists('images'):
    os.makedirs('images')

# 1. Scrape and Save Text
all_text = soup.get_text(separator='\n', strip=True)

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write(all_text)

print("Text content saved to text.txt")

# 2. Scrape and Save Images
img_tags = soup.find_all('img')
img_count = 0

for img in img_tags:
    img_url = img.get('src')
    if img_url:
        # Handle relative URLs
        img_url = urljoin(URL, img_url)
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join('images', f'image_{img_count}.jpg')
            with open(img_name, 'wb') as f:
                f.write(img_data)
            print(f"Saved image: {img_name}")
            img_count += 1
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

print(f"Downloaded {img_count} images.")
