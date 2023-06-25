import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import pandas as pd

class GrumpyTestApp:
    def __init__(self, master):
        self.master = master
        try:
            user_data = pd.read_excel('user_data.xlsx')
            self.name = user_data['Name'][0]
        except FileNotFoundError:
            self.name = "Unknown"
        self.score = 0
        self.question_index = 0
        self.questions = [
            {"question": "1.'요즘애들'이라는 말을 자주 사용한다", "answers": ["자주 사용한다", "종종 사용한다", "아주 가끔 사용한다", "사용하지 않는다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "2. 회의시간에 후배가 내 의견에 반대한다면?", "answers": ["회의 끝나고 옥상으로 부른다", "나중에 은근슬쩍 꼽준다", "신경은 쓰이지만 그냥 넘어간다", "반대한 사실조차 기억하지 못한다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "3. 후배가 나보다 출근을 늦게 한다면?", "answers": ["사회생활 잘하라고 경고한다", "눈치준다", "신경은 쓰이지만 넘어간다", "별 생각없다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "4. 사생활 영역도 인생선배로서 조언해줄 수 있다", "answers": ["매우 그렇다", "그렇다", "그렇지 않다", "매우 그렇지 않다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "5. 후배들에게 배울게 있다는 말에 동의하지만 실제로 배워본적은 없다", "answers": ["매우 그렇다", "그렇다", "그렇지 않다", "매우 그렇지 않다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "6. 회식자리에서 후배가 고기를 굽지도 않고 먹기 바쁘다 당신은?", "answers": ["따로 불러서 조언을 한다", "눈치준다", "신경은 쓰이지만 넘어간다", "별 생각없다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "7. 후배의 옷차림이나 인사예절을 지적할 수 있다고 생각한다", "answers": ["매우 그렇다", "그렇다", "그렇지 않다", "매우 그렇지 않다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "8. 처음 만난 사람이 나보다 나이가 어릴 때 당신은?", "answers": ["바로 반말한다", "타이밍 보다가 자연스럽게 반말한다", "상대방 의사 들어보고 반말한다", "친해졌다고 생각이 들때 물어보고 반말한다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "9. 술자리는 반드시 참석해야한다고 생각한다", "answers": ["매우 당연하다", "특별한일이 아니면 다 참석해야한다", "정말 피곤하다면 불참해도 된다", "별 생각없다"], "points": [2, 1.5, 1, 0], "selected": -1},
            {"question": "10. 얼굴 몇번 본 후배가 밖에서 마주쳤을때 인사도 하지않고 지나갔다 당신은?", "answers": ["그자리에서 바로 꾸중한다", "나중에 따로 불러 얘기한다", "신경은 쓰이지만 그냥 넘어간다", "별생각없다"], "points": [2, 1.5, 1, 0], "selected": -1}
            
        ]

        self.create_widgets()

    def create_widgets(self):
        
        self.title_label = tk.Label(self.master, text="꼰대력 테스트", font=("Arial", 20), bg="lightcyan")
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self.master, text=f"이름: {self.name}", font=("Arial", 12), bg="lightcyan")
        self.name_label.pack(pady=10)

        self.question_label = tk.Label(self.master, text="", font=("Arial", 14), bg="lightcyan")
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for i in range(4):
            answer_button = tk.Button(self.master, text="", command=lambda idx=i: self.select_answer(idx), bg="white", relief=tk.RAISED, width=30)
            answer_button.pack(pady=5)
            self.answer_buttons.append(answer_button)

        self.next_button = tk.Button(self.master, text="다음 문제", state=tk.DISABLED, command=self.next_question, bg="lightblue", relief=tk.RAISED)
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        question = self.questions[self.question_index]
        self.question_label.configure(text=question["question"])

        for i in range(4):
            self.answer_buttons[i].configure(text=question["answers"][i], state=tk.NORMAL, bg="white")

        self.next_button.configure(state=tk.DISABLED)

    def select_answer(self, answer_index):
        question = self.questions[self.question_index]
        question["selected"] = answer_index

        for i in range(4):
            if i == answer_index:
                self.answer_buttons[i].configure(bg="skyblue")
            else:
                self.answer_buttons[i].configure(state=tk.DISABLED)

        self.next_button.configure(state=tk.NORMAL)

    def next_question(self):
        question = self.questions[self.question_index]
        self.score += question["points"][question["selected"]]
        self.question_index += 1

        if self.question_index == len(self.questions):
            self.show_result()
        else:
            self.show_question()

    def show_result(self):
        self.title_label.configure(text="테스트 결과", font=("Arial", 20))
        self.question_label.configure(text=f"{self.name}님의 총점은 {self.score}점입니다.")

        for button in self.answer_buttons:
            button.pack_forget()

        self.next_button.pack_forget()

        if self.score <= 5 :
            result_label = tk.Label(self.master, text=f"{self.name}님은 보살입니다!!", font=("Arial", 16), bg="lightcyan")
            result_label.pack(pady=20)
        elif self.score <= 10:
            result_label = tk.Label(self.master, text=f"{self.name}님은 꼰대가 아닙니다!", font=("Arial", 16), bg="lightcyan")
            result_label.pack(pady=20)
        elif self.score <= 15:
            result_label = tk.Label(self.master, text=f"{self.name}님은 꼰대일지도 모릅니다!", font=("Arial", 16), bg="lightcyan")
            result_label.pack(pady=20)
        else:
            result_label = tk.Label(self.master, text=f"{self.name}님은 누가뭐래도 꼰대입니다.", font=("Arial", 16), bg="lightcyan")
            result_label.pack(pady=20)

        self.exit_button = tk.Button(self.master, text="종료", font=('Arial', 12), command = lambda : self.master.quit())
        self.exit_button.pack(side=tk.RIGHT, pady=10,padx=5,anchor=tk.SE)
        


        self.save_result_to_file()

    def save_result_to_file(self):
        result = f"Name: {self.name}\nScore: {self.score}"
        with open("Grumpytest_result.txt", "w") as file:
            file.write(result)

    
    def open_test_select(self):
        self.master.destroy()
        from test_select import testselectApp
        testselectApp(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("꼰대력 테스트")
    root.geometry("600x400")
    root.configure(bg="lightcyan")
    app = GrumpyTestApp(root)
    root.mainloop()
