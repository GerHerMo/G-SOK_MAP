import tkinter as tk
from PIL import Image, ImageTk
import random
import os

def Dp_Random_Img(image_folder, top_text, top_text_font, text_lines, text_font):
    # 이미지 폴더의 모든 파일을 가져옴
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]

    # 랜덤으로 이미지 파일 선택
    selected_image = random.choice(image_files)

    # 이미지 파일 경로
    image_path = os.path.join(image_folder, selected_image)

    # Tkinter 창 생성
    root = tk.Tk()
    root.title("G-SOK Map")

    # 최상단 텍스트 라벨 추가
    top_text_label = tk.Label(root, text=top_text, font=top_text_font)
    top_text_label.pack(pady=10)

    # 이미지를 로드하고 표시
    img = Image.open(image_path)
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
image_folder = "C:\ABCBootCamp\G_SOK_MAP_Project\ImgFolder"

# 랜덤 이미지에 따른 레이블 변경
n = 12
random_obj = "소나무"
unit = "그루"

# 최상단에 표시할 텍스트와 폰트
top_text = f"고마워요! 덕분에 {n}{unit}의 {random_obj}를 지켰어요!"
top_text_font = ("NanumGothic", 20, "bold")

# 출력할 텍스트 라인과 폰트
text_lines = [
    "This is a random image viewer.",
    "The image above is selected randomly.",
    "This viewer can also display text."
]
text_font = ("Helvetica", 12)

Dp_Random_Img(image_folder, top_text, top_text_font, text_lines, text_font)
