import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for checkbox in checkboxes:
    if (checkbox.get_attribute("value") == "option2"):
        checkbox.click()
        checkbox.is_selected()

radioboxes = driver.find_elements_by_xpath("//input[@type='radio']")
for radiobox in radioboxes:
    if (radiobox.get_attribute("value") == "radio2"):
        radiobox.click()
    print("ena", radiobox.is_enabled())
    print("sel",radiobox.is_selected())


time.sleep(3)
driver.quit()