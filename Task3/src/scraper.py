import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []

    # Use the correct class for BBC News headlines
    for item in soup.find_all('h3', class_='gs-c-promo-heading__title'):
        text = item.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines

def save_headlines_to_file(headlines, filename):
    with open(filename, 'w') as file:
        for headline in headlines:
            file.write(headline + '\n')

from utils import fetch_headlines, write_headlines_to_file

if __name__ == "__main__":
    url = 'https://www.bbc.com/news'
    headlines = fetch_headlines(url)
    write_headlines_to_file(headlines, r'c:\Users\Mohan babu\html\task3\news-headlines-scraper\top_headlines.txt')
    print("Headlines have been successfully scraped and saved to 'c:\\Users\\Mohan babu\\html\\task3\\news-headlines-scraper\\top_headlines.txt'.")
    print(f"Found {len(headlines)} headlines")

from utils import fetch_headlines, write_headlines_to_file