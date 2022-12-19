from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


try:
    print('ПОГНАЛИ НАХУЙ!')
    url = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(url)
    first_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    first_button.click()
    confirm_button = browser.switch_to.alert
    confirm_button.accept()
    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    print(f"X = {x}")

    def calc(x: int) -> int:
        return math.log(abs(12*math.sin(x)))

    y = calc(int(x))
    print(f"Y = {y}")

    answer_bar = browser.find_element(By.ID, "answer")
    answer_bar.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    result = browser.switch_to.alert
    final = result.text
    browser.switch_to.alert.accept()
finally:
    print('DONE')
    ans = final.split()
    print(ans[-1])
    browser.quit()
