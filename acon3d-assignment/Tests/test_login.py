import time

from Pages.Login import Login
from Pages.Home import Home
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login_ck(driver):
    """
    로그인 클릭, 로그인 되어 있을시 로그아웃

    args:
    - driver: 크롬 드라이버
    """

    try:
        driver.implicitly_wait(10)
        login_button = Home.home_login_button(driver)
        login_button.click()
    except:
        home_user_info_icon = Home.home_user_info_icon(driver)
        home_user_info_icon.click()
        home_logout_button = Home.home_logout_button(driver)
        home_logout_button.click()


def login_validation(driver, user_id, user_pw):
    """
    로그인

    args:
    - driver: 크롬 드라이버
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로 그인 패스워드
    """
    driver.implicitly_wait(10)

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


def test_access_user_join_page(driver, url):
    """
    홈 > 로그인 > 회원가입

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    """
    driver.get(url)
    assert driver.title == "에이콘3D - 3D모델과 함께 창작이 재밌고 쉬워지는 곳", "타이틀이 올바르지 않거나 찾을 수 없습니다."

    login_ck(driver)
    login_user_join_button = Login.login_user_join_button(driver)
    login_user_join_button.click()
    user_join_page = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/form/div[1]/div[1]')
    assert user_join_page.text == "회원 정보 입력", "회원가입 페이지를 찾을 수 없습니다."


