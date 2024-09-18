from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x): return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Принимаем окно
    confirm = browser.switch_to.alert
    confirm.accept()
    # Считаем
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # вставляем ответ
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()