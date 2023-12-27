import asyncio
import aiofiles
from pathlib import Path
import re
from loguru import logger
from selectolax.parser import HTMLParser

import httpx

list_page = "https://www.taifex.com.tw/cht/3/dlOptPrevious30DaysSalesData"
list_table_selector = "#printhere > table:nth-child(4)"
csv_download_selector = 'input[title="前30個交易日選擇權每筆成交資料csv格式(zip檔)"]'
link_extractor = re.compile(r"javascript:window.open\('(.+)'\)")

download_folder = Path("downloads")


async def download_and_save(url: str, filepath: Path) -> None:
    async with httpx.AsyncClient() as client:
        logger.debug("正在下載：{}", url)
        response = await client.get(url)

    async with aiofiles.open(filepath, "wb") as f:
        logger.info("正在寫入：{}", filepath)
        await f.write(response.content)


async def main() -> None:
    # 拉回清單頁面
    async with httpx.AsyncClient() as client:
        logger.info("正在取回清單頁面……")
        response = await client.get(list_page)
        content = response.text

    # 取回清單頁面的表格
    logger.info("正在解析表格……")
    parser = HTMLParser(content)
    table = parser.css_first(list_table_selector)
    assert table is not None, "找不到表格。"

    # 取得每一個表格列的連結
    download_buttons = table.css(csv_download_selector)
    download_urls = list[str]() * len(download_buttons)
    for download_button in download_buttons:
        raw_link_onclick = download_button.attributes["onclick"]
        if not raw_link_onclick:
            logger.debug("發現不需要的按鈕：{}", download_button.html)
            continue

        matched_result = link_extractor.search(raw_link_onclick)
        if not matched_result:
            logger.debug("發現不是下載連結的 onclick 屬性：{}", download_button.html)
            continue

        url = matched_result.group(1)
        logger.debug(f"找到連結：{url}")

        download_urls.append(url)

    # 掃描檔案：檢查是否已經下載過（亦即 zip 檔案是否已經存在），
    # 如果已經下載過就略過，否則下載並存檔。
    logger.info("正在檢查下載清單……")
    download_folder.mkdir(exist_ok=True)

    async with asyncio.TaskGroup() as task_group:
        for url in download_urls:
            # 取得檔案名稱
            filename = url.split("/")[-1]
            filepath = download_folder / filename

            # 檢查是否已經下載過
            if filepath.exists():
                logger.debug("檔案已經存在：{}", filename)
                continue

            # 建立下載任務
            task_group.create_task(download_and_save(url, filepath))

    logger.info("下載完成。")


if __name__ == '__main__':
    asyncio.run(main())
