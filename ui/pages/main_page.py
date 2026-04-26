from ui.pages.base_page import BasePage
import os
from dotenv import load_dotenv


load_dotenv()
BASE_URL = os.getenv("BASE_URL")


class MainPage(BasePage):
    ENDPOINT = os.getenv("MAIN_ENDPOINT")

