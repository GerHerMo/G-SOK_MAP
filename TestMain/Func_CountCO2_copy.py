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

class VehicleCo2:
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

        self.Bool_trainUsed = False
        self.emission_train = 0.0
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



    global emissions_data

    def set_train_kind(self,using_train):
        if self.train_time != 0.0:
            # using_train = input("이용한 열차 : ")
            match using_train:
                case "1":
                    self.emission_train = self.train_time / 60.0 * emissions_data["Train"]["KTX"]["speed"] * emissions_data["Train"]["KTX"]["emission"]
                case "2":
                    self.emission_train = self.train_time / 60.0 * emissions_data["Train"]["KTX_Sancheon_and_Mugunghwa"]["speed"] * emissions_data["Train"]["KTX_Sancheon_and_Mugunghwa"]["emission"]
                case "3":
                    self.emission_train = self.train_time / 60.0 * emissions_data["Train"]["Nuriro_and_ITX_Cheongchun_and_ITX_Saemaeul"]["speed"] * emissions_data["Train"]["Nuriro_and_ITX_Cheongchun_and_ITX_Saemaeul"]["emission"]
                case _:
                    self.emission_train = 0.0
                    print("잘못된 값을 입력하셨습니다, 열차시간은 계산에서 제외합니다")
        else:
            print("입력된 기차가 없습니다")


    def calculate_co2(self):
        # move_bus = (25.0/60.0 * emissions_data["Bus"]["speed"])*emissions_data["Bus"]["emission"]
        self.emissions_co2 = (self.emission_bus + self.emission_subway + self.emission_s_flight +
                              self.emission_l_flight + self.emission_g_car + self.emission_d_car +
                              self.emission_elec_car + self.emission_elec_bicycle + self.emission_train)

        return round(self.emissions_co2,2)

# vehicle = VehicleCo2(train_time= 30,subway_time=50,electric_car_time=40)
# vehicle.set_train_kind('3')
# print(vehicle.calculate_co2())
