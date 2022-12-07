"""
UI 테스트 실행시 필요한 웹 드라이브(크롬) 셋업
"""
from pathlib import Path

import pytest
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome import service as chrome_fs
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    load_dotenv()
    print("start loading driver...")
    DRIVER_PATH = os.getenv("DRIVER_PATH")
    assert DRIVER_PATH is not None, "driver path is not given."
    assert Path(DRIVER_PATH).exists(), "driver file does not exist."
    assert Path(DRIVER_PATH).is_absolute(), "driver path must be given as absolute path."

    browser_service = chrome_fs.Service(executable_path=DRIVER_PATH)
    options = ChromeOptions

    options = options()
    print(os.getenv("IS_HEADLESS"))

    IS_HEADLESS = bool(int(os.getenv("IS_HEADLESS")))
    if IS_HEADLESS:
        print("continue in headless mode.")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-desktop-notifications")
        options.add_argument("--disable-extensions")
    options.add_argument("--lang=ko")

    driver = webdriver.Chrome(options=options, service=browser_service)
    driver.implicitly_wait(10)

    print("finish loading driver.")

    yield driver
    print("driver closed.")
    driver.quit()


@pytest.fixture(scope="session")
def url():
    load_dotenv()
    URL = os.getenv("URL")
    assert URL is not None, "base url is not given."
    yield URL


@pytest.fixture(scope="session")
def user_id():
    load_dotenv()
    USER_ID = os.getenv("USER_ID")
    assert USER_ID is not None, "base user_id is not given."
    yield USER_ID


@pytest.fixture(scope="session")
def user_pw():
    load_dotenv()
    USER_PW = os.getenv("USER_PW")
    assert USER_PW is not None, "base user_pw is not given."
    yield USER_PW
