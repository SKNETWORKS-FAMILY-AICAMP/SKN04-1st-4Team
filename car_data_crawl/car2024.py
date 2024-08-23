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
from selenium.webdriver.chrome.options import Options

options = Options()
prefs = {"download.default_directory": "/Users/jungyun/bootcamp_ai/git/SKN04-1st-4Team/car_data_crawl"}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
time.sleep(6)

driver.get('https://kosis.kr/statHtml/statHtml.do?orgId=116&tblId=DT_MLTM_1244&vw_cd=MT_ZTITLE&list_id=M2_18&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%2FstatisticsList%2FstatisticsListIndex.do')
time.sleep(10)

main = driver.window_handles # 팝업창 끄기

for i in main:
    if i != main[0]:
        driver.switch_to.window(i)
        driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.switch_to.frame("iframe_leftMenu") # 왼쪽 iframe 선택
driver.find_element(By.XPATH, '/html/body/div/form/div[2]/ul/li/li[18]/ul/li[17]/ul/li[1]/a/span').click() # 시도별 클릭
time.sleep(15)
driver.switch_to.alert.accept() # 알림창 끄기
time.sleep(5)
driver.switch_to.default_content() # 오른쪽 iframe으로 넘어가기 위해 초기화
driver.switch_to.frame("iframe_rightMenu") # 오른쪽 iframe 선택
driver.switch_to.frame("iframe_centerMenu2") # 센터메뉴2 iframe 선택
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[1]/div/div[1]/span[1]/button[1]').click() # 시점 클릭
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[2]/div[2]/div/ul/li[8]/span/span[2]').click() # 23년 12월 클릭
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[1]/button[1]').click() # 조회 클릭
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[1]/div/div[2]/button[9]').click() # 조회조건 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[1]/div/div[2]/label/input').click() # 전체선택 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[1]/div/div[3]/div/ul/li[4]/span/span[2]' ).click() # 계 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/h3[2]').click() # 시도명 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[2]/div/div[2]/label/input').click() # 전체선택 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/h3[3]').click() # 시군구 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[3]/div/div[2]/label/input').click() # 전체선택 클릭
time.sleep(7)
driver.switch_to.alert.accept() # 알림창 끄기
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[3]/div/div[2]/label/input').click() # 전체선택 클릭으로 초기화
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[3]/div/div[3]/div/ul/li[1]/span/span[2]').click() # 계 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/h3[4]').click() # 레벨01 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[4]/div/div[2]/label/input').click() # 전체선택 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[2]/div[4]/div/div[3]/div/ul/li[5]/span/span[2]').click() # 총계 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[7]/div[3]/div[1]/div[2]/div[1]/span/button').click() # 조회 클릭
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/form[2]/div[5]/div[2]/div[3]/div[1]/div/div[2]/button[7]').click() # 다운로드 클릭
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form[2]/div[3]/div[4]/div/div[2]/div[3]/span[1]/a').click() # 다운로드 클릭
time.sleep(10)


driver.quit()