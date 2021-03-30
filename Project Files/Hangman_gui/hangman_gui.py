from tkinter import *
import random
def hangman():
    restart_var = True
    while restart_var:
        counter = 0
        ans = ''
        def confirmAnswer(ans,guessing_word_input):
            global answer
            answer = (guessing_word_input.get()).upper()
            first_window.destroy()
        def soloPlay():
            random_word_list = ['HEMANTH','PYTHON','CODING','MOUSE','CLAIN','RADIO','MANJU','BURGER','MUSIC','HANGMAN','CRICKET','SMARTPHONE','CAMERA','SCHOOL', 'COLLEGE','EXERCISE']
            random.shuffle(random_word_list)
            global answer
            answer = random_word_list[0]
            first_window.destroy()

        first_window = Tk()
        first_window.title('Enter Word')
        first_window.resizable(False,False)

        enter_word_label = Label(text = 'Enter Guessing Word (letters only, spaces allowed) : ')
        enter_word_label.pack()

        guessing_word_input = Entry(first_window,show = '*',width = (50))
        guessing_word_input.pack(side = LEFT)

        confirm_guess_button = Button(text = 'Enter',command = (lambda: confirmAnswer(ans,guessing_word_input)))
        confirm_guess_button.pack(side = LEFT)

        solo_play_button = Button(text = 'Solo',command = soloPlay)
        solo_play_button.pack(side = RIGHT)

        first_window.mainloop()

        window = Tk()
        window.geometry('800x600')
        window.title('Hangman')
        window.resizable(False,False)
        answerList = []

        for i in answer:
            answerList.append(i)

        revealing_ans = []
        for i in range(len(answerList)):
            if answerList[i]!=' ':
                revealing_ans += '*'
            else:
                revealing_ans += '/'
        print(revealing_ans)

        revealing_ans_label = Label(text= revealing_ans,font = (None,50))
        revealing_ans_label.pack()
        print(len(revealing_ans),' letters\n')

        exit_button = Button(text = 'EXIT',command = exit)
        exit_button.place(x = 20,y =20)

        hangman_canvas = Canvas(window,width = 400,height = 400,)
        hangman_canvas.place(x=200,y=70)

        class turn:
            def __init__(self,num):
                self.num = num

            def lifeLost(self):
                self.num -=1
            
            def turn(self):
                self.num += 1

        lifenum = turn(8)
        life_label_text = 'Lives: ' + str(lifenum.num)
        life_label = Label(text = life_label_text,font = (None, 20),foreground = 'red')
        life_label.place(x = 650,y = 50)

        num_of_turns = turn(0)
        num_of_turns_text = 'Turns: ' + str(num_of_turns.num)
        num_of_turns_label = Label(text = num_of_turns_text,font = (None, 20))
        num_of_turns_label.place(x = 650,y = 100)

        class button:
            def __init__(self,letter,button):
                num_of_turns.turn()
                num_of_turns_text = 'Turns: ' + str(num_of_turns.num)
                num_of_turns_label.config(text = num_of_turns_text)
                self.letter = letter
                self.button = button
                button.config(state = 'disabled',disabledforeground = 'red2')
                print(letter)
                counter =0
                #check for letter
                for i in range(len(answerList)):
                    if letter == answerList[i]:
                        revealing_ans[i]=answerList[i]
                        counter += 1
                if counter > 0:
                    print('Correct')

                    revealing_ans_label.config(text = revealing_ans)

                    if '*' not in revealing_ans:
                        endGame()
                else:
                    print('Wrong')
                    lifenum.lifeLost()
                    life_label_text = 'Lives: ' + str(lifenum.num)
                    life_label.config(text = life_label_text)

                    if lifenum.num == 7:
                        hangman_canvas.create_line(0,300,80,300)
                    if lifenum.num == 6:
                        shape2 = hangman_canvas.create_line(40,40,40,300)
                    if lifenum.num == 5:
                        shape3 = hangman_canvas.create_line(0,40,300,40)
                    if lifenum.num == 4:
                        shape4 = hangman_canvas.create_line(300,40,300,100)
                    if lifenum.num == 3:
                        shape5 = hangman_canvas.create_oval(260,100,340,180)
                    if lifenum.num == 2:
                        shape6 = hangman_canvas.create_line(300,180,300,260)
                    if lifenum.num == 1:
                        shape7 = hangman_canvas.create_line(280,220,300,200,320,220)
                    if lifenum.num == 0:
                        shape8 = hangman_canvas.create_line(280,280,300,260,320,280)
                        endGame()
                

        def endGame():
            print(answer)
            window.destroy()
            final_window = Tk()
            final_window.title('GAME ENDED')
            final_message = Label(text = 'GAME ENDED')
            final_message.pack()
            answer_label = Label(final_window,text= answer,font = (None,50))
            if lifenum.num == 0:
                answer_label.config(foreground = 'red')
            else:
                answer_label.config(foreground = 'green')
            answer_label.pack()
            exit_button_end = Button(final_window,text = 'EXIT',command = (lambda: exit()))
            exit_button_end.pack()

            play_again_button = Button(text = 'Play Again',command = final_window.destroy)
            play_again_button.pack()

        button_frame = Frame()
        button_frame.place(x=0, y = 500)

        buta = Button(button_frame,text = 'A',command =(lambda: button('A',buta)),width = 3)
        buta.pack(side = LEFT)
        butb = Button(button_frame,text = 'B',command =(lambda: button('B',butb)),width = 3)
        butb.pack(side = LEFT)
        butc = Button(button_frame,text = 'C',command =(lambda: button('C',butc)),width = 3)
        butc.pack(side = LEFT)
        butd = Button(button_frame,text = 'D',command =(lambda: button('D',butd)),width = 3)
        butd.pack(side = LEFT)
        bute = Button(button_frame,text = 'E',command =(lambda: button('E',bute)),width = 3)
        bute.pack(side = LEFT)
        butf = Button(button_frame,text = 'F',command =(lambda: button('F',butf)),width = 3)
        butf.pack(side = LEFT)
        butg = Button(button_frame,text = 'G',command =(lambda: button('G',butg)),width = 3)
        butg.pack(side = LEFT)
        buth = Button(button_frame,text = 'H',command =(lambda: button('H',buth)),width = 3)
        buth.pack(side = LEFT)
        buti = Button(button_frame,text = 'I',command =(lambda: button('I',buti)),width = 3)
        buti.pack(side = LEFT)
        butj = Button(button_frame,text = 'J',command =(lambda: button('J',butj)),width = 3)
        butj.pack(side = LEFT)
        butk = Button(button_frame,text = 'K',command =(lambda: button('K',butk)),width = 3)
        butk.pack(side = LEFT)
        butl = Button(button_frame,text = 'L',command =(lambda: button('L',butl)),width = 3)
        butl.pack(side = LEFT)
        butm = Button(button_frame,text = 'M',command =(lambda: button('M',butm)),width = 3)
        butm.pack(side = LEFT)
        butn = Button(button_frame,text = 'N',command =(lambda: button('N',butn)),width = 3)
        butn.pack(side = LEFT)
        buto = Button(button_frame,text = 'O',command =(lambda: button('O',buto)),width = 3)
        buto.pack(side = LEFT)
        butp = Button(button_frame,text = 'P',command =(lambda: button('P',butp)),width = 3)
        butp.pack(side = LEFT)
        butq = Button(button_frame,text = 'Q',command =(lambda: button('Q',butq)),width = 3)
        butq.pack(side = LEFT)
        butr = Button(button_frame,text = 'R',command =(lambda: button('R',butr)),width = 3)
        butr.pack(side = LEFT)
        buts = Button(button_frame,text = 'S',command =(lambda: button('S',buts)),width = 3)
        buts.pack(side = LEFT)
        butt = Button(button_frame,text = 'T',command =(lambda: button('T',butt)),width = 3)
        butt.pack(side = LEFT)
        butu = Button(button_frame,text = 'U',command =(lambda: button('U',butu)),width = 3)
        butu.pack(side = LEFT)
        butv = Button(button_frame,text = 'V',command =(lambda: button('V',butv)),width = 3)
        butv.pack(side = LEFT)
        butw = Button(button_frame,text = 'W',command =(lambda: button('W',butw)),width = 3)
        butw.pack(side = LEFT)
        butx = Button(button_frame,text = 'X',command =(lambda: button('X',butx)),width = 3)
        butx.pack(side = LEFT)
        buty = Button(button_frame,text = 'Y',command =(lambda: button('Y',buty)),width = 3)
        buty.pack(side = LEFT)
        butz = Button(button_frame,text = 'Z',command =(lambda: button('Z',butz)),width = 3)
        butz.pack(side = LEFT)
        window.mainloop()
hangman()
