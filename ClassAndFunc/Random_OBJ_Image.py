import tkinter as tk
from PIL import Image, ImageTk
import random
import os

emission_co2 = 1.0
dif_emission_co2 = 0.0
customer = '신세계'

def set_emission_co2(value):
    global emission_co2
    emission_co2 = value

def set_dif_emission_co2(value):
    global dif_emission_co2
    dif_emission_co2 = value

def Dp_Random_Img(image_folder):
    # 이미지 폴더의 모든 파일을 가져옴

    image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]

    # 이미지와 관련된 데이터를 리스트로 관리
    image_data = {
        'tree.jpg': (int(dif_emission_co2/9.2), '그루', '나무'),
        'bee.png': (int(dif_emission_co2*500), '마리', '벌'),
        'sunflower.jpg': (int(dif_emission_co2/1.5), '송이', '해바라기')
    }

    # 랜덤으로 이미지 파일 선택
    # selected_image = random.choice(image_files)

    if dif_emission_co2 >= 9.2:
        selected_image = random.choice(['tree.jpg', 'sunflower.jpg'])
    else:
        selected_image = 'bee.png'

    kg = 'kg'

    # 이미지 파일 경로
    image_path = os.path.join(image_folder, selected_image)

    # 선택된 이미지에 따른 변수 설정
    if selected_image in image_data:
        n, unit, random_obj = image_data[selected_image]
        if selected_image == 'bee.png':
            kg = 'g'
            emission_co2_converted = emission_co2 * 1000  # g 단위로 변환
            dif_emission_co2_converted = dif_emission_co2 * 1000  # g 단위로 변환
        else:
            emission_co2_converted = emission_co2  # kg 단위 그대로 사용
            dif_emission_co2_converted = dif_emission_co2  # kg 단위 그대로 사용
    else:
        n, unit, random_obj = (1, '개', '알 수 없는 객체')
        emission_co2_converted = emission_co2
        dif_emission_co2_converted = dif_emission_co2

    # 최상단에 표시할 텍스트와 폰트
    top_text = f"고마워요! {customer}님!\n 덕분에 {n}{unit}의 {random_obj}들을 지켰어요!"
    top_text_font = ("NanumGothic", 20, "bold")

    mileage = random.randint(100, 1000)
    # 출력할 텍스트 라인과 폰트
    text_lines = [
        f"총 {emission_co2_converted}{kg}의 탄소배출량이 발생했고,",
        f"평균 여행보다 {dif_emission_co2_converted}{kg} 만큼의 탄소배출량이 줄었어요!",
        f"현재까지 {mileage} 그린마일리지 적립!"
    ]
    text_font = ("NanumGothic", 14)

    # Tkinter 창 생성
    root = tk.Tk()
    root.title("G-SOK Map")

    # 최상단 텍스트 라벨 추가
    top_text_label = tk.Label(root, text=top_text, font=top_text_font)
    top_text_label.pack(pady=10)

    # 이미지를 로드하고 표시
    img = Image.open(image_path)
    img = img.resize((600, 500),Image.Resampling.LANCZOS)
    # Image.Resampling.LANCZOS : 이미지 리사이즈시 화질 저하를 완화해주는 코드 // pillow 10.0.0 버전 이후 함수명 바뀜
    img = ImageTk.PhotoImage(img)

    panel = tk.Label(root, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    # 텍스트 라벨 추가
    for line in text_lines:
        text_label = tk.Label(root, text=line, font=text_font)
        text_label.pack()

    # Tkinter 이벤트 루프 시작
    root.mainloop()

# 이미지 폴더 경로
# image_folder = "C:/ABCBootCamp/G_SOK_MAP_Project/ImgFolder"
#
# Dp_Random_Img(image_folder)
