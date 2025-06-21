Hacker News Top 30 Scraper

Scrapes the front page of [Hacker News](https://news.ycombinator.com)  
Collects the top 30 stories and saves them into a clean CSV.

Extracted fields:
- `rank`: story position (1–30)
- `title`: article title
- `link`: URL to article
- `score`: number of upvotes
- `author`: username of poster
- `comments`: number of comments

Tech Stack:
- Python 3
- `requests` for HTTP
- `BeautifulSoup` for HTML parsing
- `pandas` for CSV export

Output sample:

| rank | title                 | score | author  | comments |
|------|-----------------------|-------|---------|----------|
| 1    | Build your own AI IDE | 210   | dev123  | 88       |
| 2    | Fast Python Libraries | 187   | codex42 | 51       |

CSV filename: `hn_top30.csv`

Run it:
```bash
python hn_scraper.py
