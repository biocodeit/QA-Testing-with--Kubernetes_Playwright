import re
from playwright.sync_api import Page, expect

class loginPage:
    def __init__(self, page:Page) -> None:
        self.username_add = page.get_by_role("textbox", name="Username")
        self.password_add = page.get_by_role("textbox", name="Password")
        self.login = page.get_by_role("button", name="Login")
        self.page=page

    def add_username(self, username:str):
        self.username_add.fill(username)

    def add_password(self, password: str):
        self.password_add.fill(password)

    def loginSetup(self, username:str, password:str):
        self.add_username(username)
        self.add_password(password)
        self.page.wait_for_timeout(100)
        self.login.click()


        
