from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Login import Login
from Pages.Home import Home
from Pages.Search import Search
from Pages.Product import Product
import time


def test_search_input_xss01(driver, url):
    """
    검색창에 "<SCRIPT>alert("테스트!!!");</SCRIPT>" 검색

    args:
      - driver: 크롬 드라이버
      - url: .env에 정의된 URL
    """
    driver.get(url)
    search_box = Search.search_box(driver)
    search_box.click()
    search_box.send_keys('<SCRIPT>alert("테스트!!!");</SCRIPT>')
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    not_search_keyword = Search.not_search_keyword(driver)
    assert not_search_keyword.text == '‘<SCRIPT>alert("테스트!!!");</SCRIPT>’에 대한 검색 결과가 없습니다. 철자와 띄어쓰기를 확인해 ' \
                                      '보세요.\n카테고리에서 상품을 쉽게 찾을 수 있어요.', "에러 발생"