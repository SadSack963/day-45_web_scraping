from bs4 import BeautifulSoup
import lxml


with open("website.html", mode="r", encoding="utf-8") as fp:
    content = fp.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.prettify())

all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.detText())
#     print(tag.get("href"))


# heading = soup.findAll(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# Here we are looking for an <a> tag inside a <p> tag
# company_url = soup.select_one(selector="p a")
# print(company_url.getText(), company_url.get("href"))

# Here we are looking for one result for id="name"... use hash (#)
# name = soup.select_one(selector="#name")
# print(name)

# Here we are looking for all results for class="heading"... use dot (.)
heading = soup.select(selector=".heading")
print(heading)


















