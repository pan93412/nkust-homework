import asyncio
from pathlib import Path
from typing import Awaitable, cast

import httpx
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://ic.nkust.edu.tw/")

        print("Title: ", await page.title())

        img_urls = page.locator("xpath=//figure/*/img")

        for img in await img_urls.all():
            src = await img.get_attribute("src")
            if src is None:
                continue
            print(src)


if __name__ == "__main__":
    asyncio.run(main())
