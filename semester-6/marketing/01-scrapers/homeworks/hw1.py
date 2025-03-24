#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup, Tag

url = "https://www.codejudger.com/target/5203.html"

def main():
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to download the page: {response.status_code}")

    # Parse the page.
    soup = BeautifulSoup(response.content, "html.parser")

    # Find out the element with innerText: 107/9/11&nbsp;第107000077期
    title_element = soup.find(lambda tag: tag.name == "span" and tag.text == "107/9/11 第107000077期 ")
    assert title_element is not None

    # Find the parent element of the title_element, which has class: contents_box02
    contents_box02_element = title_element.find_parent(class_="contents_box02")
    assert isinstance(contents_box02_element, Tag)

    # Find the regular balls.
    balls = contents_box02_element.find_all(class_="ball_tx")
    assert len(balls) == 6+6

    # Find the special ball.
    special_ball = contents_box02_element.find(class_="ball_red")
    assert isinstance(special_ball, Tag)

    result: dict[str, list[int]] = {
        "開出順序": [],
        "大小順序": [],
        "特別號": []
    }

    # The first 6 balls are for "開出順序", the next 6 balls are for "大小順序"
    for i in range(2):
        push_to = ["開出順序", "大小順序"][i]

        for j in range(6):
            ball = balls[i*6+j]
            assert isinstance(ball, Tag)

            n = ball.text.strip()
            if n == "":
                continue

            result[push_to].append(int(n))

    # The last ball is for "特別號"
    result["特別號"].append(int(special_ball.text.strip()))

    # Format according to the requirements.
    print(f"開出順序: {'  '.join(map(str, result['開出順序']))}")
    print(f"大小順序: {'  '.join(map(str, result['大小順序']))}")
    print(f"特別號　: {result['特別號'][0]}")


if __name__ == "__main__":
    main()
