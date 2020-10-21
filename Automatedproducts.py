from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver")
driver.get("https://www.edfa3ly.com/cart")
time.sleep(5)
ele = driver.find_element_by_name("url")
ele.send_keys("https://www.6pm.com/p/product/9409514")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='sb-site']/div[1]/div[1]/div[2]/div/div[2]/form/div[2]/div/div[2]/input[1]").click()