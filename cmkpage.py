from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from base import Base


class Cmkpage(Base):

    _BIN_IMMEDIATELY_ENTER = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/button/div')
    _BIN_CHAT = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[4]/div[1]/div/div[6]/div[2]')
    _INPUT_CHAT_CONTENT = (By.XPATH, '/html/body/div[3]/div[1]/div/input')
    _BIN_SEND = (By.XPATH, '/html/body/div[3]/div[1]/div/button')
    _BIN_FREE_VIEW = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]/div')
    _BIN_BACK_EXPLAIN = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div')
    _BIN_SECOND_GROUP = (By.XPATH, '//*[@id="previewContainer"]/div[3]/div[1]/div/div/div[1]/div/div[2]/div[2]')

    def click_immediately_enter(self):
        self.do_find(self._BIN_IMMEDIATELY_ENTER).click()

    def click_chat(self):
        self.do_find(self._BIN_CHAT).click()

    def input_chat_content(self):
        faker = Faker(['zh_CN'])
        JS_ADD_TEXT_TO_INPUT = """
              var elm = arguments[0], txt = arguments[1];
              elm.value += txt;
              elm.dispatchEvent(new Event('change'));
              """
        b = u'\ud83d' + u'\udc4d'
        elem = self.do_find(self._INPUT_CHAT_CONTENT)
        self.do_execute_script(JS_ADD_TEXT_TO_INPUT, elem, f"{faker.name()}: {b}{b}{b}")
        elem.send_keys("欢迎你进入同屏讲解！！！")

    def click_send_button(self):
        self.do_find(self._BIN_SEND).click()

    def click_free_viewing(self):
        self.do_find(self._BIN_FREE_VIEW).click()

    def click_second_group(self):
        self.do_find(self._BIN_SECOND_GROUP).click()

    def back_to_explain(self):
        self.do_find(self._BIN_BACK_EXPLAIN).click()




