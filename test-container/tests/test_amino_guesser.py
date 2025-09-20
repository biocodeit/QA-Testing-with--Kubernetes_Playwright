import re
from playwright.sync_api import Page, expect



def test_example(page: Page) -> None:
    page.goto("http://localhost:8080/")
    expect(page.get_by_role("heading")).to_contain_text("Amino Acid Guesser")
    expect(page.locator("#opt_h1")).to_contain_text("Name")
    expect(page.locator("#opt_h2")).to_contain_text("3‑code")
    expect(page.locator("#opt_h3")).to_contain_text("1‑code")
    page.get_by_text("Name").click()
    page.get_by_role("button", name="next").get_attribute()
