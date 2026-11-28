from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ingresa_usuario(self, username):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)

    def ingresa_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)

    def hacer_click_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def obtener_mensaje_error(self):
        texto_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        return texto_error.text

    def login(self, username, password):
        self.ingresa_usuario(username)
        self.ingresa_password(password)
        self.hacer_click_login()