import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
country_list = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
c = "India"
found = False
for country in country_list:
    print("country", country.text)
    if (country.text == c):
        found = True
        print("India present")
        country.click()
        break
if not found:
    print("India not found")
assert driver.find_element_by_id("autosuggest").get_attribute('value') == c
driver.quit()