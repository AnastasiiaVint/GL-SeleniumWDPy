from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_homework5():

    def test_first(self):
        baseUrl = "http://35.236.6.102/litecart/"
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseUrl)

        # Add random items to the cart
        num = 1
        while num < 4:
            popular_products = driver.find_elements(By.XPATH, "//*[@id='box-popular-products']//article")
            number_of_products = len(popular_products)
            driver.find_element(By.XPATH, "//*[@id='box-popular-products']//article[%s]" % random.randrange(1,number_of_products)).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name = 'add_cart_product']"))).click()
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@id = 'cart']//div[@class = 'badge quantity']"),(str(num))))
            driver.back()
            num += 1

        # Navigate to the shopping cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id = 'cart']//a"))).click()

        # Remove all products from the cart one-by-one.
        number_of_remove_buttons = len(WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//button[@title = 'Remove']"))))

        while number_of_remove_buttons > 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title = 'Remove']"))).click()
            time.sleep(1)
            number_of_remove_buttons -= 1

        empty_cart_indication = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/p[contains(text(), 'There are no items in your cart.')]")))
        assert empty_cart_indication.is_displayed()