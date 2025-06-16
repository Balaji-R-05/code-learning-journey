from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/news.ycombinator.com/"

response = requests.get(url)
yc_response = response.text

soup = BeautifulSoup(yc_response, 'html.parser')

# Find all article tags, text and links in it
article_tags = soup.find_all(name="a", class_="storylink")
article_text = [tag.getText() for tag in article_tags]
article_links = [tag.get("href") for tag in article_tags]

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_text)
# print(article_links)
# print(article_score)

max_score = max(article_score)
max_index = article_score.index(max_score)

print(article_text[max_index])
print(article_links[max_index])
print(article_score[max_index])
