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
latitude = 35.1594965345398
longitude = 129.162576586723
name = "해운대해수욕장"

latitude_YeoSu = 34.8377033412796
longitude_YeoSu = 127.892653150096
name_YeoSu = "여수 보물섬" # 위치는 남해군청 좌표를 가져옴

# 인터파크 투어 국내여행 1박 기준 2개의 목적지

# map_url = create_map_url(latitude, longitude, name)
directions_url = create_directions_url(latitude, longitude, name)
directions_url_YeoSu = create_directions_url(latitude_YeoSu, longitude_YeoSu, name_YeoSu)

# Selenium을 사용하여 Chrome으로 URL 열기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 핑찍힌 지도 열기
# driver.get(map_url)
# driver.implicitly_wait(10)
# time.sleep(5)

# 목적지 URL 열기
driver.get(directions_url)
driver.implicitly_wait(10)
time.sleep(5)

# 5초 뒤에 여수 표시

driver.get(directions_url_YeoSu)
time.sleep(5)

input("Press Enter to close the browser...")
# Enter를 눌러야 창 닫음
driver.quit()