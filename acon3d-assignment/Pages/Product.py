from selenium.webdriver.common.by import By


class Product:
    def product_buy_button(self):
        return self.find_element(By.CSS_SELECTOR, ".sc-a695b05b-8 > div")
