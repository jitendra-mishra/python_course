from time import sleep
from selenium import webdriver

# set the path of ChromeDriver in Mac,
# normally we put the driver in /usr/local

# Open Chrome browser
#https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/
#driver = webdriver.Chrome(executable_path="/usr/local/chromedriver")

#Open Firefox browser
# we have to donwload the Gecodriver: https://github.com/mozilla/geckodriver/releases
driver = webdriver.Firefox(executable_path="/usr/local/geckodriver")

webdriver.Ie

driver.get("https://www.google.co.in")
driver.maximize_window()

#sleep for 5 seconds
sleep(5)

#get title
title = driver.title
print(title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()

driver.quit()