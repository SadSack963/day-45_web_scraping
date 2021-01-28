from bs4 import BeautifulSoup
import lxml
import requests

WEB_PAGE = "https://news.ycombinator.com/news"
WEB_FILE = "./data/ycombinator_news.html"


def get_web_page(url, file):
    # Get web page
    response = requests.get(url)

    # Save web page to file
    with open(file, mode="w", encoding="utf-8") as fp:
        fp.write(response.text)


def read_web_file(file):
    # Read the web page from file
    with open(file, mode="r", encoding="utf-8") as fp:
        content = fp.read()

    return BeautifulSoup(content, "html.parser")


def get_first_article(soup):
    # Get first article details
    article_tag = soup.find(name="a", class_="storylink")
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_score = soup.find(class_="score")
    article_upvote = article_score.getText()

    return article_text, article_link, article_upvote


def get_all_articles(soup):
    # Get all article details
    articles = soup.findAll(name="a", class_="storylink")
    article_texts = []
    article_links = []
    for article in articles:
        article_texts.append(article.getText())
        article_links.append(article.get("href"))
    upvotes = soup.findAll(class_="score")
    article_upvotes = [int(item.getText().strip(" points")) for item in upvotes]

    # print(article_upvotes)
    return article_texts, article_links, article_upvotes


def get_most_upvoted(lists):
    index = lists[2].index(max(lists[2]))

    # print(lists[0][index])
    # print(lists[1][index])
    # print(index)
    return lists[0][index], lists[1][index], index


def sort_results(lists):
    # The list used as the sort index must be the first item in zip()
    sorted_lists = [(x, y, z) for (z, x, y) in sorted(zip(lists[2], lists[0], lists[1]), reverse=True)]

    # print(sorted_lists)
    return sorted_lists


if __name__ == "__main__":
    # get_web_page(url=WEB_PAGE, file=WEB_FILE)
    soup = read_web_file(WEB_FILE)
    # first_result = get_first_article(soup)
    all_results = get_all_articles(soup)
    # most_upvoted = get_most_upvoted(all_results)
    sorted_results = sort_results(all_results)
