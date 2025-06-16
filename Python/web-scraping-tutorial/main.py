from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())
# print(soup.a)

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))

heading_id = soup.find(name="h1", id="name")  # using id
heading_class = soup.find(name="h3", class_="heading") # using class
company_url = soup.select_one(selector="p a")

print(company_url)
print(heading_class)

# print(soup.title.string)