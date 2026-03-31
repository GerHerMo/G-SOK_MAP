emissions_data = {
    "S_Flight": {
        "emission": 255.0, # gCo2 단위
        "scope": "Scope 1",
        "speed": 850,
        'avg_emission': 0.3 # 이동수단별 km당 평균 탄소 배출량
    },
    "L_Flight": {
        "emission": 150.0,
        "scope": "Scope 1",
        "speed": 925,
        'avg_emission': 0.16
    },
    "Gasoline_Car": {
        "emission": 192.0,
        "scope": "Scope 1",
        "speed": 57, # 고속도로와 일반도로 평균값의 평균
        'avg_emission': 3.37
    },
    "Diesel_Car": {
        "emission": 171.0,
        "scope": "Scope 1",
        "speed": 57,
        'avg_emission': 3.0
    },
    "Bus": {
        "emission": 105.0,
        "scope": "Scope 1",
        "speed": 22,
        'avg_emission': 0.47
    },
    "Subway":{
        "emission": 26.0,
        "scope": "Scope 1",
        "speed": 50,
        'avg_emission': 0.52
    },
    "Electric_Car": {
        "emission": 53.0,
        "scope": "Scope 2",
        "speed": 46, # 출처 : https://www.wltpfacts.eu/from-nedc-to-wltp-change/
        'avg_emission': 1.15
    },
    "Electric_Bicycle": {
        "emission": 12.0,
        "scope": "Scope 2",
        "speed": 17, # 평균 15~20 km/h
        'avg_emission': 0.71
    },
    "Train": {
        "KTX": {
            "emission": 19.92,
            "scope": "Scope 2",
            "speed": 180,
            'avg_emission': 0.11
        },
        "KTX_Sancheon_and_Mugunghwa": {
            "emission": 38.105,
            "scope": "Scope 2",
            "speed": 120, # KTX 산천과 무궁화호의 평균속도
            'avg_emission': 0.32
        },
        "Nuriro_and_ITX_Cheongchun_and_ITX_Saemaeul": {
            "emission": 27.19,
            "scope": "Scope 2",
            "speed": 140, # 누리호, ITX 의 평균속도
            'avg_emission': 0.19
        }
    }
}

