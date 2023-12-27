import allure
import pytest
from selenium import webdriver


from selenium import webdriver

from log_util import logger


class Base:

    def __init__(self, url):
        # 创建一个driver
        # 第一步：创建一个driver实例变量
        logger.info("创建driver")
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(500, 800)
        self.driver.implicitly_wait(5)
        self.driver.get(url)

    @allure.description
    def do_find(self, by, value=None):
        logger.info(f"查找元素{by, value}")
        """查找单个元素"""
        if value:
            return self.driver.find_element(by, value)
        else:
            # (By.ID,"")
            return self.driver.find_element(*by)

    def do_finds(self, by, value=None):
        """查找多个元素"""
        # (By.ID,"")
        if value:
            return self.driver.find_elements(by, value)
        else:
            return self.driver.find_elements(*by)

    def do_execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    def do_send_keys(self, text, by, value=None):
        logger.info(f"输入内容{text}")
        """输入文本"""
        ele = self.do_find(by, value)
        ele.clear()
        ele.send_keys(text)
