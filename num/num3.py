from time import sleep

import pytest



# @allure.feature('HR考勤判定自动化')
class TestUi:
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)  # 隐式等待， 全局有效，等待十秒 ，超时报错
    driver.maximize_window()

    def setup(self):
        driver = self.driver
        driver.get('http://portal.drumbeatdev.com/login')
        driver.find_element_by_id('account_name').send_keys('CS13')
        driver.find_element_by_id('password').send_keys('123qwe')
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/form/button').click()

    #
    def teardown(self):
        driver = self.driver
        sleep(5)
        driver.close()
        print('结束')

    # @pytest.mark.parametrize('date', read_yaml_testcase("应用token/hr_ui.yaml"))
    def test_hr_ui(self, date):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="355272421562933248"]/div[2]/div[8]/div').click()  # 打开HR应用
        sleep(2)
        als = driver.window_handles  # 切换网页
        driver.switch_to.window(als[-1])  # 跳转到HR tab页
        driver.find_element_by_xpath('//*[@id="root"]/div/section/aside/div/div[3]/ul/li[8]/div').click()
        driver.find_element_by_xpath('//*[@id="rc-menu-uuid-10178-2-439254862581153792-popup"]/li[3]/span').click()
        assert date('assert') in driver.title


if __name__ == '__main__':
    pytest.main(['-s', 'test_hr_ui.py'])
