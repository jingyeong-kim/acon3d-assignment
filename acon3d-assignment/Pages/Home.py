from selenium.webdriver.common.by import By


class Home:
    def home_login_button(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-2e2b475a-2:nth-child(2) .sc-53b29b66-1 > div")

    def home_acon_intro_button(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-53b29b66-1 > .menu__about")

    def home_user_info_icon(self):
        return self.find_element(By.CSS_SELECTOR, ".flex > .sc-2e2b475a-7")

    def home_mypage_button(self):
        return self.find_element(By.CSS_SELECTOR, ".gdhZu")

    def home_logout_button(self):
        return self.find_element(By.CSS_SELECTOR, ".menu__signout > .sc-11b3376b-2")
