import requests
from bs4 import BeautifulSoup

def get_quotes(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  quotes = []
  for quote in soup.find_all('div', class_='quote'):
    quote_data = {
      'text': quote.find('span', class_='text').text,
      'author': quote.find('small', class_='author').text,
      'tags': [tag.text for tag in quote.find_all('a', class_='tag')]
    }
    quotes.append(quote_data)

  return quotes

quotes = get_quotes('http://quotes.toscrape.com/')