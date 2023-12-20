import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAbs(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Chrome()
        def registration(self, link):
            browser = self.driver
            browser.implicitly_wait(5)
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
            browser.find_element(By.CSS_SELECTOR, ".third_class .third").send_keys("test@mail.ru")
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            welcome_text= browser.find_element(By.TAG_NAME, "h1").text
            return welcome_text

        def test_link1(self):
            link = "http://suninjuly.github.io/registration1.html"
            registration_result = self.registration(link)
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", registration_result)
        def test_link2(self):
            link = "http://suninjuly.github.io/registration2.html"
            registration_result = self.registration(link)
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", registration_result)
        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()
