from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.ID, "num1")
    num1 = int(a.text)
    b = browser.find_element(By.ID, "num2")
    num2 = int(b.text)
    sum_num = int(num1) + int(num2)
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(sum_num))
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()