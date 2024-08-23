import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import psycopg2

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


url = 'https://www.chevrolet.co.kr/faq'
driver.get(url)
text = []
title = []
images = []
category = []
for i in [2,3,5]:
    driver.find_element(By.XPATH, f'/html/body/main/adv-grid[2]/adv-col[1]/div/adv-grid/adv-col[{i}]/div/a').click()
    time.sleep(3)
    for j in range(1, 11):
        driver.find_element(By.XPATH, f'/html/body/main/adv-grid[5]/adv-col/div/div[{j}]/div/div[1]').click()
        time.sleep(1)
        text.append(driver.find_element(By.XPATH, f'/html/body/main/adv-grid[5]/adv-col/div/div[{j}]/div/div[2]/gb-content-well/adv-grid/adv-col/div').text)
        if i == 2:
            category.append('차량구매')
            title.append(driver.find_element(By.XPATH, f'/html/body/main/adv-grid[5]/adv-col/div/div[{j}]/div/div[1]/h6').text.replace('[구매관련]', '').strip())
        elif i == 3:
            category.append('차량정비')
            title.append(driver.find_element(By.XPATH, f'/html/body/main/adv-grid[5]/adv-col/div/div[{j}]/div/div[1]/h6').text.replace('[차량관리]', '').strip())
        else:
            category.append('홈페이지')
            title.append(driver.find_element(By.XPATH, f'/html/body/main/adv-grid[5]/adv-col/div/div[{j}]/div/div[1]/h6').text.replace('[통합계정]', '').strip())
        images.append(None)


for i in range(len(images)):
    with psycopg2.connect(
        host='192.168.0.87',
            dbname='postgres',
            user='postgres',
            password='qksrkqek12',
            port=8874
        )as conn:
            with conn.cursor() as cur:
                cur.execute(f'''INSERT INTO project1.faq VALUES ('en_coe', '{title[i]}', '{category[i]}', '{images[i]}', '{text_[i]}')''')