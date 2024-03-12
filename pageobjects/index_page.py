from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver  # 声明webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 等待
from selenium.webdriver.support import expected_conditions as EC


class Index:

    def __init__(self, driver: WebDriver):  # 声明WebDriver，以便提示
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # 等待时间


