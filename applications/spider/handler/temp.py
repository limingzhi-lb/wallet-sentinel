from playwright.sync_api import sync_playwright
from pathlib import Path
from urllib.parse import urlparse, urlunparse
import time

"""
https://playwright.dev/python/docs/api/class-route
"""
def custom_headers(url) -> dict:
    res = urlparse(url)
    loc = res.netloc
    host = urlunparse([res.scheme, res.netloc, '', '', '', ''])
    page_url = urlunparse([res.scheme, res.netloc, res.path, '', '', ''])
    return {
        'authority': loc,
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': host,
        'referer': host,
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-referer-page': page_url,
        'x-rp-client': 'h5_1.0.0',
    }


with sync_playwright() as p:
    url = 'https://item.jd.com/7836786.html#crumb-wrap'
    extra_http_headers = custom_headers(url)
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(extra_http_headers=extra_http_headers)
    page = context.new_page()
    page.goto(url)
    print(context.storage_state())
    time.sleep(5)
    page.screenshot(path='example1.png')
    browser.close()
