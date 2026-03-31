emissions_data = {
    "S_Flight": {
        "emission": 255.0,
        "scope": "Scope 1",
        "speed": 850
    },
    "L_Flight": {
        "emission": 150.0,
        "scope": "Scope 1",
        "speed": 925
    },
    "Gasoline_Car": {
        "emission": 192.0,
        "scope": "Scope 1",
        "speed": 57 # 고속도로와 일반도로 평균값의 평균
    },
    "Diesel_Car": {
        "emission": 171.0,
        "scope": "Scope 1",
        "speed": 57
    },
    "Bus": {
        "emission": 105.0,
        "scope": "Scope 1",
        "speed": 22
    },
    "Subway":{
        "emission": 26.0,
        "scope": "Scope 1",
        "speed": 50
    },
    "Electric_Car": {
        "emission": 53.0,
        "scope": "Scope 2",
        "speed": 46 # 출처 : https://www.wltpfacts.eu/from-nedc-to-wltp-change/
    },
    "Electric_Bicycle": {
        "emission": 12.0,
        "scope": "Scope 2",
        "speed": 17 # 평균 15~20 km/h
    },
    "Train": {
        "KTX": {
            "emission": 19.92,
            "scope": "Scope 2",
            "speed": 180
        },
        "KTX_Sancheon_and_Mugunghwa": {
            "emission": 38.105,
            "scope": "Scope 2",
            "speed": 120 # KTX 산천과 무궁화호의 평균속도
        },
        "Nuriro_and_ITX_Cheongchun_and_ITX_Saemaeul": {
            "emission": 27.19,
            "scope": "Scope 2",
            "speed": 140 # 누리호, ITX 의 평균속도
        }
    }
}

# gCO2e(Co2 그램 배출량)/p-Km (승객 - 킬로미터)
print(emissions_data)

# 총 거리에 따른 탄소배출량 계산 = (각 이동수단별 이동 거리 X 해당 수단의 km 당 co2 배출량 ) 의 합산
# = SUM( ( ( 이동수단 평균 속도(km/h) X 이동수단 사용시간 ) X 이동수단 km/ co2배출량 ) X 인원수 )

# ex) 15km 이동시 버스로 10분 , 도보로 100미터, 지하철 30분, 버스 15분 사용시 탄소배출량
example_value = 0.0
move_bus = (25.0/60.0 * emissions_data["Bus"]["speed"])*emissions_data["Bus"]["emission"]
move_walking = 0.1 * 0
move_subway = (0.5 * emissions_data["Subway"]["speed"])*emissions_data["Subway"]["emission"]

example_value +=round(move_bus + move_walking + move_subway,3)
print(f"{move_bus} + {move_walking} + {move_subway}")
print(f"총 Co2 배출량 : {example_value} gCo2e/pkm")