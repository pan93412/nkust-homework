import argparse
import logging
import time

import loguru
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

parser = argparse.ArgumentParser()
parser.add_argument("--headless", action="store_true")
parser.add_argument("--wait", type=int, default=5)
args = parser.parse_args()

options = Options()
logger.debug("init: setting eager mode")
options.page_load_strategy = 'eager'

# background
if args.headless:
    logger.info("arg: headless mode enabled")
    options.add_argument('--headless')

logger.debug("init: setting webdriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
logger.debug("init: setting implicit wait to 5 seconds")
driver.implicitly_wait(5)

logger.debug("op: open page")
driver.get("https://ic.nkust.edu.tw")

logger.info("info: name: {}", driver.name)
logger.info("info: title: {}", driver.title)
logger.info("info: current_url: {}", driver.current_url)
logger.info("info: session_id: {}", driver.session_id)
logger.info("info: capabilities: {}", driver.capabilities)
logger.info("info: src: {}", driver.page_source.replace('\n', '')[:400])

logger.debug("op: move window to (10, 10)")
driver.set_window_position(10, 10)

logger.debug("op: resize window to 500x500")
driver.set_window_size(500, 500)

logger.debug("op: wait for {} seconds", args.wait)
time.sleep(args.wait)

logging.debug("op: bye!")
driver.quit()
