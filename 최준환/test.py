import tkinter as tk
import pandas as pd
from tkinter import messagebox

class SatooriTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("경상도 사투리 테스트")
        self.root.geometry("400x400")
        
        self.questions = []
        self.answers = []
        self.choices = []
        self.current_question_index = 0
        self.score = 0
        self.results = []

        self.load_file()

        self.question_label = tk.Label(self.root, text="")
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
        self.root.withdraw()  # 이전 창 숨기기

        result_window = tk.Toplevel(self.root)
        result_window.title("결과")
        result_window.geometry("300x200")

        result_label = tk.Label(result_window, text="테스트가 종료되었습니다.")
        result_label.pack(pady=10)

        score_label = tk.Label(result_window, text=f"점수: {self.score} / 11")
        score_label.pack()

        if self.score >= 9:
            message = "경상도 토박이시네요!"
        else:
            message = "경상도 분이 아니신가봐요!"

        message_label = tk.Label(result_window, text=message)
        message_label.pack(pady=10)

        exit_button = tk.Button(result_window, text="종료", command=self.exit_program)
        exit_button.pack(pady=10)

        self.save_results_to_file()

    def save_results_to_file(self):
        file_path = "test_results.xlsx"
        df = pd.DataFrame(self.results)
        df.to_excel(file_path, index=False)

    def exit_program(self):
        self.root.destroy()

root = tk.Tk()
app = SatooriTestApp(root)
root.mainloop()
