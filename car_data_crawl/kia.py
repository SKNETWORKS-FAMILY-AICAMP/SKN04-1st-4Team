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

driver.get('https://www.kia.com/kr/customer-service/center/faq')
driver.maximize_window()


text = []
title = []
images = []
category = []
index_ = [3, 4, 6]
for i in index_:
    driver.find_element(By.XPATH,
            f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/ul/li[{i}]/button'
        ).click()
    if i == 6:
        time.sleep(5)
        driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div/h3/button').click()
        category.append('홈페이지')
        #타이틀 버튼 누르기
        time.sleep(2)
        title.append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div/h3/button').text.replace('\'', '').replace('\"', '').strip())
        #제목 넣기
        try:
            text.append(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div/div').text.replace('\'', '').replace('\"', '').strip())
            #내용넣기
            image = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div/div/div/div/ul/li/div/picture/img')
            images.append(image.get_attribute('src'))
            #이미지 저장

        except:
            images.append(None)
            #이미지가 없다면 공백 저장
    elif i == 4:
        time.sleep(3)
        num_ = len(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div/ul').text.split('\n'))
        for h in range(2, num_ + 1):
            time.sleep(3)
            a = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div').text.split('\n')
            a = len([data for data in a if data]) + 1
            for k in range(1, a):
                driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/h3/button').click()

                time.sleep(2)
                
                category.append('차량정비')

                #타이틀 버튼 누르기
                title.append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/h3/button').text.replace('\'', '').replace('\"', '').strip())
                #제목 넣기
                
                try:
                    text.append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/div').text.replace('\'', '').replace('\"', '').strip())
                    #내용넣기
                    image = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/div/div/div/ul/li/div/picture/img')
                    images.append(image.get_attribute('src'))
                    
                    #이미지 저장
                except:
                    images.append(None)
                    #이미지가 없다면 공백 저장
            driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div/ul/li[{h}]/a').click()
        
    else:
        time.sleep(3)
        num_ = len(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div/ul').text.split('\n'))
        for h in range(2, num_ + 1):
            a = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div').text.split('\n')
            a = len([data for data in a if data]) + 1
            for k in range(1, a):
                driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/h3/button').click()

                time.sleep(2)
                
                category.append('차량구매')

                #타이틀 버튼 누르기
                title.append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/h3/button').text.replace('\'', '').replace('\"', '').strip())
                #제목 넣기
                
                try:
                    text.append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/div').text.replace('\'', '').replace('\"', '').strip())
                    #내용넣기
                    image = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{k}]/div/div/div/ul/li/div/picture/img')
                    images.append(image.get_attribute('src'))
                    #이미지 저장
                except:
                    images.append(None)
                    #이미지가 없다면 공백 저장

            driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div/ul/li[{h}]/a').click()

driver.quit()

text_ = text[:30]
images_ = images[:30]
category_ = category[:30]
title_ = title[:30]

for i in range(len(images_)):
    with psycopg2.connect(
        host='192.168.0.87',
            dbname='postgres',
            user='postgres',
            password='qksrkqek12',
            port=8874
        )as conn:
            with conn.cursor() as cur:
                cur.execute(f'''INSERT INTO project1.faq VALUES ('kia', '{title_[i]}', '{category_[i]}', '{images_[i]}', '{text_[i]}')''')
