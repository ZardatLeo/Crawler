import time, math
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

async def goto_with_retries(page, url, retries=5, delay=5):
    for i in range(retries):
        try:
            await page.goto(url, timeout=10000)  # 每次尝试10秒超时
            return page
        except PlaywrightTimeoutError:
            time.sleep(delay)  # 等待几秒后重试
            print(page, url)
    return page

async def main():
    async with async_playwright() as p:
        with open("output_en_2.txt", "w", encoding="utf-8") as file:
            pass
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        homes = "https://www.chinadaily.com.cn/"
        topics = {
            "business":["/economy", "/companies", "/biz_industries", "/tech", "/motoring", "/money"],
            'life':["/fashion", "/celebrity", "/people", "/health", "/video", "/photo"],
            'culture':["/art", "/musicandtheater", "/filmandtv", "/books", '/heritage', '/eventandfestival', '/culturalexchange']
        }
        for k in range(1, 3):            
            # business = ["economy", "companies", "biz_industries", "tech", "motoring", "cmoney"]
            # life = ["fashion", "celebrity", "people", "health", "video", "photo"]
            # culture = ["art", "musicandtheater", "filmandtv", "books", 'heritage', 'eventandfestival', 'culturalexchange']
            # 选择主题
            home = homes
            if k == 0:
                topic = topics["business"]
                home += 'business'
            elif k == 1:
                topic = topics["life"]
                home += 'life'
            else:
                topic = topics["culture"]
                home += 'culture'

            page = await goto_with_retries(page, home)
            len_ver = len(topic)

            # 选择板块
            for version in range(len_ver):
                currhome = home + topic[version]
                page = await goto_with_retries(page, currhome)
                currpage = await page.query_selector_all('div.main_art div.lft_art div#div_currpage a')
                pgs = len(currpage) - 1
                # 选择页码
                for pg in range(pgs):
                    page_link = "/page_" + str(pg + 1) + ".html"
                    link = currhome + page_link
                    page = await goto_with_retries(page, link)
                    a_tags = await page.query_selector_all("div.main_art div.lft_art div.mb10.tw3_01_2 span.tw3_01_2_t h4 a")
                    tag_count = len(a_tags)
                    hrefs = []  
                    for i in range(tag_count):
                        href = await a_tags[i].get_attribute("href")
                        href = "https:" + href
                        hrefs.append(href)

                    # 选择文章
                    for i in range(len(hrefs)):
                        # await page.goto(hrefs[i], timeout=60000)
                        page = await goto_with_retries(page, hrefs[i])
                        content_items = await page.query_selector_all("div.main_art div.lft_art div#Content > p")
                        for i, content_item in enumerate(content_items):
                            text = await content_item.text_content()
                            with open("output_en_2.txt", "a", encoding = "utf-8") as file:
                                file.write(text)

asyncio.run(main())