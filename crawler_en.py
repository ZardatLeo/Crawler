import time, math
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        with open("output_en.txt", "w", encoding="utf-8") as file:
            pass
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        link = "https://www.bbc.com/news"
        await page.goto(link)

asyncio.run(main()) 