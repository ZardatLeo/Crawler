import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://x.com/")
    page.goto("https://twitter.com/x/migrate?tok=7b2265223a222f222c2274223a313732363034373631367de314b3db3634e1ee81a4a62f0720dec5")
    page.goto("https://x.com/?mx=2")
    page.goto("https://x.com/")
    page.get_by_test_id("xMigrationBottomBar").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
