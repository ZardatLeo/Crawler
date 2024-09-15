import time, math
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        with open("output_zh.txt", "w", encoding="utf-8") as file:
            pass
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        month, day = 8, 1

        # 获取每天的首页链接
        for day in range(1, 32):
            link = "http://paper.people.com.cn/rmrb/html/2024-08/01/nbs.D110000renmrb_01.htm"
            if day < 10:
                link = link[:45] + "0" + str(day) + link[47:]
            else:
                link = link[:45] + str(day) + link[47:]

            # 计算每天的版块数
            await page.goto(link)
            version_content = await page.query_selector_all('div.main.w1000 div.right.right-main div.swiper-box div.swiper-container > div')
            versions = len(version_content)

            for version in range(1, versions + 1):
                if version < 10: 
                    link = link[:-5] + str(version) + link[-4:]
                else:
                    link = link[:-6] + str(version) + link[-4:]
                await page.goto(link)

                # 获取每个版块的文章数
                list_items = await page.query_selector_all('div.main.w1000 div.right.right-main div.news ul.news-list > li')
                artical_count = len(list_items)

                pre_art_link = link[:48] + "nw.D110000renmrb_202408"

                # 得到每天第一版第一篇链接
                if day < 10:
                    art_link = pre_art_link + "0" + str(day) + "_1-01.htm"
                else:
                    art_link = pre_art_link + str(day) + "_1-01.htm"

                # 进入每个版块
                for artical in range(1, artical_count + 1):
                    if version < 10: 
                        version_str = "0" + str(version)
                    else:
                        version_str = str(version)
                    art_link = art_link[:-8] + str(artical) + "-" + version_str + art_link[-4:]
                    await page.goto(art_link)

                    # 获取每篇文章的段落数
                    content_items = await page.query_selector_all('div.main.w1000 div.right.right-main div.article-box div.article #ozoom > p')
                    for idx, item in enumerate(content_items):
                        text = await item.text_content()
                        with open("output_zh.txt", "a", encoding="utf-8") as file:
                            file.write(text)

        await page.close()

asyncio.run(main()) 