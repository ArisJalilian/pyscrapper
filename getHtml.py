from playwright.sync_api import sync_playwright

def getHtml(url:str):

    ua = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/69.0.3497.100 Safari/537.36"
    )
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page(user_agent=ua)
        page.goto(url)
        page.wait_for_timeout(1000)

        html = page.content()

    return html