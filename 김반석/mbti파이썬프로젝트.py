import tkinter as tk
import tkinter.messagebox as messagebox
import pandas as pd
class MBTI_Test:
    def __init__(self,questions,responses):
        self.questions = questions
        self.responses = responses
        self.index=0
    def add_response(self, response):
        self.responses.append(response)
        
    def calculate_type(self):
        traits = {
            "E": 0,
            "I": 0,
            "S": 0,
            "N": 0,
            "T": 0,
            "F": 0,
            "J": 0,
            "P": 0
        }

        for response in self.responses:
            if response == "e":
                traits["E"] += 1
            elif response == "i":
                traits["I"] += 1
            elif response == "s":
                traits["S"] += 1
            elif response == "n":
                traits["N"] += 1
            elif response == "t":
                traits["T"] += 1
            elif response == "f":
                traits["F"] += 1
            elif response == "j":
                traits["J"] += 1
            elif response == "p":
                traits["P"] += 1

        mbti_type = ""

        if traits["E"] > traits["I"]:
            mbti_type += "E"
        else:
            mbti_type += "I"

        if traits["S"] > traits["N"]:
            mbti_type += "S"
        else:
            mbti_type += "N"

        if traits["T"] > traits["F"]:
            mbti_type += "T"
        else:
            mbti_type += "F"

        if traits["J"] > traits["P"]:
            mbti_type += "J"
        else:
            mbti_type += "P"

        return mbti_type

    def display_mbti_type(self,mbti_type):
        messagebox.showinfo("MBTI 테스트결과", f"당신의 mbti 성격 유형은 {mbti_type}입니다!")
        root.geometry("940x600")
        self.a_button.pack_forget()
        self.b_button.pack_forget()
        self.question_label.pack_forget()
        image_mbti_1=tk.PhotoImage(file=mbti_type+'파이썬.png')
        image_label_1=tk.Label(root,image=image_mbti_1)
        image_label_1.grid(row=1,column=0)
        if mbti_type[1:3]=='NT':
            root.configure(bg='#E8D8E0')
        if mbti_type[1:4:2]=='SJ':
            root.configure(bg='#CDE6E7')
        if mbti_type[1:3]=='NF':
            root.configure(bg='#EBEEE6')
        if mbti_type[1:4:2]=='SP':
            root.configure(bg='#F7E7CB')
        image_mbti_2=tk.PhotoImage(file='mbti파이썬.png')
        image_label_2=tk.Label(root,image=image_mbti_2)
        image_label_2.grid(row=1,column=1)
        age_label=tk.Label(root,text=self.mental_age(),font=('Corbel',15))
        age_label.grid(row=0,column=0,columnspan=10)
        exit_button = tk.Button(root, text="종료", font=('Arial', 12),width=10,height=2, command = lambda : self.quit())
        exit_button.grid(row=2,column=1,columnspan=10)
        root.mainloop()
        
    def mental_age(self):
                mbti_age = {
            'ISTJ': (25, 75),
            'ISFJ': (60, 70),
            'INFJ': (60, 100),
            'INTJ': (50, 60),
            'ISTP': (20, 25),
            'ISFP': (23, 60),
            'INFP': (6, 60),
            'INTP': (5, 40),
            'ESTP': (15, 20),
            'ESFP': (15, 17),
            'ENFP': (21, 80),
            'ENTP': (10, 38),
            'ESTJ': (22, 45),
            'ESFJ': (25, 35),
            'ENFJ': (9, 38),
            'ENTJ': (20, 52)
            }
                age_range = mbti_age.get(self.calculate_type())
                if self.age() >= age_range[0] and self.age() <= age_range[1]:
                     return "{}유형의 평균 정신연령과 실제 나이가 비슷하네요~".format(self.calculate_type())
                elif self.age() < age_range[0]:
                     return "{}유형의 평균 정신연령보다 더 어리게 사시네요~".format(self.calculate_type())
                else:
                     return "{}유형의 평균 정신연령보다 더 늙게 사시네요~".format(self.calculate_type())
        

    def select_option(self,option):
        self.add_response(option)
        if len(self.responses) == len(self.questions)/2:
            mbti_type = self.calculate_type()
            self.display_mbti_type(mbti_type)
        else:
            self.question_label.configure(text=self.questions[2*len(self.responses)])
            self.index=len(self.responses)
            self.a_button.configure(command= lambda: test.select_option(self.questions[self.index*2+1][0]))
            self.b_button.configure(command= lambda: test.select_option(self.questions[self.index*2+1][1]))
    def start_test(self):
        intro_label.pack_forget()
        start_button.pack_forget()
        self.question_label = tk.Label(root,text=questions[0],font=('Corbel',12))
        self.question_label.pack(pady=50)
        self.a_button = tk.Button(root, text="a) 동의",bg='#CC8272', command= lambda: self.select_option("e"))
        self.a_button.pack(pady=20)
        self.b_button = tk.Button(root, text="b) 비동의",bg='#CC8272', command= lambda: self.select_option("i"))
        self.b_button.pack(pady=20)
    def age(self):
        self.user_data = pd.read_excel('user_data.xlsx')
        self.user_age = self.user_data['Age'][0]
        return self.user_age
    def quit(self):
        exit()
