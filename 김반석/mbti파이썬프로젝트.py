import tkinter as tk
import tkinter.messagebox as messagebox
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
        root.geometry("900x500")
        self.a_button.pack_forget()
        self.b_button.pack_forget()
        self.question_label.pack_forget()
        image_mbti_1=tk.PhotoImage(file=mbti_type+'파이썬.png')
        image_label_1=tk.Label(root,image=image_mbti_1)
        image_label_1.pack(side='left')
        if mbti_type[1:3]=='NT':
            root.configure(bg='#E8D8E0')
            right_label=tk.Label(root,text)
        if mbti_type[1:4:2]=='SJ':
            root.configure(bg='#CDE6E7')
        if mbti_type[1:3]=='NF':
            root.configure(bg='#EBEEE6')
        if mbti_type[1:4:2]=='SP':
            root.configure(bg='#F7E7CB')
        image_mbti_2=tk.PhotoImage(file='mbti파이썬.png')
        image_label_2=tk.Label(root,image=image_mbti_2)
        image_label_2.pack(side='right')
        root.mainloop()

    def select_option(self,option):
        self.add_response(option)
        print(option)
        if len(self.responses) == len(self.questions)/2:
            mbti_type = self.calculate_type()
            print(mbti_type)
            self.display_mbti_type(mbti_type)
        else:
            self.question_label.configure(text=self.questions[2*len(self.responses)])
            self.index=len(self.responses)
            self.a_button.configure(command= lambda: test.select_option(self.questions[self.index*2+1][0]))
            self.b_button.configure(command= lambda: test.select_option(self.questions[self.index*2+1][1]))
        print(len(responses))
        print(len(questions))
        print(self.index)
    def start_test(self):
        intro_label.pack_forget()
        start_button.pack_forget()
        self.question_label = tk.Label(root,text=questions[0],font=('Corbel',12))
        self.question_label.pack(pady=50)
        self.a_button = tk.Button(root, text="a) 동의", command= lambda: self.select_option("e"))
        self.a_button.pack(pady=20)
        self.b_button = tk.Button(root, text="b) 비동의", command= lambda: self.select_option("i"))
        self.b_button.pack(pady=20)

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
]
responses = []
test = MBTI_Test(questions,responses)
intro_label=tk.Label(root,text=intro_text,bg='#CC8272',font=('sitka text',12))
intro_label.pack(pady=50)
start_button=tk.Button(root,text='시작',width=9,height=3,relief='groove',overrelief='sunken',bg='#A79E7A'
,font=('BIZ UDPGothic',12),command=lambda: test.start_test())
start_button.pack(pady=10)


'''question_label = tk.Label(root,text=questions[0])
question_label.pack(pady=20)
a_button = tk.Button(root, text="a) 동의", command= lambda: test.select_option("e"))
a_button.pack(pady=20)
b_button = tk.Button(root, text="b) 비동의", command= lambda:test.select_option("i"))
b_button.pack(pady=20)'''
'''if test.index==1:
    c_button = tk.Button(root, text="c) 동의", command=lambda: test.select_option("c"))
    c_button.pack(pady=20)
    d_button = tk.Button(root, text="d) 비동의", command=lambda: test.select_option("d"))
    d_button.pack(pady=20)
if test.index==2:
    e_button = tk.Button(root, text="e) 동의", command=lambda: test.select_option("e"))
    e_button.pack(pady=20)
    f_button = tk.Button(root, text="f) 비동의", command=lambda: test.select_option("f"))
    f_button.pack(pady=20)
if test.index==3:
    g_button = tk.Button(root, text="g) 동의", command=lambda: test.select_option("g"))
    g_button.pack(pady=20)
    h_button = tk.Button(root, text="h) 비동의", command=lambda: test.select_option("h"))
    h_button.pack(pady=20)'''
'''root.mainloop()'''
