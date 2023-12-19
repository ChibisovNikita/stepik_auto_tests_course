from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    send1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    send1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element1.text
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
    input4 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input4.click()
    alert = browser.switch_to.alert
    alert.accept()
finally:
    time.sleep(3)
    browser.quit()