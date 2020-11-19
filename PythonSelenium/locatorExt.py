from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")

driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Jitu")
driver.find_element_by_css_selector(".password").send_keys("Mishra")
driver.find_element_by_link_text("Forgot Your Password?").click()

#sleep(3)

driver.find_element_by_xpath("//a[text()='Cancel']").click()

#xpath
#//div[@id='usernamegroup']/label

#css-selector - check there is a space present
#div[id='usernamegroup'] label

#grant-parent
#//form[@name='login']/div[1]/label

sleep(2)
##grand-parent using css
str = driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text
#goto 1st label
#form[name='login'] label:nth-child(1)
print(str)

driver.quit()


