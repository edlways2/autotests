from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk@a.ru")
    # Или можно так elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]') for element in elements: element.send_keys("Test text")
    name_object = browser.find_element(By.ID, "file")           # находим элемент отвечающий за отправку файла на странице и сохраняем в обЪект
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'biba.txt')           # добавляем к этому пути имя файла 
    name_object.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

       
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()