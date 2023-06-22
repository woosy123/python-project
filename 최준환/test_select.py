import tkinter as tk
import subprocess
import pandas as pd

def open_test1():
    subprocess.Popen(['python', 'SatooriTest.py'])
    root.destroy()

def open_test2():
    subprocess.Popen(['python', 'DailyKoreanTest.py'])
    root.destroy()

def open_test3():
    subprocess.Popen(['python', 'test3.py'])
    root.destroy()

def open_test4():
    subprocess.Popen(['python', 'test4.py'])
    root.destroy()

def close_program():
    root.destroy()

# 사용자 정보 읽기
try:
    user_data = pd.read_excel('user_data.xlsx')
    user_name = user_data['Name'][0]
except FileNotFoundError:
    user_name = "Unknown"

root = tk.Tk()
root.geometry("400x400")

greeting_label = tk.Label(root, text=f"{user_name}님은 어떤 테스트를 진행하시겠습니까?", font=("Arial", 14))
greeting_label.pack(pady=10)

frame_tests = tk.Frame(root)
frame_tests.pack(pady=10)

button_test1 = tk.Button(frame_tests, text="사투리 테스트", command=open_test1, width=20, height=5)
button_test1.grid(row=0, column=0, padx=10, pady=10)

button_test2 = tk.Button(frame_tests, text="데일리 코리안", command=open_test2, width=20, height=5)
button_test2.grid(row=0, column=1, padx=10, pady=10)

button_test3 = tk.Button(frame_tests, text="테스트 3", command=open_test3, width=20, height=5)
button_test3.grid(row=1, column=0, padx=10, pady=10)

button_test4 = tk.Button(frame_tests, text="테스트 4", command=open_test4, width=20, height=5)
button_test4.grid(row=1, column=1, padx=10, pady=10)

button_close = tk.Button(root, text="종료", command=close_program)
button_close.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)

root.mainloop()
