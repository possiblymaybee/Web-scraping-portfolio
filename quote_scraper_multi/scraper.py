import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://quotes.toscrape.com"
url = "/page/1/"
all_quotes = []

while url:
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        all_quotes.append({"quote": text, "author": author})

    # Находим ссылку на следующую страницу
    next_button = soup.find("li", class_="next")
    if next_button:
        url = next_button.a["href"]  # например: /page/2/
    else:
        url = None  # прекращаем цикл

# Сохраняем в CSV
df = pd.DataFrame(all_quotes)
df.to_csv("all_quotes.csv", index=False)
print("Saved", len(df), "quotes.")
