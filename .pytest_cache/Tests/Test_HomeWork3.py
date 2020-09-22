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

        driver.quit()


    def test_second(self):
        baseUrl = "http://35.236.6.102/litecart/"
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseUrl)

        first_product = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, " //*[@id='box-campaign-products']//article[1]")))

        first_product_name = first_product.find_element(By.XPATH, ".//*[@class = 'name']").text

        first_product_price = first_product.find_element(By.XPATH, ".//*[@class = 'regular-price']")
        first_product_price_value = first_product_price.text
        first_product_price_color = first_product_price.value_of_css_property('color')
        first_product_price_style = first_product_price.value_of_css_property('text-decoration-line')

        first_product_discount = first_product.find_element(By.XPATH, ".//*[@class = 'campaign-price']")
        first_product_discount_value = first_product_discount.text
        first_product_discount_color = first_product_discount.value_of_css_property('color')
        first_product_discount_style = first_product_discount.value_of_css_property('font-weight')

        first_product.click()

        item_page_product_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='box-product']//h1"))).text
        item_page_product_price = driver.find_element(By.XPATH, ".//*[@class = 'regular-price']")
        item_page_price_value = item_page_product_price.text
        item_page_price_color = item_page_product_price.value_of_css_property('color')
        item_page_price_style = item_page_product_price.value_of_css_property('text-decoration-line')

        item_page_discount = driver.find_element(By.XPATH, ".//*[@class = 'campaign-price']")
        item_page_discount_value = item_page_discount.text
        item_page_discount_color = item_page_discount.value_of_css_property('color')
        item_page_discount_style = item_page_discount.value_of_css_property('font-weight')

        assert first_product_name == item_page_product_name

        assert first_product_price_value == item_page_price_value
        assert first_product_price_color == item_page_price_color
        assert first_product_price_style == item_page_price_style

        assert first_product_discount_value == item_page_discount_value
        assert first_product_discount_color == item_page_discount_color
        assert first_product_discount_style == item_page_discount_style

        driver.quit()