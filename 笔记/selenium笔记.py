# 1、安装
# pip install selenium

# 2、下载浏览器驱动
# （1）谷歌驱动
# http://chromedriver.storage.googleapis.com/index.html
# linux chrome
# https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm

# （2）火狐驱动
# https://github.com/mozilla/geckodriver/releases/

# 3、测试代码
# 可以指定路径，或将驱动放到当前文件夹
from selenium import webdriver

url = "https://www.baidu.com/"

# 加载驱动
# driver = webdriver.Firefox()   # Firefox浏览器
# driver = webdriver.Firefox("驱动路径")
driver = webdriver.Chrome()    # Chrome浏览器
# driver = webdriver.Ie()        # Internet Explorer浏览器
# driver = webdriver.Edge()      # Edge浏览器
# driver = webdriver.Opera()     # Opera浏览器
# driver = webdriver.PhantomJS()   # PhantomJS

# 打开网页
driver.get(url)

# 3 等待策略
# 3.1 显式等待
# 显式等待使WebDriver等待某个条件成立时继续执行，否则在达到最长事件抛出超时异常（TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

element = WebDriverWait(driver, 3, 0.5).until(
    EC.presence_of_element_located((By.ID, "kw"))
)
element.send_keys('python')
driver.quit()

# WebDriverWait类有WebDriver提供，在设置事件内，默认每间隔一段时间检测一次当前页面元素是否存在，如果超时则未检测到，则抛出异常。
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
# driver：浏览器驱动
# timeout：最长超时时间，默认单位为s
# poll_frequency：超时后的异常信息，默认情况下抛–NoSuchElementException异常。
# WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。
#
# until(method, message=‘’) 调用该方法提供的驱动程序作为一个参数，直到返回值为True。
# until_not(method, message=‘’) 调用该方法提供的驱动程序作为一个参数，直到返回值为False。

# 3.2 隐式等待
# 如果某些元素不是立即可用的，隐式等地啊是告诉WebDriver去等待一定时间后去查找元素。默认等待时间为0秒，一旦设置该值，隐式等待是设置该WebDriver的实例的生命周期。
from selenium import webdriver
from selenium.webdriver.common.by import By

# 加载驱动
driver = webdriver.Chrome()  # Chrome浏览器

url = "https://www.baidu.com/"
driver.set_window_size(1000, 900)

# 隐式等待
driver.implicitly_wait(10)  # seconds

driver.get(url)

driver.find_element(By.ID, "kw").clear()
driver.find_element(By.ID, "kw").send_keys("Python")
driver.find_element(By.ID, "su").click()

# 4 浏览器控制
# 1、控制浏览器窗口大小
driver.set_window_size(900, 700)

# 2、浏览器前进、后退
driver.forward()
driver.back()

# 3、刷新
driver.refresh()

# 5 元素定位
# 通过id 查询首个满足条件
driver.find_element(by=By.ID, value="username")
# 通过class 查询所有满足条件 [列表形式返回]
driver.find_elements(by=By.CLASS_NAME, value="item")
# 通过TAG_NAME
driver.find_elements(by=By.TAG_NAME, value="a")
driver.find_elements(by=By.TAG_NAME, value="a").get_attribute("href")
# 参数一by ：By.ID、By.CLASS_NAME、By.NAME
# 参数二value: 指定 ID、name或Class的值

# 4 具体使用
# 3.1 元素查找、定位
# 3.3 Webelement常用方法
# 1、点击和输入
driver.find_element(By.ID, "kw").clear()  				# 清除文本
driver.find_element(By.ID, "kw").send_keys("Python")    # 模拟按键输入
driver.find_element(By.ID, "su").click()  				# 点击元素

# 2、提交
# 模拟输入框回车操作
# 新版本中未测试出功能

# 3、其他
#
# size：返回元素尺寸
# text：获取元素的文本
# get_attribute(name)：获取属性值
# is_displayed：设置元素是否用户可见
# 总结：
from selenium import webdriver

# 加载驱动
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Chrome浏览器

# url = "https://read.douban.com/ebook/7821748/?dcs=search"
url = "https://www.baidu.com/"
driver.set_window_size(900, 700)
# 打开网页
driver.get(url)

driver.find_element(By.ID, "kw").clear()  # 清除文本
driver.find_element(By.ID, "kw").send_keys("Python")  # 模拟按键输入
driver.find_element(By.ID, "su").click()  # 点击元素

# 4 鼠标操作
# selenium鼠标事件用的是ActionChains，在调用的时候并不会执行，而是在perform()方法被调用后执行。
# 引用 ActionCharins类
# from selenium.webdriver.common.action_chains import ActionChains

# 4.1 单击/双击/鼠标右击
url = "https://www.baidu.com/"

# 实例：点击百度图片超链接
from selenium import webdriver

# 引用ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://www.baidu.com/"

driver = webdriver.Chrome()  # Chrome浏览器

# 隐式等待
driver.implicitly_wait(10)  # seconds

# 打开网页
driver.get(url)
rc = driver.find_element(by=By.LINK_TEXT, value="图片")

# 右击
# ActionChains(driver).context_click(rc).perform()
# 双击
# ActionChains(driver).double_click(rc).perform
# 单击
ActionChains(driver).click(on_element=rc).perform()

# 4.2 移动元素
# 这个测试案例并不是很好，各位大佬如果有的话可以留言。
# 移动元素
element = driver.find_element(By.LINK_TEXT, "图片")
target = driver.find_element(By.LINK_TEXT, "更多")
ActionChains(driver).drag_and_drop(element, target).perform()

# 5 键盘事件
# 全选 Ctrol+A ：send_keys(Keys.CONTROL, 'a')
# 复制 Ctrol+C：send_keys(Keys.CONTROL, 'c')
# 剪切 Ctrol+X：send_keys(Keys.CONTROL, 'x')
# 粘贴 Ctrol+V：send_keys(Keys.CONTROL, 'v')
#
# 键盘 F1：send_keys(Keys.F1)
# …
# 键盘 F12：send_keys(Keys.F12)
#
# 删除键 BackSpace：send_keys(Keys.BACK_SPACE)
#
# 空格键 Space：send_keys(Keys.SPACE)
#
# 制表键 Tab：send_keys(Keys.TAB)
#
# Esc键 Tab：send_keys(Keys.ESCAPE)
#
# 回车键 ENTER：send_keys(Keys.ENTER)

# 5.1 输入
from selenium import webdriver

# 引入 ActionChains 类
from selenium.webdriver import Keys

# 加载驱动
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()  # Chrome浏览器

url = "https://www.baidu.com/"
driver.set_window_size(1000, 900)

driver.get(url)

driver.find_element(By.ID, "kw").clear()
driver.find_element(By.ID, "kw").send_keys("Pythonn")
driver.find_element(By.ID, "kw").send_keys(Keys.BACK_SPACE)

# 5.2 组合按键
# Ctrl+a
ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# 6 获取页面信息
# 获取当前页面URL
now_url = driver.current_url
# 获取当前页面title
title = driver.title

# 11 文件上传
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')

# 12 cookie操作
# WebDriver操作cookie的方法：
#
# get_cookies()： 获得所有cookie信息。
# get_cookie(name)： 返回字典的key为“name”的cookie信息。
# add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。
# delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。
# delete_all_cookies()： 删除所有cookie信息

# 13 调用JavaScript代码
# 获取网页标题
driver.execute_script('return document.title;')


# 14 关闭浏览器
# 关闭单个窗口
driver.close()
# 关闭所有窗口
driver.quit()
