import tkinter as tk
from KoreanQuiz import KoreanQuiz
from GrumpyTest import GrumpyTestApp
from SatooriTest import SatooriTestApp
import pandas as pd


class test_select:
    def __init__(self,root):
        self.root = root
        # 사용자 정보 읽기
        try:
            user_data = pd.read_excel('user_data.xlsx')
            user_name = user_data['Name'][0]
        except FileNotFoundError:
            user_name = "Unknown"

        self.greeting_label = tk.Label(root, text=f"{user_name}님은 어떤 테스트를 진행하시겠습니까?", font=("Arial", 14))
        self.greeting_label.pack(pady=10)

        self.frame_tests = tk.Frame(root)
        self.frame_tests.pack(pady=10)

        self.button_test1 = tk.Button(self.frame_tests, text="사투리 테스트", command=self.open_test1, width=20, height=5)
        self.button_test1.grid(row=0, column=0, padx=10, pady=10)

        self.button_test2 = tk.Button(self.frame_tests, text="데일리 코리안", command=self.open_test2, width=20, height=5)
        self.button_test2.grid(row=0, column=1, padx=10, pady=10)

        self.button_test3 = tk.Button(self.frame_tests, text="테스트 3", command=self.open_test3, width=20, height=5)
        self.button_test3.grid(row=1, column=0, padx=10, pady=10)

        self.button_test4 = tk.Button(self.frame_tests, text="테스트 4", command=self.open_test4, width=20, height=5)
        self.button_test4.grid(row=1, column=1, padx=10, pady=10)

        self.button_close = tk.Button(self.root, text="종료", command=self.close_program)
        self.button_close.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)
    
        
    def open_test1(self):
        self.all_destroy()
        SatooriTestApp(self.root)
        
    def open_test2(self):
        self.all_destroy()
        KoreanQuiz(self.root)

    def open_test3(self):
        self.all_destroy()
        GrumpyTestApp(self.root)

    def open_test4(self):
        self.all_destroy()
        KoreanQuiz(self.root)

    def all_destroy(self):
        self.button_test1.destroy()
        self.button_test2.destroy()
        self.button_test3.destroy()
        self.button_test4.destroy()
        self.greeting_label.destroy()
        self.frame_tests.destroy()
        self.button_close.destroy()
    def close_program(self):
        root.destroy()


root = tk.Tk()
root.geometry("400x400")
test_select(root)
root.mainloop()