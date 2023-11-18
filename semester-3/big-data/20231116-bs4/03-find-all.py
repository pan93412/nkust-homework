import bs4
import requests

with open("page.html") as f:
    soup = bs4.BeautifulSoup(f, "lxml")

    lists = soup.find_all("li")
    print(lists)
