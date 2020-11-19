
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

list= []
list2 = []

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
ber_product = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(ber_product))
assert len(ber_product) == 3

add_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in add_buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver,8)

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veggie in veggies:
    list2.append(veggie.text)

print(list)
print(list2)

assert list == list2

beforeDiscount = driver.find_element_by_css_selector(".totAmt").text

#time.sleep(2)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

afterDiscount = driver.find_element_by_css_selector(".discountAmt").text

assert float(afterDiscount) < int(beforeDiscount)

totalAmounts = driver.find_elements_by_xpath("//tr/td[5]/p")
s = 0
for amount in totalAmounts:
    s = s + int(amount.text)
print(s)
assert s == int(beforeDiscount)

#time.sleep(5)
success_info = driver.find_element_by_class_name("promoInfo").text
print(success_info)
time.sleep(2)
driver.quit()
