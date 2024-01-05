import json
from quotes import quotes
from authors import authors

quotes_json = json.dumps(quotes, indent=4)
authors_json = json.dumps(authors, indent=4)

with open('quotes.json', 'w') as f:
  f.write(quotes_json)

with open('authors.json', 'w') as f:
  f.write(authors_json)