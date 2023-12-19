from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(element1_num1, element2_num2):
    return str(element1_num1 + element2_num2)

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    element1_num1 = int(element1.text)
    element2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    element2_num2 = int(element2.text)
    m = sum( element1_num1, element2_num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(m))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()