import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")
driver.implicitly_wait(5)

original_window = driver.current_window_handle

# select the search bar with aria-label '搜尋'
search_bar_el = driver.find_element(By.CSS_SELECTOR, "textarea[aria-label='搜尋']")
search_bar_el.send_keys("Selenium")
search_bar_el.submit()

# open new tabs for every result
result_els = driver.find_elements(By.CSS_SELECTOR, "[jsname=UWckNb]")
random.shuffle(result_els)  # prevent being detected
result_tabs = []
for result_el in result_els:
    result_title = result_el.find_element(By.CSS_SELECTOR, "h3").text
    print("RESULT", result_title)

    # open new tab
    result_url = result_el.get_attribute("href")
    driver.switch_to.new_window(result_title)
    driver.get(result_url)
    result_tabs.append(driver.current_window_handle)
    driver.switch_to.window(original_window)
