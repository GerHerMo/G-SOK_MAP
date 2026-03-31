# G-SOK MAP (Green Sustainability Our Key MAP)

## 📌 프로젝트 소개
**G-SOK MAP**은 사용자의 다양한 이동 수단 이용 내역을 바탕으로 탄소 배출량을 계산하고, 환경 보호 성과를 시각적으로 보여주는 친환경 데스크톱 애플리케이션입니다. 내연기관 자동차를 이용했을 때와 비교하여 얼마나 많은 탄소(CO2)를 절감했는지 계산하고, 그 성과를 '나무', '해바라기', '벌' 등의 이미지와 그린 마일리지로 환산하여 직관적으로 보여줍니다. 또한, 카카오맵 연동을 통해 목적지까지의 경로 안내 기능을 제공합니다.

---

## 🚀 주요 기능
1. **이동 수단별 탄소 배출량 계산 (`Func_CountCO2.py`)**
   - 버스, 지하철, 기차(KTX, 무궁화호, ITX 등), 전기차, 전기자전거, 비행기 등 다양한 이동 수단의 소요 시간을 입력받아 총 탄소 배출량을 계산합니다.
   - 이동을 전면 자동차로만 했을 때의 배출량(`calculate_only_car()`)과 비교하여 실질적인 **탄소 절감량**을 산출합니다.

2. **친환경 성과 시각화 (Eco-Reward UI) (`Random_OBJ_Image.py`)**
   - `Tkinter`와 `Pillow`를 활용하여 사용자에게 시각적 리워드를 제공하는 GUI를 띄웁니다.
   - 탄소 절감량에 따라 특정 생물(예: 나무 n그루, 벌 n마리 등)을 지켰다는 메시지를 이미지와 함께 출력하며, 임의의 그린 마일리지를 적립해 줍니다.

3. **카카오맵 연동 길찾기 (`Mapping_Arrive.py`)**
   - `Selenium`과 `webdriver_manager`를 사용하여 카카오맵 웹페이지를 자동으로 실행합니다.
   - 출발지 및 목적지(예: 해운대해수욕장, 여수 등)의 위도/경도 좌표를 기반으로 지도에 핑을 찍거나 길 찾기 URL을 연동합니다.

---

## 📂 프로젝트 구조

```text
G_SOK_MAP_Project/
│
├── ClassAndFunc/                  # 프로젝트의 핵심 로직 폴더
│   ├── G_Sok_Main.py              # 🌟 메인 실행 파일 (탄소 계산 및 GUI 호출)
│   ├── Func_CountCO2.py           # 탄소 배출량 계산 클래스 (VehicleCo2)
│   ├── Random_OBJ_Image.py        # 보상 이미지 및 결과 텍스트를 출력하는 Tkinter GUI 로직
│   └── Mapping_Arrive.py          # Selenium 기반 카카오맵 브라우저 자동화 스크립트
│
├── ImgFolder/                     # GUI에 사용되는 환경 보상 이미지 자원
│   ├── bee.png                    # 벌 이미지 (절감량이 적을 때)
│   ├── sunflower.jpg              # 해바라기 이미지
│   └── tree.jpg                   # 나무 이미지 (절감량이 클 때)
│
└── TestFilese/                    # 기능 구현을 위한 사전 테스트 스크립트 폴더
    ├── MapTest_*.py               # 카카오 모빌리티 API 및 Folium을 활용한 지도/경로 시각화 테스트
    ├── TestCounting_CO2.py        # CO2 계산식 기초 검증 스크립트
    └── *.html                     # Folium으로 생성된 로컬 지도 파일들
