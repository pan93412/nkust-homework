import argparse
from typing import Callable

import httpx
from crawler import Flow
from extractor import extractors
from extractor.extractor import Extractor
from serializer import serializers
from structures.news import NewsList
from wrapper.news_list import NewsListWrapper


def new_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", type=str, choices=["news"], default="news")
    parser.add_argument(
        "--format",
        type=str,
        choices=[key for key in serializers.keys()],
        default="json",
    )
    parser.add_argument("type", type=str, choices=[key for key in extractors.keys()])
    parser.add_argument("url", type=str)

    return parser


def visualize_news_list(news_list: NewsList) -> None:
    for news in news_list:
        print(f"\x1b[1m#{news.seq} | \x1b[33m{news.title}\x1b[0m")
        print(f"{news.date}")
        print("\n".join(map(lambda line: "\t" + line, news.content.split("\n"))))
        print("\n\n")


def main():
    parser = new_parser()
    args = parser.parse_args()

    request = httpx.Request(method="GET", url=args.url)
    extractor = extractors[args.type]
    serializer = serializers[args.format]

    match args.method:
        case "news":
            method: Callable[
                [Extractor], NewsList
            ] = lambda extractor: extractor.extract_news()

            flow = (
                # todo: dynamic type
                Flow[NewsList, str]()
                .request(request)
                .extract_with(extractor)
                .command(method, NewsListWrapper)
                .display(visualize_news_list)
                .serializer(serializer)
            )

        case _:
            raise Exception(f"Unknown method: {args.method}")

    with open("output." + serializers[args.format].extension(), "w") as f:
        result = flow.execute()
        f.write(result)


if __name__ == "__main__":
    main()
