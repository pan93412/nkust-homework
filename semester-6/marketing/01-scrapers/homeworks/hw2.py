#!/usr/bin/env python3

import pandas as pd
from bs4 import BeautifulSoup, Tag

def main():
    # Read the HTML file.
    with open("read.html", "r") as f:
        html = f.read()

    # Parse the page.
    soup = BeautifulSoup(html, "html.parser")

    # Find out the 'table.DataTable2' element.
    table = soup.find("table", class_="DataTable2")
    assert isinstance(table, Tag)

    # Find out the 'tr' elements.
    trs = table.find_all("tr")

    # Assert the first 'tr' element has 2 'th' elements.
    first_tr = trs[0]
    assert isinstance(first_tr, Tag)
    ths = first_tr.find_all("th")
    assert len(ths) == 2
    assert ths[0].text.strip() == "日 期"
    assert ths[1].text.strip() == "NTD/USD"

    result = {
        "日 期": [],
        "NTD/USD": []
    }

    # Assert the second 'tr' element has 2 'td' elements.
    for i in trs[1:]:
        assert isinstance(i, Tag)
        tds = i.find_all("td")
        assert len(tds) == 2

        result["日 期"].append(tds[0].text.strip())
        result["NTD/USD"].append(float(tds[1].text.strip()))

    # Turn it to a dataframe and output as a CSV file.
    df = pd.DataFrame(result)
    df.to_csv("result.csv", index=False)


if __name__ == "__main__":
    main()
