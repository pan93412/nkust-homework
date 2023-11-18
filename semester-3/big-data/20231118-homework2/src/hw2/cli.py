import argparse
import enum

import httpx

from executor import Executor
from extractor import extractors


class ExecuteMethod(enum.Enum):
    news = "news"


def new_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("type", type=str, choices=[key for key in extractors.keys()])
    parser.add_argument(
        "--method", type=str, choices=list(ExecuteMethod), default=ExecuteMethod.news
    )
    parser.add_argument("url", type=str)

    return parser


def main():
    parser = new_parser()
    args = parser.parse_args()

    executor = Executor(extractors[args.type])
    request = httpx.Request(method="GET", url=args.url)

    match args.method:
        case ExecuteMethod.news:
            result = executor.execute(
                request, lambda extractor: extractor.extract_news()
            )
            print(result)
        case _:
            raise Exception(f"Unknown method: {args.method}")


if __name__ == "__main__":
    main()
