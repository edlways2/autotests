from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x): return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "https://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)


	# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
	button = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "100"))
	button = browser.find_element(By.ID, "book")
	button.click()
	# Считаем
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	# вставляем ответ
	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(y)
	# Нажимаем кнопку
	button = browser.find_element(By.ID, "solve")
	button.click()

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(7)
	# закрываем браузер после всех манипуляций
	browser.quit()