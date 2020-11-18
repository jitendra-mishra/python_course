from time import sleep
from selenium import webdriver

# set the path of ChromeDriver in Mac,
# normally we put the driver in /usr/local
driver = webdriver.Chrome(executable_path="/usr/local/chromedriver")
driver.get("https://www.google.co.in")

#sleep for 5 seconds
sleep(5)

#get title
title = driver.title
print(title)
print(driver.current_url)
driver.quit()