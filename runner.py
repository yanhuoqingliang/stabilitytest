import time
from threading import Thread

import timertools
from bmkpage import BmkPage
from cmkpage import Cmkpage

target_time = 60*60*2


def B_control():
    start_time = timertools.start()
    B_page = BmkPage('123f07fc')
    B_page.click_video_button()
    time.sleep(1.5)
    while True:
        if timertools.is_expired(start_time, target_time):
            break
        B_page.swipe_to_left(2)
        B_page.swipe_to_right(2)
        B_page.swipe_to_up(1)
        B_page.swipe_to_down(1)


def c_start_001(url):
    start_time = timertools.start()
    c_page = Cmkpage(url)
    time.sleep(10)
    c_page.click_immediately_enter()
    time.sleep(1.5)
    while True:
        if timertools.is_expired(start_time, target_time):
            break
        c_page.click_chat()
        c_page.input_chat_content()
        time.sleep(1.5)
        c_page.click_send_button()
        time.sleep(10)


def c_start_002(url):
    start_time = timertools.start()
    c_page = Cmkpage(url)
    time.sleep(10)
    c_page.click_immediately_enter()
    time.sleep(1.5)
    while True:
        if timertools.is_expired(start_time, target_time):
            break
        c_page.click_free_viewing()
        time.sleep(1.5)
        c_page.click_second_group()
        time.sleep(1.5)
        c_page.back_to_explain()
        time.sleep(20)


def readfile(filepath):
    lines = []
    with open('token.txt', 'r') as f:
        for line in f.readlines():
            lines.append(line)
        return lines


if __name__ == '__main__':
    urls = readfile('token.txt')
    B_con = Thread(target=B_control, name='B')
    c_con1 = Thread(target=c_start_001, name='C1', args=(urls[0],))
    c_con2 = Thread(target=c_start_001, name='C2', args=(urls[1],))
    c_con3 = Thread(target=c_start_002, name='C3', args=(urls[2],))
    B_con.start()
    c_con1.start()
    c_con2.start()
    c_con3.start()
    B_con.join()
    c_con1.join()
    c_con2.join()
    c_con3.join()










