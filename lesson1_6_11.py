from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(r"C:\Users\wwwma\environments\selenium_course\chromedriver")
    browser.get(link)
    
    
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control first"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control second"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control third"]')
    input3.send_keys("adrg@sftgtj.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text


   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
