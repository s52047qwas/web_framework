from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver  # 声明webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 等待
from selenium.webdriver.support import expected_conditions as EC


# https://www.ketangpai.com/#/login
# 578043031
class LoginPage:
    # 元素定位
    # 账号输入框
    user_input = (By.XPATH, '//input[@placeholder="请输入邮箱/手机号/账号"]')
    # 密码输入框
    password_input = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 登录确认框
    login_button = (By.XPATH, '//button[contains(@class,"el-button")]//span[text()="登录"]')
    # 错误替身
    error_tips = (By.XPATH, '//p[contains(@class,"el-message__content")]"]')

    # 元素操作

    def __init__(self, driver: WebDriver):  # 声明WebDriver，以便提示
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # 等待时间

    def login(self, user, password):
        # 登录操作
        self.wait.until(EC.visibility_of_element_located(self.login_button))  # 等待登录按钮可见
        self.driver.find_element(*self.user_input).send_keys(user)  # 输入账号
        self.driver.find_element(*self.password_input).send_keys(password)  # 输入账号
        self.driver.find_element(*self.login_button).click()  # 点击登录按钮

    def get_login_error_msg(self):
        self.wait.until(EC.visibility_of_element_located(self.error_tips))  # 等待错误提示可见
        return self.driver.find_element(*self.error_tips).text  # 返回错误提示文本信息
