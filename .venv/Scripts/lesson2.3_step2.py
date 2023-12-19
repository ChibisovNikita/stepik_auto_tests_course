from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    click1 = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    click1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    element1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element1.text
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input2.click()
finally:
    time.sleep(5)
    browser.quit()
