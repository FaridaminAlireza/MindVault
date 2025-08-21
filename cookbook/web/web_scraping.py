import requests
from bs4 import BeautifulSoup

# Step 1: Send HTTP request
url = "http://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

# Step 2: Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract quotes
quotes = soup.find_all("div", class_="quote")

for i, quote in enumerate(quotes, start=1):
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

    print(f"{i}. {text} — {author} | Tags: {tags}")
