from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver")
driver.get("https://www.edfa3ly.com/cart")
time.sleep(5)
ele = driver.find_element_by_name("url")
ele.send_keys("https://www.abercrombie.com/shop/wd/p/skinny-suede-belt-41330319?categoryId=12266&seq=02&faceout=prod1")
