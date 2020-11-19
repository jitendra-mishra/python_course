
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
ber_product = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(ber_product))
assert len(ber_product) == 3

add_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in add_buttons:
    button.click()
driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver,8)

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

#time.sleep(2)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
#time.sleep(5)
success_info = driver.find_element_by_class_name("promoInfo").text
print(success_info)
time.sleep(2)
driver.quit()
