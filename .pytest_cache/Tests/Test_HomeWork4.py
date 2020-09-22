from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_homework4():

    def test_first(self):
        baseUrl = "http://35.236.6.102/litecart/admin"
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseUrl)

        # Login to admin panel
        username_field = driver.find_element_by_xpath("//input[@name='username']")
        username_field.click()
        username_field.send_keys("admin")

        psw_field = driver.find_element_by_xpath("//input[@name='password']")
        psw_field.click()
        psw_field.send_keys('gl_admin')

        login_btn = driver.find_element_by_xpath("//button[@name='login']")
        login_btn.click()

        # Navigate to the Countries menu
        countries_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                            "//ul[@id='box-apps-menu']//span[@title = 'Countries']")))
        countries_tab.click()

        # Open 'Spain' tab
        spain = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Spain']")))
        spain.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'panel-heading']")))

        arrow_icons = driver.find_elements(By.XPATH, "//i[contains(@class, 'fa-external-link')]")
        number_of_arrow_icon = len(arrow_icons)

        for i in range(number_of_arrow_icon):
            arrow_icon = arrow_icons[i]
            arrow_icon_link = arrow_icon.find_element(By.XPATH, ".//parent::a").get_attribute("href")
            arrow_icon.click()

            driver.switch_to.window(driver.window_handles[-1])
            new_window_current_url = driver.current_url
            assert arrow_icon_link == new_window_current_url
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        driver.quit()
