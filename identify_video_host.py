import argparse
import Constant as c 
from selenium import webdriver
import time

driver = webdriver.Chrome(c.DRIVER)
driver.get('chrome://extensions/')
time.sleep(0.5)
driver.get_screenshot_as_file('1_chrome_extensions.png')
# driver.find_element_by_id("knob").click()

# print(driver.find_element_by_class_name("div.more-actions"))

print(driver.find_element_by_xpath('//*[@id="knob"]'))
# print(driver.find_elements_by_tag_name("span"))
time.sleep(0.5)
driver.get_screenshot_as_file('1_dev_mode.png')



