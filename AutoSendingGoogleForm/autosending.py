from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import datetime

import chromedriver_binary
import time
import os

url = 'https://docs.google.com/forms/d/e/1FAIpQLSfqK5ZfrgjBImj5S8ewax9Ndo2KR5DHPX6oBkt3OHaNPee_IQ/viewform?entry.1109015296=' + '後藤士朗'


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("log-level=3")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

# Chromeで自動操作
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# URLに遷移
driver.get(url)

# メールアドレス指定
# login_id = "メールアドレス" #ここに入力する
# email_form = driver.find_element_by_name("identifier")
# email_form.send_keys(login_id)
# email_form.send_keys(Keys.ENTER)
# time.sleep(1)

# パスワード指定
# login_pw = "パスワード" #ここに入力する
# passwd_form = driver.find_element_by_name("password")
# passwd_form.send_keys(login_pw)
# passwd_form.send_keys(Keys.ENTER)
# time.sleep(1)

# GoogleFormの送信ボタンを押す
submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
submit_button.click
time.sleep(1)


driver.close()
driver.quit()