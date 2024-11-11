import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

# Set up headers with a list of User-Agents to avoid bot detection
headers = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"},
    # Add more User-Agent strings to improve bot evasion
]

# Amazon book product page
url = "https://www.amazon.com/gp/browse.html?node=283155"

# Storage list for data
data = []

# Function to fetch page content
def fetch_page(url):
    response = requests.get(url, headers=random.choice(headers))
    if response.status_code == 200:
        return response.text
    else:
        print("Failed request, status code:", response.status_code)
        return None

# Function to parse review information
def parse_review(soup):
    reviews = soup.find_all("div", {"data-hook": "review"})
    for review in reviews:
        review_id = review.get("id")
        title = soup.find("a", {"data-hook": "product-link"}).text.strip()
        price = soup.find("span", {"class": "a-price-whole"}).text.strip() if soup.find("span", {
            "class": "a-price-whole"}) else "N/A"
        user_id = review.find("a", {"data-hook": "review-author"}).get("href").split('/')[3]
        profile_name = review.find("span", {"class": "a-profile-name"}).text
        helpfulness = review.find("span", {"data-hook": "helpful-vote-statement"}).text if review.find("span", {
            "data-hook": "helpful-vote-statement"}) else "0"
        score = review.find("i", {"data-hook": "review-star-rating"}).text.split()[0]
        time = review.find("span", {"data-hook": "review-date"}).text
        summary = review.find("a", {"data-hook": "review-title"}).text.strip()
        text = review.find("span", {"data-hook": "review-body"}).text.strip()

        data.append({
            "Id": review_id,
            "Title": title,
            "Price": price,
            "User_id": user_id,
            "profileName": profile_name,
            "review/helpfulness": helpfulness,
            "review/score": score,
            "review/time": time,
            "review/summary": summary,
            "review/text": text,
        })

# Main scraping loop
for page in range(1, 10):  # change pages
    print(f"Scraping page {page}")
    page_url = f"{url}&pageNumber={page}"
    html_content = fetch_page(page_url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        parse_review(soup)
        time.sleep(random.uniform(1.5, 3.5))  # Random delay between requests
    else:
        print("Skipping page due to failed fetch")

# Save data to CSV
df = pd.DataFrame(data)
df.to_csv("Books_rating.csv", index=False, encoding="utf-8")
print("Data saved to Books_rating.csv")
