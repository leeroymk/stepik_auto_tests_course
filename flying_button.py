from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math



print('ПОГНАЛИ НАХУЙ!')

url = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(url)
fly_button = browser.find_element(By.CSS_SELECTOR, "button")
fly_button.click()
currentwindow = browser.window_handles
print(f'SUKA {currentwindow}')
newtab = browser.switch_to.window(currentwindow[1])
x_value = browser.find_element(By.ID, 'input_value')
x = int(x_value.text)
print(f'X = {x}')

def calc(x):
    return math.log(abs(12*math.sin(x)))

y = calc(x)
print(f'Y = {y}')
answer_bar = browser.find_element(By.ID, 'answer')
answer_bar.send_keys(y)
submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()
alertwindow = browser.switch_to.alert
print(alertwindow.text)
sleep(3)
browser.quit()