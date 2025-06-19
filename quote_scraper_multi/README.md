# Quote Scraper (All Pages)

This Python script scrapes **all quotes** from [quotes.toscrape.com](http://quotes.toscrape.com) by following pagination links.

Features:
- Extracts quote text and author
- Walks through all pages (`/page/1`, `/page/2`, etc.)
- Saves data to a CSV file

Tools used:
- Python 3
- requests
- BeautifulSoup
- pandas

Output:
- `all_quotes.csv` — clean CSV file with all quotes

How it works:
The script uses a `while` loop to check for a “Next” button and continues scraping until there are no more pages.

