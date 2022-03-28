from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"


try:

    browser = webdriver.Firefox() #r"C:\Users\wwwma\environments\selenium_course\geckodriver"
    browser.get(link)
    
    
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys("adrg@sftgtj.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_xpath('//input[@type="file"]')
    element.send_keys(file_path)

   # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
