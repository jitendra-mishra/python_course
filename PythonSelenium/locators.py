from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")

driver.get("https://rahulshettyacademy.com/angularpractice")

#driver.find_element_by_name("name").send_keys("Hello")
#driver.find_element_by_xpath("//div[@class='form-group']//input[@name='name']").send_keys("Hello")
driver.find_element_by_css_selector("input[name='name']").send_keys("HELLO")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@type='submit']").click()

sleep(3)
str = driver.find_element_by_class_name("alert-success").text
str1 = driver.find_element_by_css_selector("[class*='alert-success']").text
str2 = driver.find_element_by_xpath("//*[contains(@class, 'alert-success')]").text
print(str)
print(str1)


#salesforce login page
#username field
driver.find_element_by_css_selector("input[class*='username']")

driver.quit()




