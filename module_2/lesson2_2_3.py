from selenium import webdriver
import time 
import math

def calc(x, y):
    return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(r"C:\Users\wwwma\environments\selenium_course\chromedriver")
    browser.get(link)
    
    x0 = browser.find_element_by_id("num1")
    y0 = browser.find_element_by_id("num2")
    x = x0.text
    y = y0.text
    z = calc(x, y)
    z_el = str(z)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z_el) 

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
