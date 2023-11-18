import argparse
import enum

import httpx
from crawler import Flow
from extractor import extractors
from serializer import serializers
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


def main():
    parser = new_parser()
    args = parser.parse_args()

    # fixme: code here are dynamic and may not type-safe. we don't check type here.

    flow = (  # type: ignore
        Flow()
        .request(httpx.Request(method="GET", url=args.url))
        .extract_with(extractors[args.type])
    )

    match args.method:
        case "news":
            flow = flow.command(  # type: ignore
                lambda extractor: extractor.extract_news(), NewsListWrapper
            ).serializer(
                serializers[args.format]
            )  # type: ignore

        case _:
            raise Exception(f"Unknown method: {args.method}")

    print(flow.execute())  # type: ignore


if __name__ == "__main__":
    main()
