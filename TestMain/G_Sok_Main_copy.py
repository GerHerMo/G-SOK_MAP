from Func_CountCO2_copy import VehicleCo2
from Random_OBJ_Image_copy import Dp_Random_Img, set_emission_co2, set_footprint_co2

em_vehicle = VehicleCo2(bus_time=30,train_time=50,electric_bicycle_time=25)


if em_vehicle.Bool_trainUsed == True:
    using_train = input('KTX면 1, KTX Sancheon 또는 Mugunghwa면 2, Nuriho 또는 ITX 일 경우 3번을 입력해주세요 : ')
    em_vehicle.set_train_kind(using_train=using_train)
# em_vehicle.set_train_kind('3')
emission_co2_value = round(em_vehicle.calculate_co2()/1000.0,2) # kg 단위


# 결과를 Random_OBJ_Image의 emission_co2 변수에 설정
set_emission_co2(emission_co2_value)
set_footprint_co2(50)

image_folder = "C:/ABCBootCamp/G_SOK_MAP_Project/ImgFolder"
# 해당 이미지 경로에 이름과 맞는 이미지가 있어야 작동
Dp_Random_Img(image_folder)
