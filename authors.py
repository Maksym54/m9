import requests
from bs4 import BeautifulSoup

def get_authors(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  authors = []
  for author in soup.find_all('div', class_='author-details'):
    author_data = {
      'name': author.find('h2', class_='author-name').text,
      'birthdate': author.find('span', class_='author-born').text,
      'birthplace': author.find('span', class_='author-born-location').text,
      'occupation': author.find('span', class_='author-occupation').text
    }
    authors.append(author_data)

  return authors

authors = get_authors('http://quotes.toscrape.com/')