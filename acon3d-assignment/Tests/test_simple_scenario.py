from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.Login import Login
from Pages.Home import Home
from Pages.Search import Search
from Pages.Product import Product
import time


def test_home_good(driver, url):
    """
    홈 화면에 첫 엑세스 시, 로그인 버튼 여부 확인

    args:
      - driver: 크롬 드라이버
      - url: .env에 정의된 URL
    """
    driver.get(url)
    home_login_button = Home.home_login_button(driver)

    assert home_login_button.text == "로그인", "홈 헤더에 로그인 버튼을 찾을 수없습니다."


def test_login_good(driver, user_id, user_pw):
    """
    정상 로그인

    args:
    - driver: 크롬 드라이버
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    login_button = Home.home_login_button(driver)
    login_button.click()

    input_user_id = Login.input_user_id(driver)
    input_user_id.click()
    input_user_id.send_keys(user_id)

    input_user_pw = Login.input_user_pw(driver)
    input_user_pw.click()
    input_user_pw.send_keys(user_pw)

    user_id_save_ck = Login.user_id_save_ck(driver)
    user_id_save_ck.click()

    login_submit = Login.login_submit(driver)
    login_submit.click()

    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)
    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."


def test_search_good(driver):
    """
    크리스마스 검색

    args:
    - driver: 크롬 드라이버
    """
    search_box = Search.search_box(driver)
    search_box.click()
    search_box.send_keys("크리스마스")
    search_box.send_keys(Keys.ENTER)

    try:
        driver.find_element(By.CSS_SELECTOR, "#\\31 000005032 .sc-c1d401f7-1 img")
    except:
        assert False, "AB 프로젝트 작가님의 '크리스마스 소품모음' 을 찾을 수없습니다."


def test_product_page_good(driver):
    """
    AB 프로젝트 작가님의 '크리스마스 소품모음' 구매

    args:
    - driver: 크롬 드라이버
    """
    driver.find_element(By.CSS_SELECTOR, "#\\31 000005032 .sc-c1d401f7-1 img").click()
    driver.switch_to.window(driver.window_handles[1])

    try:
        product_buy_button = Product.product_buy_button(driver)
        product_buy_button.click()
    except:
        assert False, "사용하기(상품 구매) 버튼을 찾을 수없습니다."
    time.sleep(3)
