import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Use o driver correspondente ao seu navegador
        self.driver.get("http://localhost:8080")  # URL do seu servidor Flask

    def test_add(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.XPATH, "//button[text()='+']").click()
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(1)  # Aguarde o resultado aparecer
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "8")

    def test_sub(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='7']").click()
        driver.find_element(By.XPATH, "//button[text()='-']").click()
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "4")

    def test_mul(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='4']").click()
        driver.find_element(By.XPATH, "//button[text()='×']").click()
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "20")

    def test_div(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='8']").click()
        driver.find_element(By.XPATH, "//button[text()='/']").click()
        driver.find_element(By.XPATH, "//button[text()='2']").click()
        driver.find_element(By.XPATH, "//button[text()='=']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "4")

    def test_square(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.XPATH, "//button[text()='x²']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "9")

    def test_sqrt(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='9']").click()
        driver.find_element(By.XPATH, "//button[text()='√x']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "3")

    def test_sin(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.XPATH, "//button[text()='0']").click()
        driver.find_element(By.XPATH, "//button[text()='sin']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "-0.9880316240928618")

    def test_cos(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='0']").click()
        driver.find_element(By.XPATH, "//button[text()='cos']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "1")

    def test_tan(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='4']").click()
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        driver.find_element(By.XPATH, "//button[text()='tan']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "1")

    def test_pi(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='π']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "π")

    def test_euler(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='e']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "e")

    def test_read_variable(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='SX']").click()
        driver.find_element(By.XPATH, "//button[text()='1']").click()
        driver.find_element(By.XPATH, "//button[text()='0']").click()
        driver.find_element(By.XPATH, "//button[text()='RX']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "10")

    def test_clear(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[text()='9']").click()
        driver.find_element(By.XPATH, "//button[text()='C']").click()
        time.sleep(1)
        result = driver.find_element(By.CLASS_NAME, "display").text
        self.assertEqual(result, "0")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
