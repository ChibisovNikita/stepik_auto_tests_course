import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    element1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element1.text
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    input2.click()

finally:
    time.sleep(5)
    browser.quit()