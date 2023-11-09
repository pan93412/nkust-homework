import asyncio
from typing import cast

import httpx
from httpx_socks import AsyncProxyTransport
from tqdm.asyncio import tqdm_asyncio

import argparse


class TypedNamespace(argparse.Namespace):
    proxy: str | None
    url: str
    count: int


def get_args() -> TypedNamespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proxy", help="proxy url")
    parser.add_argument("url", help="url to download")
    parser.add_argument("--count", help="number of times to download", type=int, default=10)
    return cast(TypedNamespace, parser.parse_args())


async def main_request(url: str, count: int, proxy: str | None) -> None:
    client_args = {}

    if proxy is not None:
        if proxy.startswith("socks"):
            transport = AsyncProxyTransport.from_url(proxy)
            client_args["transport"] = transport
        else:
            client_args["proxies"] = proxy

    async with httpx.AsyncClient(**client_args) as client:
        with tqdm_asyncio(total=count, desc="Downloading") as progress:
            download_tasks = (
                client.get(url, headers={
                    "User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
                })
                for _ in range(count)
            )
            await progress.gather(*download_tasks)


async def main():
    args = get_args()
    await main_request(args.url, args.count, args.proxy)


if __name__ == "__main__":
    asyncio.run(main())
