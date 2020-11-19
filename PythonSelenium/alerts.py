import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("jitu")
driver.find_element_by_css_selector("#alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
alert.accept()
assert "jitu" in alertText

time.sleep(3)
driver.find_element_by_css_selector("#name").send_keys("jitu")
driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
alert = driver.switch_to.alert
dismissText = alert.text
print(dismissText)
alert.dismiss()
time.sleep(3)
assert "jitu" in dismissText



driver.quit()

