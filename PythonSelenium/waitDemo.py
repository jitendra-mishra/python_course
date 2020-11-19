
import time

from selenium import webdriver

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
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()


time.sleep(2)
driver.quit()
