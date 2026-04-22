from playwright.sync_api import sync_playwright

def run_wordle_test():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless = False)
        page = browser.new_page()
        print("Navigaiting to Wordle")
        page.goto("https://www.nytimes.com/games/wordle/index.html")
        playbutton = page.get_by_role("button", name = "Play")
        if page.get_by_role("button", name="OK").is_visible():
            page.get_by_role("button", name="OK").click()
        playbutton.wait_for(state = "visible")
        playbutton.click()
        page.locator('[data-testid="icon-close"]').click()
        word_data = page.evaluate() 
        input("press enter to close page")

if __name__ == "__main__":
    run_wordle_test()