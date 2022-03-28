from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(r"C:\Users\wwwma\environments\selenium_course\chromedriver")
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
 
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    button = browser.find_element_by_css_selector("button.btn")
    
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    option1.click()
    option2.click()
    button.click()
   

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
