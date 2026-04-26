import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class BasePage:
    ENDPOINT = ""
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(f"{BASE_URL}{self.ENDPOINT}")

