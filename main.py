from bs4 import BeautifulSoup
import lxml
import requests

WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "./data/100_best_movies.html"


def get_web_page():
    # Get web page
    response = requests.get(WEB_PAGE)

    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.text)


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    else:
        pass
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


def get_all_titles(soup):
    # Get all article details
    all_titles = soup.findAll(name="h3", class_="title")
    title_texts = []
    title_index = []
    index = 100
    for title in all_titles:
        text = title.getText().lstrip("0123456789) :")
        title_index.append(index)
        title_texts.append(text)
        index -= 1
    return title_index, title_texts


def sort_results(lists):
    # The list used as the sort index must be the first item in zip()
    sorted_lists = [(x, y) for (x, y) in sorted(zip(lists[0], lists[1]))]

    # print(sorted_lists)
    return sorted_lists


def save_titles(list):
    with open("./data/film_titles.txt", mode="w", encoding="utf-8") as fp:
        for item in list:
            fp.writelines(f"{item[0]})  \t{item[1]}\n")


if __name__ == "__main__":
    result = read_web_file()
    titles = get_all_titles(result)
    sorted_titles = sort_results(titles)
    print(sorted_titles)
    save_titles(sorted_titles)
