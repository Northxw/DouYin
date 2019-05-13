# -*- coding:utf-8 -*-

import random
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import *
import multiprocessing


class DouYin(object):
    def __init__(self, device_udid, driver_port):
        # 驱动配置
        self.desired_caps = {
            'platformName': PLANTFORM,
            'platformVersion': PLANTFORM_VERSION,
            'deviceName': device_udid,
            'udid': device_udid,            # 用于区分多台设备
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY,
            'noReset': True,
            # "unicodeKeyboard": True,
            # "resetKeyboard": True
        }
        self.server = "http://localhost:{}/wd/hub".format(str(driver_port))
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)


    def get_screen_size(self):
        """获取屏幕宽高度"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)


    def enter_fans_list_page(self):
        """进入粉丝列表界面"""
        # 搜索
        search_home_page = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, '//android.widget.ImageView[@resource-id="com.ss.android.ugc.aweme:id/aqz"]'
        )))
        search_home_page.click()
        time.sleep(CLICK_TIME)
        # 搜索输入框
        search_text = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//android.widget.EditText[@resource-id="com.ss.android.ugc.aweme:id/agq"]'
        )))
        search_text.click()
        search_text.send_keys('944454978')
        time.sleep(CLICK_TIME)
        # 搜索
        search_s = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, '//android.widget.TextView[@resource-id="com.ss.android.ugc.aweme:id/agt"]'
        )))
        search_s.click()
        time.sleep(CLICK_TIME + 3)
        # 用户界面
        user = self.wait.until(EC.presence_of_element_located((By.XPATH, USER_XPATH)))
        user.click()
        time.sleep(CLICK_TIME)
        # 粉丝列表界面
        fans = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//android.widget.TextView[@resource-id="com.ss.android.ugc.aweme:id/ak3"]'
        )))
        fans.click()
        time.sleep(CLICK_TIME)

    def crawl_fans_info(self):
        """获取粉丝信息"""
        size = self.get_screen_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.9)
        y2 = int(size[1] * 0.15)

        while True:
            if "暂时没有更多了" in self.driver.page_source or "TA还没有粉丝" in self.driver.page_source:
                break
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(random.randint(3, 4))

        return_ = self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//android.widget.ImageView[@resource-id="com.ss.android.ugc.aweme:id/nj"]'
        )))
        return_.click()
        return_.click()
        self.wait.until(EC.presence_of_element_located((
            By.XPATH, '//android.widget.EditText[@resource-id="com.ss.android.ugc.aweme:id/agq"]'
        ))).clear()

    def main(self):
        """主函数"""
        while True:
            self.enter_fans_list_page()
            self.crawl_fans_info()

if __name__ == '__main__':
    # 进程列表
    process_list = []
    device_list = ['127.0.0.1:62026', '127.0.0.1:62001']
    for device in range(len(device_list)):
        driver_port = 4723 + 2 * device
        douyin = DouYin(device_list[device], driver_port)
        process_list.append(multiprocessing.Process(target=douyin.main))

    for p1 in process_list:
        p1.start()
    for p2 in process_list:
        p2.join()