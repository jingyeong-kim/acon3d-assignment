from selenium.webdriver.common.by import By


class Login:
    def move_login_page(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-2e2b475a-2:nth-child(2) .sc-53b29b66-1 > div")

    def input_user_id(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-adefc696-2 > .sc-adefc696-5")

    def input_user_pw(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-adefc696-3 > .sc-adefc696-5")

    def user_id_save_ck(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-adefc696-7")

    def login_submit(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-adefc696-9")

    def login_err_text(self):
        return self.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/div')

    def login_err_text_id(self):
        return self.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div')

    def login_user_join_button(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-adefc696-13")
