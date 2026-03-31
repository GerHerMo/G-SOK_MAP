from Func_CountCO2 import VehicleCo2
from Random_OBJ_Image import Dp_Random_Img, set_emission_co2, set_dif_emission_co2

# 이동 수단 입력
em_vehicle = VehicleCo2(bus_time=30, subway_time=50, electric_car_time=50,train_time=43)

if em_vehicle.Bool_trainUsed == True:
    using_train = input('KTX면 1, KTX Sancheon 또는 Mugunghwa면 2, Nuriho 또는 ITX 일 경우 3번을 입력해주세요 : ')
    em_vehicle.set_train_kind(using_train=using_train)
# em_vehicle.set_train_kind('3')
emission_co2_value = round(em_vehicle.calculate_co2()/1000.0,2) # kg 단위

# 결과를 Random_OBJ_Image의 emission_co2 변수에 설정
set_emission_co2(emission_co2_value)
set_dif_emission_co2(round(em_vehicle.calculate_only_car()-emission_co2_value,1))

image_folder = "C:/ABCBootCamp/G_SOK_MAP_Project/ImgFolder"
# 해당 이미지 경로에 이름과 맞는 이미지가 있어야 작동
Dp_Random_Img(image_folder)