class VehicleCo2:
    global emissions_data

    def __init__(self,bus_time=0.0,subway_time=0.0,s_flight_time=0.0,l_flight_time=0.0,
                 gasoline_car_time=0.0,diesel_car_time=0.0,electric_car_time=0.0,
                 train_time=0.0,electric_bicycle_time=0.0 ):
        self.bus_time = bus_time
        self.subway_time = subway_time
        self.s_flight_time = s_flight_time
        self.l_flight_time = l_flight_time
        self.gasoline_car_time = gasoline_car_time
        self.diesel_car_time = diesel_car_time
        self.train_time = train_time
        self.electric_bicycle_time = electric_bicycle_time
        self.electric_car_time = electric_car_time

        self.using_train = 0
        self.avg_emission = 0.0
        self.avg_em_only_car = 0.0
        self.Bool_trainUsed = False
        self.emission_train = 0.0
        self.list_avg = list(emissions_data.keys())[:-1]
        self.list_vtime = [self.s_flight_time,self.l_flight_time,self.gasoline_car_time,self.diesel_car_time,
                             self.bus_time,self.subway_time,self.electric_car_time,self.electric_bicycle_time]

        self.emission_bus =  self.bus_time / 60.0 * emissions_data["Bus"]["speed"] * emissions_data["Bus"]["emission"]
        self.emission_subway = self.subway_time / 60.0 * emissions_data["Subway"]["speed"] * emissions_data["Subway"]["emission"]
        self.emission_s_flight =  self.s_flight_time / 60.0 * emissions_data["S_Flight"]["speed"] * emissions_data["S_Flight"]["emission"]
        self.emission_l_flight =  self.l_flight_time / 60.0 * emissions_data["L_Flight"]["speed"] * emissions_data["L_Flight"]["emission"]
        self.emission_g_car =  self.gasoline_car_time / 60.0 * emissions_data["Gasoline_Car"]["speed"] * emissions_data["Gasoline_Car"]["emission"]
        self.emission_d_car =  self.diesel_car_time / 60.0 * emissions_data["Diesel_Car"]["speed"] * emissions_data["Diesel_Car"]["emission"]
        self.emission_elec_car = self.electric_car_time / 60.0 * emissions_data["Electric_Car"]["speed"] * emissions_data["Electric_Car"]["emission"]
        self.emission_elec_bicycle = self.electric_bicycle_time / 60.0 * emissions_data["Electric_Bicycle"]["speed"] * emissions_data["Electric_Bicycle"]["emission"]

        self.emissions_co2 = 0.0
        # 초기화시에 각 이동수단별 시간을 가져온다
        if self.train_time== 0.0:
            self.Bool_trainUsed = False
        else:
            self.Bool_trainUsed = True

    def set_train_kind(self,using_train):
        self.using_train = using_train
        if self.train_time != 0.0:
            # using_train = input("이용한 열차 : ")
            match self.using_train:
                case "1":
                    self.emission_train = (self.train_time / 60.0 * emissions_data["Train"]["KTX"]["speed"] *
                                           emissions_data["Train"]["KTX"]["emission"])
                case "2":
                    self.emission_train = (self.train_time / 60.0 * emissions_data["Train"]["KTX_Sancheon_and_Mugunghwa"]["speed"] *
                                           emissions_data["Train"]["KTX_Sancheon_and_Mugunghwa"]["emission"])
                case "3":
                    self.emission_train = (self.train_time / 60.0 * emissions_data["Train"]["Nuriro_and_ITX_Cheongchun_and_ITX_Saemaeul"]["speed"] *
                                           emissions_data["Train"]["Nuriro_and_ITX_Cheongchun_and_ITX_Saemaeul"]["emission"])
                case _:
                    self.emission_train = 0.0
                    print("잘못된 값을 입력하셨습니다, 열차는 계산에서 제외됩니다")
        else:
            print("입력된 기차가 없습니다")

    def calculate_co2(self):
        # move_bus = (25.0/60.0 * emissions_data["Bus"]["speed"])*emissions_data["Bus"]["emission"]
        self.emissions_co2 = (self.emission_bus + self.emission_subway + self.emission_s_flight +
                              self.emission_l_flight + self.emission_g_car + self.emission_d_car +
                              self.emission_elec_car + self.emission_elec_bicycle + self.emission_train)

        return round(self.emissions_co2,2)

    def calculate_avg_emission(self): # 비교 대조용으로 사용, 실질적으로 사용되진 않음 ( 검증용 )
        for index in range(len(self.list_avg)):
            self.avg_emission += emissions_data[self.list_avg[index]]['avg_emission'] * ( self.list_vtime[index] )

        if self.using_train == 1 :
            self.avg_emission += emissions_data["Train"]["KTX"]['avg_emission'] * self.train_time
        elif self.using_train == 2:
            self.avg_emission += emissions_data["Train"]["KTX_Sancheon_and_Mugunghwa"]['avg_emission'] * self.train_time
        elif self.using_train == 3:
            self.avg_emission += emissions_data["Train"]["Nuriro_and_ITX_Cheongchun_and_ITX_Saemaeul"]['avg_emission'] * self.train_time

            # emissions_data[self.list_avg[index]]['avg_emission'] => km 당 평균 배출량
        return self.avg_emission

    def calculate_only_car(self):
        total_car_emission = 0.0
        # 비행기를 제외한 나머지 이동수단의 시간을 모두 차량 이동으로 가정하고 배출량 계산
        for time in self.list_vtime:
            total_car_emission += (time / 60.0) * emissions_data["Gasoline_Car"]["speed"] * emissions_data["Gasoline_Car"]["emission"]

        # 비행기 배출량
        total_car_emission += self.emission_s_flight
        total_car_emission += self.emission_l_flight

        # 최종 배출량을 kg 단위로 변환
        return round(total_car_emission / 1000.0, 2)


vehicle = VehicleCo2(bus_time=30, subway_time=50, electric_car_time=50,train_time=43)
vehicle.set_train_kind('1')
print(vehicle.calculate_co2())
print(vehicle.calculate_only_car())