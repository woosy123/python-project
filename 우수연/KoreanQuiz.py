import tkinter as tk
import pandas as pd
from PIL import ImageTk, Image
import random

class KoreanQuiz:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.current_question = 0
        self.total_questions = 10  # 전체 문제 수
        self.results = []  # 결과 저장용 리스트
        
        # 대사 데이터를 엑셀 파일에서 읽어옵니다.
        self.dialogues = pd.read_excel('dialogues.xlsx')

        self.question_description_label = tk.Label(root, text="description", font=('Arial', 14), wraplength=400)
        self.question_description_label.pack()

        self.question_label = tk.Label(root, text="Question", font=('Arial', 14))
        self.question_label.pack()

        self.answer_entry = tk.Entry(root, font=('Arial', 12))
        self.answer_entry.pack()

        self.answer_entry.bind("<Return>", self.check_answer)  # Enter 키로 제출하도록 바인딩합니다.

        self.result_label = tk.Label(root, text="", font=('Arial', 14))
        self.result_label.pack()

        self.image_label = tk.Label(root)  # Label to display the image
        self.image_label.pack()

        self.question_order = self.generate_question_order()
        self.display_question()

    def generate_question_order(self):
    # Generate a random order of questions.
        total_questions = len(self.dialogues)
        question_indices = list(range(total_questions))
        random.shuffle(question_indices)  # Shuffle the indices randomly

        if total_questions <= self.total_questions:
            return question_indices
        else:
            return question_indices[:self.total_questions]
        
    def display_question(self):
        # 현재 질문과 설명을 가져와서 화면에 표시합니다.
        current_question_index = self.question_order[self.current_question]
        question_description = self.dialogues['Description'][current_question_index]
        question = self.dialogues['Question'][current_question_index]
        self.question_description_label.configure(text='\n'+question_description)
        self.question_label.configure(text='\n'+question+'\n')

        image_path = "./daily.jpg"  # Replace with the path to your image
        image = Image.open(image_path)
        image = image.resize((250, 130))  # Resize the image if needed
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def check_answer(self, event=None):
        # 사용자가 입력한 답과 정답을 비교하여 점수를 계산합니다.
        current_question_index = self.question_order[self.current_question]
        user_answer = self.answer_entry.get()
        correct_answer = self.dialogues['Answer'][current_question_index]

        if user_answer == correct_answer:
            self.score += 1

        # 결과를 저장합니다.
        result = {
            'Description': self.dialogues['Description'][current_question_index],
            'Question': self.dialogues['Question'][current_question_index],
            'Answer': correct_answer,
            'UserAnswer': user_answer,
            'Score': self.score
        }
        self.results.append(result)

        self.current_question += 1
        self.answer_entry.delete(0, tk.END)

        if self.current_question == self.total_questions:
            self.display_result()
        else:
            self.display_question()

    def display_result(self):
        # 결과를 화면에 표시합니다.
        self.question_description_label.destroy()
        self.question_label.destroy()
        self.answer_entry.destroy()

        result_text = f"맞은 개수는 \n {self.score}/{self.total_questions}\n 입니다!\n"

        if self.score >= 8:
            result_text += "\n폼 미쳐따\n"
        elif self.score >= 5:
            result_text += "\n(나이) MZ 일듯말듯..?\n"
        elif self.score >= 3:
            result_text += "\n노력만..! 하고 계시네요\n"
        else:
            result_text += "\n한국인 맞아요?\n"

        self.result_label.configure(text=result_text)

        exit_button = tk.Button(root, text="종료", font=('Arial', 14), command = lambda : self.quit_quiz())
        exit_button.pack(side=tk.BOTTOM, pady=10)

        # 결과를 파일에 저장합니다.
        self.save_results_to_file()

    def save_results_to_file(self):
        # 결과를 Excel 파일로 저장합니다.
        df = pd.DataFrame(self.results)
        df.to_excel('quiz_results.xlsx', index=False)


root = tk.Tk()
root.geometry("400x400")  # 창의 크기 조정
app = KoreanQuiz(root)
root.mainloop()