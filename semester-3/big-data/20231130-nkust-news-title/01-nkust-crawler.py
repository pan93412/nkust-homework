import asyncio
from typing import Awaitable

from playwright.async_api import async_playwright, Browser, Page


async def open_page_for(browser: Browser, url: str) -> Page:
    page = await browser.new_page()
    await page.goto(url)

    return page


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw")

        print("Title: ", await page.title())

        page_queue = list[Awaitable[Page]]()

        for mtitle in await page.query_selector_all(".mtitle > a"):
            print("\tNews: ", await mtitle.inner_text())
            href = await mtitle.get_attribute("href")

            if href is not None:
                page_queue.append(open_page_for(browser, href))

        pages = await asyncio.gather(*page_queue)
        for page in pages:
            print("\t\tTitle: ", await page.title())


if __name__ == '__main__':
    asyncio.run(main())
