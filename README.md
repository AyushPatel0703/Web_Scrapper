# 📊 Flipkart Page Scraper

A Python-based web scraping tool that extracts textual content and images from Flipkart’s mobiles category page using `requests` and `BeautifulSoup`.

---

## 📌 Project Overview

This script performs the following tasks:

- 🔍 Scrapes all visible **text** from the Flipkart page and saves it to `text.txt`.
- 🖼 Downloads all **images** on the page and stores them in an `images/` directory.
- 🌐 Resolves relative URLs using `urljoin` to ensure all resources are correctly fetched.
- 🗂 Automatically creates necessary directories if they don’t exist.

---

## 🛠️ Technologies Used

- Python 3.x
- [Requests](https://docs.python-requests.org/en/master/)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html)

---

## 📁 Project Structure

web-scraper/
- ├── scraper.py # Main script file
- ├── text.txt # Extracted text content
- ├── images/ # Directory containing downloaded images
