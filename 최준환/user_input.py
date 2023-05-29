import tkinter as tk
from tkinter import messagebox
import subprocess

def open_test(name, birth, gender):
    test_file = f"my_test.py"
    try:
        subprocess.Popen(["python", test_file, name, birth, gender])
    except FileNotFoundError:
        messagebox.showerror("오류", "테스트 파일을 찾을 수 없습니다.")

class UserInfoWindow:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback
        self.name_var = tk.StringVar()
        self.birth_var = tk.StringVar()
        self.gender_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        name_label = tk.Label(self.master, text="이름:")
        name_label.pack()
        name_entry = tk.Entry(self.master, textvariable=self.name_var)
        name_entry.pack()

        birth_label = tk.Label(self.master, text="생년월일:")
        birth_label.pack()
        birth_entry = tk.Entry(self.master, textvariable=self.birth_var)
        birth_entry.pack()

        gender_label = tk.Label(self.master, text="성별:")
        gender_label.pack()

        gender_frame = tk.Frame(self.master)
        gender_frame.pack()

        male_radio = tk.Radiobutton(gender_frame, text="남성", variable=self.gender_var, value="남성")
        male_radio.pack(side=tk.LEFT)

        female_radio = tk.Radiobutton(gender_frame, text="여성", variable=self.gender_var, value="여성")
        female_radio.pack(side=tk.LEFT)

        # 기본값으로 선택되지 않도록 설정
        self.gender_var.set(None)

        start_button = tk.Button(self.master, text="시작", command=self.start_test)
        start_button.pack()

    def start_test(self):
        name = self.name_var.get()
        birth = self.birth_var.get()
        gender = self.gender_var.get()

        if name and birth and gender:
            self.master.destroy()
            self.callback(name, birth, gender)
        else:
            messagebox.showerror("오류", "모든 정보를 입력해주세요.")


def start_user_info_window():
    root = tk.Tk()
    root.geometry("500x500")
    app = UserInfoWindow(root, open_test)
    # app = UserInfoWindow(root, lambda name, birth, gender: open_test(root, name, birth, gender))
    root.mainloop()

# 사용자 정보 입력 창 실행
start_user_info_window()
