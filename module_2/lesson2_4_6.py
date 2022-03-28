from selenium import webdriver
import time 
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome(r"C:\Users\wwwma\environments\selenium_course\chromedriver")
    browser.get(link)
    browser.find_element_by_id("button")

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
