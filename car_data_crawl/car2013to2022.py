import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = Options()
prefs = {"download.default_directory": "/Users/jungyun/bootcamp_ai/git/SKN04-1st-4Team/car_data_crawl"}
options.add_experimental_option('prefs', prefs)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 웹 페이지에 띄워진 정보를 긁어오는 것
driver.get('https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1257')

select_element = Select(driver.find_element('css selector', 'select#stat_box'))
select_element.select_by_value('125704')
bs = BeautifulSoup(driver.page_source, 'lxml')

# 페이지 로드 대기 (필요에 따라 조정)
time.sleep(5)

# iframe으로 전환
iframe_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//iframe[@name="showStblGams"]'))
)
driver.switch_to.frame(iframe_element)

# iframe 내에서 요소 찾기 및 클릭
download_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "excelButton"))
)
download_button.click()

time.sleep(10)

# 작업 후 기본 프레임으로 돌아가기
driver.switch_to.default_content()

driver.quit()