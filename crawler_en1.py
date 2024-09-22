import time, math
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def goto_with_retries(page, url, retries=3, delay=5):
    for i in range(retries):
        try:
            await page.goto(url, timeout=10000)  # 每次尝试10秒超时
            return page
        except PlaywrightTimeoutError:
            time.sleep(delay)  # 等待几秒后重试
    return page

async def main():
    async with async_playwright() as p:
        with open("output_en.txt", "w", encoding="utf-8") as file:
            pass
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        home = "https://www.chinadaily.com.cn/world/"
        versions = ["asia_pacific", "america", "europe", "middle_east", "africa", "china-us", "cn_eu", "China-Japan-Relations", "china-africa"]
        len_ver = len(versions)
        for version in range(len_ver):
            pgs = 10
            for pg in range(pgs):
                page_link = "/page_" + str(pg + 1) + ".html"
                link = home + versions[version] + page_link
                await page.goto(link)
                a_tags = await page.query_selector_all("div.main_art div.lft_art div.mb10.tw3_01_2 span.tw3_01_2_t h4 a")
                tag_count = len(a_tags)
                hrefs = []
                for i in range(tag_count):
                    href = await a_tags[i].get_attribute("href")
                    href = "https:" + href
                    hrefs.append(href)

                for i in range(len(hrefs)):
                    # await page.goto(hrefs[i], timeout=60000)
                    page = await goto_with_retries(page, hrefs[i])
                    content_items = await page.query_selector_all("div.main_art div.lft_art div#Content > p")
                    for i, content_item in enumerate(content_items):
                        text = await content_item.text_content()
                        with open("output_en.txt", "a", encoding = "utf-8") as file:
                            file.write(text)

asyncio.run(main()) 