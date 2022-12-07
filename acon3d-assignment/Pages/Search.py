from selenium.webdriver.common.by import By


class Search:
    def search_box(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-1c0752e2-0")

    def not_search_keyword(self):
        return self.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div/div[2]')



