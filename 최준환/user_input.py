import tkinter as tk
from tkinter import messagebox
import pandas as pd
import subprocess

def save_user_data():
    name = entry_name.get()
    age = entry_age.get()
    gender = var_gender.get()
    
    # 입력값이 비어있는지 확인
    if name == '' or age == '' or gender == '':
        messagebox.showinfo("경고", "사용자 정보를 입력해주세요.")
        return
    
    # 사용자 데이터를 DataFrame으로 생성
    user_data = pd.DataFrame({'Name': [name], 'Age': [age], 'Gender': [gender]})
    
    # DataFrame을 Excel 파일로 저장
    user_data.to_excel('user_data.xlsx', index=False)
    
    # 현재 창 종료
    root.destroy()
    
    # test.py 파일 실행
    subprocess.Popen(['python', 'test_select.py'])

# 사용자 정보 입력 창 생성
root = tk.Tk()
root.geometry("400x400")

label_name = tk.Label(root, text="이름")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="나이")
label_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()

label_gender = tk.Label(root, text="성별")
label_gender.pack()

var_gender = tk.StringVar()

radio_male = tk.Radiobutton(root, text="남성", variable=var_gender, value="남성")
radio_male.pack()

radio_female = tk.Radiobutton(root, text="여성", variable=var_gender, value="여성")
radio_female.pack()

# 초기값으로 선택되지 않도록 설정
var_gender.set(None)

button_done = tk.Button(root, text="완료", command=save_user_data)
button_done.pack()

root.mainloop()
