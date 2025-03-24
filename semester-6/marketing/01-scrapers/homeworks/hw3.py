#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # 設定 Chrome 瀏覽器選項
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')  # 無頭模式，不會開啟瀏覽器視窗
    
    with webdriver.Chrome(options=chrome_options) as driver:
        print("[*] 取回「豆瓣电影」手機版頁面首頁")
        driver.get("https://m.douban.com/movie/")
        
        # 等待 "影院热映" 準備完成
        print("[*] 等待「影院热映」準備完成")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "section.subject_unino div.W7erk"))
        )

        # 拉取所有「影院热映」的電影
        print("[*] 拉取所有「影院热映」的電影")
        movies = driver.find_elements(By.CSS_SELECTOR, "section.subject_unino div.W7erk")
        for i, movie in enumerate(movies):
            print(f"    [{i+1}] {movie.text}")


if __name__ == "__main__":
    main()
