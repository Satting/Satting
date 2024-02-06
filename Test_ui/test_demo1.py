import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # 隐式等待， 全局有效，等待十秒 ，超时报错
driver.maximize_window()
driver.get('https://www.baidu.com')

time.sleep(3)
driver.find_element(By.ID, 'kw').send_keys("selenium")
time.sleep(3)
