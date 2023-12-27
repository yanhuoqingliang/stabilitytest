import time

from adbtools import AdbTools, KeyCode


class BmkPage(object):

    def __init__(self, device_id):
        self.Device = AdbTools(device_id)
        self.screen_size = self.Device.get_screen_normal_size()
        self.x = int(self.screen_size[0])
        self.y = int(self.screen_size[1])

    def swipe_to_right(self, loop: int):
        for number in range(1, loop+1):
            self.Device.shell(f'input swipe {self.x/4} {self.y/2} {self.x*3/4} {self.y/2} {500}')
            time.sleep(1.5)

    def swipe_to_left(self, loop: int):
        for number in range(1, loop+1):
            self.Device.shell(f'input swipe {self.x*3/4} {self.y/2} {self.x/4} {self.y/2} {500}')
            time.sleep(1.5)

    def swipe_to_up(self, loop: int):
        for number in range(1, loop+1):
            self.Device.shell(f'input swipe {self.x/2} {self.y*3/4} {self.x/2} {self.y/4} {500}')
            time.sleep(1.5)

    def swipe_to_down(self, loop: int):
        for number in range(1, loop+1):
            self.Device.shell(f'input swipe {self.x/2} {self.y/4} {self.x/2} {self.y*3/4} {500}')
            time.sleep(1.5)

    def click_video_button(self):
        self.Device.shell(f'input tap 510 1444')

    def click_guduan_button(self):
        self.Device.shell(f'input tap 643 1446')
        self.Device.shell(f'input tap 619 1462')

    def input(self, text):
        self.Device.shell(f'input text {text}')

    def send_keyevent(self, keycode):
        self.Device.send_keyevent(keycode)


if __name__ == '__main__':
    pass