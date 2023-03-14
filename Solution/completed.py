import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.domain = urlparse(url).netloc
        self.links_file = os.path.join('scrapped_data', f'{self.domain}.txt')
        self.images_file = os.path.join(
            'scrapped_data', f'{self.domain}_img.txt')

        # Create a directory for scraped data if it doesn't exist
        if not os.path.exists('scrapped_data'):
            os.makedirs('scrapped_data')

    def scrape_links(self):
        # Send HTTP request
        response = requests.get(self.url)

        # Parse HTML content with Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links on the page
        links = soup.find_all('a')

        # Save link URLs and text to a file
        with open(self.links_file, 'w', encoding='utf-8') as f:
            for link in links:
                f.write(f'URL: {link.get("href")}\nText: {link.text}\n')

    def scrape_images(self):
        # Send HTTP request
        response = requests.get(self.url)

        # Parse HTML content with Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image tags on the page
        images = soup.find_all('img')

        # Save image URLs to a file
        with open(self.images_file, 'w', encoding='utf-8') as f:
            for img in images:
                f.write(f'{img.get("src")}\n')


# Example usage
url = 'https://www.kibo.school'
scraper = WebScraper(url)
scraper.scrape_links()
scraper.scrape_images()
