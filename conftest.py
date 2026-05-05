pytest_plugins = [
    "ui.fixtures.page_fixtures",
    "ui.fixtures.make_browser_fixtures",
    "ui.fixtures.user_fixtures"

]

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)