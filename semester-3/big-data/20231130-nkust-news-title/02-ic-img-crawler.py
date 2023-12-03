import asyncio
from pathlib import Path
from typing import Awaitable, cast

import httpx
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
from playwright.async_api import async_playwright


async def main():
    imgsrc = list[str]()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://ic.nkust.edu.tw/")

        print("Title: ", await page.title())

        for img in await page.query_selector_all("img"):
            src = await img.get_attribute("src")
            if src is None:
                continue
            imgsrc.append(src)

    ic_path = Path("ic")
    ic_path.mkdir(exist_ok=True)

    async with httpx.AsyncClient() as client:
        filenames = []
        responses_futures = []

        # Download them all.
        for src in tqdm(imgsrc):
            filename = src.replace("/", "__")

            filenames.append(filename)
            responses_futures.append(client.get("https://ic.nkust.edu.tw/" + src))

        responses = cast(list[httpx.Response], await tqdm_asyncio.gather(*responses_futures))

        for filename, response in zip(filenames, responses):
            if response.status_code != 200:
                print("Error: ", response.status_code, response.text)
                continue

            with open(ic_path / filename, "wb") as f:
                f.write(response.content)


if __name__ == "__main__":
    asyncio.run(main())
