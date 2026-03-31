import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_map_url(latitude, longitude, name=None):
    base_url = "https://map.kakao.com/link/map/"
    if name:
        url = f"{base_url}{name},{latitude},{longitude}"
    else:
        url = f"{base_url}{latitude},{longitude}"
    return url

def create_directions_url(latitude, longitude, name=None):
    base_url = "https://map.kakao.com/link/to/"
    if name:
        url = f"{base_url}{name},{latitude},{longitude}"
    else:
        url = f"{base_url}{latitude},{longitude}"
    return url

# 예시 사용 < - 해당 부분을 여행지로 변경
# https://deveapp.com/map.php <- 위도 경도 변환 사이트
latitude = 34.7921469527007
longitude = 126.425695326
name = "목포갓바위"

map_url = create_map_url(latitude, longitude, name)
directions_url = create_directions_url(latitude, longitude, name)

# Selenium을 사용하여 Chrome으로 URL 열기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 첫 번째 URL 열기
# driver.get(map_url)
# time.sleep(5)

# 두 번째 URL ( 목적지 ) 열기
driver.get(directions_url)
driver.implicitly_wait(10)
time.sleep(5)


input("Press Enter to close the browser...")
driver.quit()