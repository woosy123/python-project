import tkinter as tk
from tkinter import messagebox
import csv
import sys

class MBTITestApp:
    def __init__(self, master,name,birth, gender):
        self.master = master
        self.current_question = 0
        self.answers = []
        self.name = name
        self.master.title(f"{self.name}의 경상도 사투리 Test")
        self.questions, self.choices = self.load_data("test_data.csv")

        self.create_widgets()

    def load_data(self, filename):
        questions = []
        choices = []

        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                questions.append(row[0])
                choices.append(row[1:])

        return questions, choices

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text=self.questions[self.current_question])
        self.question_label.pack()

        self.choices_var = tk.StringVar(value=self.choices[self.current_question])

        self.next_button = tk.Button(self.master, text="다음", command=self.next_question)
        self.next_button.pack()

        for choice in self.choices[self.current_question]:
            choice_radio = tk.Radiobutton(self.master, text=choice, variable=self.choices_var, value=choice)
            choice_radio.pack()

    def next_question(self):
        selected_choice = self.choices_var.get()
        if selected_choice:
            self.answers.append(selected_choice)
            self.choices_var.set("")
            self.current_question += 1

            if self.current_question < len(self.questions):
                self.question_label.config(text=self.questions[self.current_question])

                # 현재 질문의 선택지 라디오 버튼 업데이트
                for widget in self.master.winfo_children():
                    if isinstance(widget, tk.Radiobutton):
                        widget.destroy()

                self.choices_var = tk.StringVar(value=self.choices[self.current_question])
                
                for choice in self.choices[self.current_question]:
                    choice_radio = tk.Radiobutton(self.master, text=choice, variable=self.choices_var, value=choice)
                    choice_radio.pack()

                if self.current_question == len(self.questions) - 1:
                    self.next_button.config(text="완료")
            else:
                self.save_result()
                self.master.destroy()

        else:
            messagebox.showerror("오류", "선택지를 선택해주세요.")

    def save_result(self):
        filename = "test_result.csv"
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Question", "Answer"])
            for i, question in enumerate(self.questions):
                writer.writerow([question, self.answers[i]])
        messagebox.showinfo("저장 완료", "테스트 결과가 저장되었습니다.")

name = sys.argv[1]
birth = sys.argv[2]
gender = sys.argv[3]

# 애플리케이션 실행
root = tk.Tk()
root.geometry("500x500")
app = MBTITestApp(root, name, birth, gender)
root.mainloop()
