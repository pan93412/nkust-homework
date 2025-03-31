#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
使用 Claude 寫出一個 PTT 文章爬蟲。

Some fixes have been made to the code.

Prompt
======

You are a professional Python crawl engineer. Your task is to crawl the
iPhone 16 related articles on PTT (Taiwan), which usually are in the board
MobileComm. You should extract the article title, content, author and link
in the article. You should write it in Artifacts.
'''

import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import logging
import argparse
from datetime import datetime
from urllib.parse import urljoin

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("ptt_crawler.log"), logging.StreamHandler()]
)
logger = logging.getLogger('ptt_crawler')

class PTTCrawler:
    def __init__(self, board='MobileComm', max_pages=5, delay=1):
        """
        Initialize the PTT crawler
        
        Args:
            board (str): PTT board name to crawl
            max_pages (int): Maximum number of pages to crawl
            delay (int): Delay between requests in seconds
        """
        self.base_url = 'https://www.ptt.cc'
        self.board = board
        self.max_pages = max_pages
        self.delay = delay
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        
        # Pass over 18 verification
        self.session.cookies.set('over18', '1')
        
        # Initialize data structures
        self.articles = []
    
    def _get_page_url(self, page=None):
        """Get the URL for a specific page of the board"""
        if page:
            return f'{self.base_url}/bbs/{self.board}/index{page}.html'
        else:
            return f'{self.base_url}/bbs/{self.board}/index.html'
    
    def _get_soup(self, url):
        """Get BeautifulSoup object from a URL"""
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def _get_previous_page(self, soup):
        """Get the previous page URL from pagination links"""
        prev_btn = soup.select('div.btn-group-paging a.btn.wide:-soup-contains("上頁")')
        if prev_btn:
            prev_url = prev_btn[0]['href']
            return prev_url
        return None
    
    def _extract_article_meta(self, div):
        """Extract article metadata from a div element"""
        try:
            # Get article URL and title
            title_element = div.select_one('div.title a')
            if not title_element:
                return None
                
            title = title_element.text.strip()

            url = urljoin(self.base_url, title_element['href'])
            
            # Get author and date
            author = div.select_one('div.meta div.author').text.strip()
            date = div.select_one('div.meta div.date').text.strip()

            return {
                'title': title,
                'url': url,
                'author': author,
                'date': date
            }
        except Exception as e:
            logger.error(f"Error extracting article meta: {e}")
            return None
    
    def _extract_article_content(self, url):
        """Extract the content of an article"""
        try:
            soup = self._get_soup(url)
            if not soup:
                return "Content extraction failed"
            
            # Get main content
            main_content = soup.select_one('div#main-content')
            if not main_content:
                return "Content extraction failed"
            
            # Remove unnecessary elements
            for element in main_content.select('div.article-metaline, div.article-metaline-right, div.push'):
                element.decompose()
            
            # Clean the content
            content = main_content.text.strip()
            
            # Remove signature
            if '--' in content:
                content = content.split('--')[0]
            
            return content.strip()
        except Exception as e:
            logger.error(f"Error extracting article content from {url}: {e}")
            return "Content extraction failed"
    
    def crawl(self, keyword: str):
        """
        Crawl the PTT board for iPhone 16 related articles
        
        Args:
            keyword (str): Keyword to filter articles
        
        Returns:
            list: List of dictionaries containing article information
        """
        logger.info(f"Starting to crawl {self.board} board for '{keyword}' related articles")
        
        page_url = self._get_page_url()
        pages_crawled = 0
        
        while page_url and pages_crawled < self.max_pages:
            full_url = urljoin(self.base_url, page_url)
            logger.info(f"Crawling page: {full_url}")
            
            soup = self._get_soup(full_url)
            if not soup:
                break
            
            # Get all article divs
            article_divs = soup.select('div.r-ent')
            
            for div in article_divs:
                article_meta = self._extract_article_meta(div)
                if article_meta:
                    # Check if the article title contains the keyword
                    if keyword.lower() in article_meta['title'].lower():
                        logger.info(f"Found related article: {article_meta['title']}")
                        
                        # Extract article content
                        article_meta['content'] = self._extract_article_content(article_meta['url'])
                        
                        # Add to list
                        self.articles.append(article_meta)
            
            # Get previous page URL for next iteration
            page_url = self._get_previous_page(soup)
            pages_crawled += 1
            
            # Sleep to avoid hitting the server too hard
            time.sleep(self.delay)
        
        logger.info(f"Crawling complete. Found {len(self.articles)} articles related to '{keyword}'")
        return self.articles
    
    def save_to_csv(self, filename='iphone16_articles.csv'):
        """Save the articles to a CSV file"""
        if not self.articles:
            logger.warning("No articles to save")
            return
        
        df = pd.DataFrame(self.articles)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        logger.info(f"Saved {len(self.articles)} articles to {filename}")
    
    def save_to_json(self, filename='iphone16_articles.json'):
        """Save the articles to a JSON file"""
        if not self.articles:
            logger.warning("No articles to save")
            return
        
        df = pd.DataFrame(self.articles)
        df.to_json(filename, orient='records', force_ascii=False, indent=4)
        logger.info(f"Saved {len(self.articles)} articles to {filename}")


def main():
    parser = argparse.ArgumentParser(description='Crawl PTT for articles')
    parser.add_argument('--board', type=str, default='MobileComm', help='PTT board name')
    parser.add_argument('--keyword', type=str, default='iphone', help='Keyword to filter articles')
    parser.add_argument('--max_pages', type=int, default=3, help='Maximum number of pages to crawl')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between requests in seconds')
    parser.add_argument('--output', type=str, default='output/iphone16_articles', help='Output filename without extension')
    parser.add_argument('--format', type=str, choices=['csv', 'json', 'both'], default='both', help='Output format')
    
    args = parser.parse_args()
    
    # Create a timestamp for unique filenames
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Initialize crawler
    crawler = PTTCrawler(
        board=args.board,
        max_pages=args.max_pages,
        delay=args.delay
    )
    
    # Run crawler
    articles = crawler.crawl(keyword=args.keyword)
    print(articles)

    # Save results
    if args.format == 'csv' or args.format == 'both':
        csv_filename = f"{args.output}_{timestamp}.csv"
        crawler.save_to_csv(csv_filename)
    
    if args.format == 'json' or args.format == 'both':
        json_filename = f"{args.output}_{timestamp}.json"
        crawler.save_to_json(json_filename)


if __name__ == "__main__":
    main()