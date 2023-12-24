import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebAppTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://127.0.0.1:8000/")

    def fill_form_and_assert(self, a, b, c, d, expected_result):
        driver = self.driver

        # Fill the form
        driver.find_element(By.NAME, "a").clear()
        driver.find_element(By.NAME, "a").send_keys(a)
        driver.find_element(By.NAME, "b").clear()
        driver.find_element(By.NAME, "b").send_keys(b)
        driver.find_element(By.NAME, "c").clear()
        driver.find_element(By.NAME, "c").send_keys(c)
        driver.find_element(By.NAME, "d").clear()
        driver.find_element(By.NAME, "d").send_keys(d)

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Check the result
        self.assertIn(expected_result, driver.page_source)

        # Click the "Back" button
        driver.find_element(By.XPATH, "//button[text()='Back']").click()

    def test_case1(self):
        self.fill_form_and_assert("2", "3", "4", "1", "Result: Condition a &lt; b and c &gt; d")

    def test_case2(self):
        self.fill_form_and_assert("3", "3", "2", "4", "Result: Condition a == b")

    def test_case3(self):
        self.fill_form_and_assert("4", "3", "5", "5", "Result: Condition c == d")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