def test_login_enter(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 아이디,패스워드 입력 후 엔터

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로 그인 패스워드
    """
    driver.get(url)

    login_ck(driver)

    user_id_save_ck = Login.user_id_save_ck(driver)
    user_id_save_ck.click()

    input_user_id = Login.input_user_id(driver)
    input_user_id.click()
    input_user_id.send_keys(user_id)

    input_user_pw = Login.input_user_pw(driver)
    input_user_pw.click()
    input_user_pw.send_keys(user_pw)
    input_user_pw.send_keys(Keys.ENTER)

    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)

    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."

    login_ck(driver)


def test_login_validation_check01(driver, url, user_id):
    """
    홈 > 로그인 > 패스워드 미입력

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    """
    driver.get(url)
    login_ck(driver)
    login_validation(driver, user_id, "")
    login_err_text = Login.login_err_text(driver)
    driver.implicitly_wait(10)
    assert login_err_text.text == "비밀번호를 입력해주세요."


def test_login_validation_check02(driver, url, user_pw):
    """
    홈 > 로그인 > 아이디 미입력

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_pw: .env에 정의된 로 그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    login_validation(driver, "", user_pw)
    login_err_text_id = Login.login_err_text_id(driver)
    driver.implicitly_wait(10)
    assert login_err_text_id.text == "아이디를 입력해주세요."


def test_login_validation_check03(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 아이디에 중간에 공백 추가

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    user_id_split = user_id.split('@')
    user_id_err = " @".join(user_id_split)
    login_validation(driver, user_id_err, user_pw)
    login_err_text = Login.login_err_text(driver)
    assert login_err_text.text == "입력된 아이디은(는) 잘못된 형식입니다."


def test_login_validation_check04(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 아이디에 앞에 공백 추가

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    login_validation(driver, " " + user_id, user_pw)
    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)
    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."

    login_ck(driver)


def test_login_validation_check05(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 아이디에 뒤에 공백 추가

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    login_validation(driver, user_id + " ", user_pw)
    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)
    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."

    login_ck(driver)


def test_login_validation_check06(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 패스워드 뒤에 공백 추가

    args:
    - driver: 크롬 드라이브
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    login_validation(driver, user_id, user_pw + " ")
    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)
    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."

    login_ck(driver)


def test_login_validation_check07(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 패스워드 잘못입력

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    login_validation(driver, user_id, user_pw + "err")
    login_err_text = Login.login_err_text(driver)
    assert login_err_text.text == "아이디 또는 비밀번호를 다시한번 확인해 주시기 바랍니다."


def test_login_validation_check08(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 아이디에 포함된 숫자 1바이트->2바이트 입력

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    user_id_split = user_id.split('9066')
    user_id_err = "９０６６".join(user_id_split)
    login_validation(driver, user_id_err, user_pw)
    login_err_text = Login.login_err_text(driver)
    assert login_err_text.text == "입력된 아이디은(는) 잘못된 형식입니다.", "올바른 에러 메세지가 표시되지 않습니다."


def test_login_validation_check09(driver, url, user_id, user_pw):
    """
    홈 > 로그인 > 아이디에 이메일(@gmail.com)빼고 입력

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    user_id_split = user_id.split('@')
    login_validation(driver, user_id_split[0], user_pw)
    login_err_text = Login.login_err_text(driver)
    assert login_err_text.text == "회원정보를 찾을 수 없습니다."


def test_login_validation_check10(driver, url, user_id, user_pw):
    """
    홈> 로그인> 로그인 패스워드 잘못입력(7회)

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)

    # 전체 테스트의 경우, 실패 횟수를 정확히 카운트 하기 위해 한번 로그인 하여 횟수 초기화
    login_validation(driver, user_id, user_pw)
    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)
    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."

    login_ck(driver)

    login_ck(driver)
    login_validation(driver, user_id, user_pw + "!!")
    for _ in range(6):
        time.sleep(3)
        login_submit = Login.login_submit(driver)
        login_submit.click()

    login_err_text = Login.login_err_text(driver)
    assert login_err_text.text == "로그인을 7회 실패하셨습니다. 10회 이상 실패 시 접속이 제한됩니다.", "에러 문구내용이 다릅니다."


def test_login_validation_check11(driver, url, user_id, user_pw):
    """
    홈> 로그인> 10회 이상 로그인실패

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)

    login_validation(driver, user_id, user_pw + "!!")
    for _ in range(11):
        time.sleep(3)
        login_submit = Login.login_submit(driver)
        login_submit.click()

    login_err_text = Login.login_err_text(driver)
    assert login_err_text.text == "존재하지 않거나 잘못된 정보로 잦은 로그인 시도하였습니다. 정보보호를 위해 15분간 접속이 차단됩니다."


def test_login_validation_check12(driver, url, user_id, user_pw):
    """
    홈> 로그인> 10회 이상 로그인실패(정보보안으로 15분동안 로그인불가) >2분뒤 로그인 재시도

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)

    login_validation(driver, user_id, user_pw + "!!")
    for _ in range(11):
        time.sleep(3)
        login_submit = Login.login_submit(driver)
        login_submit.click()

    time.sleep(120)
    login_submit = Login.login_submit(driver)
    login_submit.click()

    login_err_text = Login.login_err_text(driver)
    assert login_err_text.text == "존재하지 않거나 잘못된 정보로 잦은 로그인 시도하였습니다. 정보보호를 위해 15분간 접속이 차단됩니다."


def test_login_validation_check13(driver, url, user_id, user_pw):
    """
    홈> 로그인> 10회 이상 로그인실패(정보보안으로 15분동안 로그인불가) >16분뒤 로그인 재시도

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)

    login_validation(driver, user_id, user_pw + "!!")
    for _ in range(11):
        time.sleep(3)
        login_submit = Login.login_submit(driver)
        login_submit.click()

    time.sleep(960)
    driver.get(url)
    login_ck(driver)
    login_validation(driver, user_id, user_pw)

    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)
    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."

    login_ck(driver)


def test_login_new_tab(driver, url, user_id, user_pw):
    """
    홈> 로그인 > new탭에서도 로그인 되어있는지

    args:
    - driver: 크롬 드라이버
    - url: .env에 정의된 URL
    - user_id: .env에 정의된 로그인 아이디(이메일)
    - user_pw: .env에 정의된 로그인 패스워드
    """
    driver.get(url)
    login_ck(driver)
    login_validation(driver, user_id, user_pw)

    time.sleep(5)
    driver.execute_script("window.open('https://www.acon3d.com/ko/toon')")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    home_user_info_icon = Home.home_user_info_icon(driver)
    home_user_info_icon.click()
    home_mypage_button = Home.home_mypage_button(driver)
    assert home_mypage_button.text == "유저홈", "유저홈 버튼을 찾을 수없습니다."

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    login_ck(driver)
