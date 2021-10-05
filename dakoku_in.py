#!/usr/bin/env python3

#webdriverをimportする 
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser

# Configファイルを読み込む
config = configparser.ConfigParser()
config.read("config", encoding="utf-8")
kotId = config["config"]["id"]
kotPw = config["config"]["pw"]

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

print('connectiong to remote browser...')
Chrome = webdriver.Chrome(executable_path=r"./chromedriver") 
driver = Chrome

# KoTの打刻ページへアクセス
driver.get('https://s2.kingtime.jp/independent/recorder/personal/')
print(driver.current_url)

# ログインIDとパスワードを入力して、OKをクリック
inputId = driver.find_element(By.ID, "id")
inputPw = driver.find_element(By.ID, "password")
buttonOK = driver.find_element_by_css_selector(".btn-control-message")
inputId.send_keys(kotId)
inputPw.send_keys(kotPw)
buttonOK.click()

# 出退勤ボタンが押せるようになるまで待つようにする
driver.implicitly_wait(5)

# ログインしたら、「出勤」をクリック
buttonSyukkin = driver.find_element_by_css_selector(".record-clock-in")
buttonSyukkin.click()

# ブラウザを終了する
driver.quit()