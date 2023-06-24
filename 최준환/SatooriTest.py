import tkinter as tk
import pandas as pd
from tkinter import messagebox
import subprocess

class SatooriTestApp:
    def __init__(self, root):
        self.root = root
        self.questions = []
        self.answers = []
        self.choices = []
        self.current_question_index = 0
        self.score = 0
        self.results = []

        self.load_file()

        self.question_label = tk.Label(self.root, text="", font=("Arial", 11))
        self.question_label.pack()

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda i=i: self.select_answer(i))
            button.pack(side=tk.TOP, padx=10, pady=5)
            self.choice_buttons.append(button)

        self.score_label = tk.Label(self.root, text="")
        self.score_label.pack(pady=10)

        self.load_next_question()

    def load_file(self):
        file_path = "test_data.xlsx"

        if file_path:
            df = pd.read_excel(file_path)
            self.questions = df.iloc[:, 0].tolist()
            self.answers = df.iloc[:, 1].tolist()
            self.choices = df.iloc[:, 2:].values.tolist()

    def load_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            choices = self.choices[self.current_question_index]
            self.question_label.config(text=question)

            for i in range(4):
                self.choice_buttons[i].config(text=choices[i], width=30)

    def select_answer(self, choice_index):
        user_answer = self.choices[self.current_question_index][choice_index]
        correct_answer = self.answers[self.current_question_index]

        if user_answer == correct_answer:
            self.score += 1

        result = {
            "문제": self.questions[self.current_question_index],
            "선택한 답변": user_answer,
            "정답": correct_answer,
            "점수": self.score
        }
        self.results.append(result)

        self.current_question_index += 1
        self.load_next_question()

        if self.current_question_index == len(self.questions):
            self.show_final_score()

    def show_final_score(self):
        self.root.title("결과")
        self.question_label.destroy()
        for i in range(4):
                self.choice_buttons[i].destroy()
        self.root.title("결과")
        self.root.geometry("400x400")

        self.result_label = tk.Label(self.root, text="테스트가 종료되었습니다.")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=f"점수: {self.score} / 10")
        self.score_label.pack()

        try:
            user_data = pd.read_excel('user_data.xlsx')
            user_age = user_data['Age'][0]
        except FileNotFoundError:
            user_age = -1

        if user_age < 25 and self.score >= 9:
            message = f"{user_age}살 인데도 사투리를 잘 아시는 거보니 \n경상도에서 태어나셨군요!"
        elif user_age >= 25 and self.score >= 9:
            message = f"{user_age}살 이신 걸 보니 \n사투리를 잘 아실만 하시네요!"
        else:
            message = "경상도 분이 아니신가봐요!"

        self.message_label = tk.Label(self.root, text=message)
        self.message_label.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="종료", command=lambda : self.root.destroy())
        self.exit_button.pack(side=tk.RIGHT, padx=5, pady=10, anchor=tk.SE)
        
        self.button_more_tests = tk.Button(self.root, text="테스트 더 해보기", command=self.open_test_select)
        self.button_more_tests.pack(side=tk.RIGHT, padx=5, pady=10, anchor=tk.SE)

        self.save_results_to_file()

    def open_test_select(self):
        self.root.destroy()
        from test_select import testselectApp
        testselectApp(self.root)

    def save_results_to_file(self):
        file_path = "test1_results.xlsx"
        df = pd.DataFrame(self.results)
        df.to_excel(file_path, index=False)