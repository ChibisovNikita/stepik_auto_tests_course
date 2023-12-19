#Импортировать unittest в файл: import unittest
import unittest
#Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
class TestAbs(unittest.TestCase):
 #Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
 #Изменить assert на self.assertEqual()
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

#Заменить строку запуска программы на unittest.main()
if __name__ == "__main__":
    unittest.main()