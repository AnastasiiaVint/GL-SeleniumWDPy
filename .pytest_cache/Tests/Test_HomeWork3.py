from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_homework():

    def test_first(self):
        baseUrl = "http://35.236.6.102/litecart/admin"
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseUrl)

        username_field = driver.find_element_by_xpath("//input[@name='username']")
        username_field.click()
        username_field.send_keys("admin")

        psw_field = driver.find_element_by_xpath("//input[@name='password']")
        psw_field.click()
        psw_field.send_keys('gl_admin')

        login_btn = driver.find_element_by_xpath("//button[@name='login']")
        login_btn.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@id='box-apps-menu']")))

        left_side_menu_items = driver.find_elements(By.XPATH, "//ul[@id='box-apps-menu']/li")

        number_of_menu = len(left_side_menu_items)

        for i in range(1, number_of_menu + 1):

            item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//ul[@id='box-apps-menu']/li[%s]" % i)))
            item.click()
            header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'panel-heading']")))
            assert header.is_displayed()

            sub_menu = driver.find_elements(By.XPATH, "//ul[@id='box-apps-menu']/li//li")
            number_of_sub_menu = len(sub_menu)

            for j in range(1, number_of_sub_menu + 1):
                sub_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//ul[@id='box-apps-menu']/li//li[%s]" % j)))
                sub_item.click()
                header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'panel-heading']")))
                assert header.is_displayed()