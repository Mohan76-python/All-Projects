import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []

    # Print all h3 tags to debug
    for item in soup.find_all('h3'):
        print(item)

    # Now try to extract headlines as before
    for item in soup.find_all('h3', class_='gs-c-promo-heading__title'):
        text = item.get_text(strip=True)
        if text:
            headlines.append(text)

    print(f"Total <h3> tags found: {len(soup.find_all('h3'))}")
    print(f"Total headlines found: {len(headlines)}")
    return headlines

def fetch_headlines(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify()[:1000])  # Add this line to print the first 1000 characters of the HTML
    headlines = []

    for item in soup.find_all('h3', class_='gs-c-promo-heading__title'):
        text = item.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines

def write_headlines_to_file(headlines, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for headline in headlines:
            file.write(headline + '\n')


from selenium import webdriver
from bs4 import BeautifulSoup

def fetch_headlines(url):
    driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    headlines = []
    for item in soup.find_all('h3', class_='gs-c-promo-heading__title'):
        text = item.get_text(strip=True)
        if text:
            headlines.append(text)
    driver.quit()
    return headlines