root = tk.Tk()
root.title("MBTI Test")
root.configure(bg='#72CC82')
root.geometry("400x400")
intro_text='MBTI는 Myers-Briggs Type indicator의 약자로\n\
   사람의 심리유형을 16가지로 분류해서 나타내는\n\
   검사입니다. Myers와 Briggs가 Carl Gustav Jung의\n\
   심리학적 유형 이론을 근거로 만든 성격 검사입니다.\n\
   자신의 성격, 적성, 대인관계 등 자신에 대한 \n\
   정보들을 알 수 있고 쉽게 자신의 성격을 표현할 수\n\
   있기에 최근에 인기가 있는 검사 중 하나입니다.'
questions = [
    "1. 나에게 새로운 친구를 만드는것은 쉬운 일이다",['e','i'] #e
    ,"2. 자유시간을 다양한 관심사를 찾는데 사용한다",['n','s'] #n
    ,"3. 다급하거나 힘든 상황에도 평정심을 유지하려고 노력한다",['t','f'] #t
    ,"4. 일이나 공부를 대비해 여러 계획을 세우려고 한다",['j','p'] #j
    ,"5. 혼자시간을 보내도 심심하지 않은 편이다",['i','e'] #i
    ,"6. 영화에 대한 감상이나 토론을 하는일에는 관심이 없다",['s','n'] #s
    ,"7. 나는 스스로 어떠한 감성을 즐긴다고 생각한다",['f','t'] #f
    ,"8. 하나의 일을 완전히 끝내고 다른 일을 시작한다",['j','p'] #j
    ,"9. 어떤 사람에게 관심이 생기면 \n먼저 다가가서 대화를 시작하는 편이다",['e','i'] #e
    ,"10. 열린 결말처럼 창작물을 \n자신의 방식대로 해석하는것을 좋아한다",['n','s'] #n
    ,"11. 자신보다 남의 일에 도움을 주는것에 \n더 만족감을 느낀다",['f','t'] #f
    ,"12. 삶의 만족은 내가 즉흥적으로 \n하고 싶은 일을 하는것에서 온다",['p','j']# p
    ,"13. 단체활동에 참여하는 일을 즐긴다 ",['e','i'] #e
    ,"14. 체험을 하며 이론을 먼저 듣는거 보다 \n먼저 해보며 느끼고 싶다",['s','n'] #s
    ,"15. 자신과 삶의 배경이 다른 사람의 삶은 \n공감하지 못하는 것이 당연하다",['t','f'] #t
    ,"16. 일을 할때 절차나 규칙을 지키는 것보다 \n내가 어느정도 스스로 판단해서 진행하는게 좋다 ",['p','j']# p
    ,"17. 혼자만의 시간을 가지는 것은 친구들을 \n만나서 노는것 만큼 중요하다",['i','e']#i
    ,"18. 미술관이나 박물관을 가는 것은 \n재미있는 일이다.",['n','s']#n
    ,"19. 자신만큼 이성적이지 못한 사람을 보면 \n짜증이 난다",['t','f']#t
    ,"20. 이미 내린 결정에 대해서는 다시 \n생각하지 않는 편이다",['j','p']#j
    ,"21. 나는 많은 시간을 혼자서 일할 수 있는\n 직업을 선호한다.",['i','e']#i
    ,"22. 철학적인 질문에 대해 깊게 생각하고 \n이야기하는 것은 재미있는 일이라고 생각한다.",['n','s']#n
    ,"23. 나는 상대방의 감정을 쉽게 알아차리고 \n그것을 이야기 할때 고려하는 편이다.",['f','t']#f
    ,"24. 나는 마감 기한을 지키기 어려울때가 자주있다",['p','j']#p
    ,"25. 나는 친구에게 먼저 만나자고 연락하는 편이다",['e','i']#e
    ,"26. 나는 오래전의 실수가 떠올라 후회할 때가 많다",['n','s']#n
    ,"27. 나는 논란이 되거나 논쟁을 불러일으킬 수 있는\n 주제에 관심이 많다",['t','f']#t
    ,"28. 나는 일이 원하는 대로 진행될 것이라는\n 자신감이 부족하다고 생각한다",['p','j']#p
]
responses = []
test = MBTI_Test(questions,responses)
intro_label=tk.Label(root,text=intro_text,font=('sitka text',12))
intro_label.pack(pady=50)
start_button=tk.Button(root,text='시작',width=9,height=3,relief='groove',overrelief='sunken',bg='#A79E7A'
,font=('BIZ UDPGothic',12),command=lambda: test.start_test())
start_button.pack(pady=10)
