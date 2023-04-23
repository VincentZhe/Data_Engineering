from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
anchot_tags = soup.find_all(name="span", class_="titleline")


# print(anchot_tags)
anchot_texts = []
anchot_links = []
for tag in anchot_tags:
    text = tag.getText()
    anchot_texts.append(text)
    link = tag.find(name="a").get("href")
    anchot_links.append(link)

anchot_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_number = max(anchot_upvote)
highest_index = anchot_upvote.index(highest_number)



print(anchot_texts[highest_index])
print(anchot_links[highest_index])
print(anchot_upvote)