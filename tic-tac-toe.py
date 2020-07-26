import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry('1350x750+0+0')
root.title('Tic Tak Toe')
root.configure(background='Cadet blue')

Tops = Frame(root, width=1350, height=100, bg='cadet blue', pady=2, relief=RIDGE)
Tops.grid(row=0, column=0)

topstitle = Label(text='Tic Tac Toe', font=('Bookman old style', 40, 'bold', 'italic'), bd=21, bg='cadet blue',
                  fg='white', justify=CENTER)
topstitle.grid(row=0, column=0)

mainframe = Frame(root, width=1350, height=600, bg='powder blue', bd=10, pady=2, relief=RIDGE)
mainframe.grid(row=1, column=0)

leftframe = Frame(mainframe, width=750, height=500, bg='cadet blue', bd=10, pady=2, relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe = Frame(mainframe, width=560, height=500, bg='cadet blue', pady=2, relief=RIDGE)
rightframe.pack(side=RIGHT)

rightframe1 = Frame(rightframe, width=560, height=200, bg='cadet blue', padx=10, pady=2, bd=10, relief=RIDGE)
rightframe1.grid(row=0, column=0)

rightframe2 = Frame(rightframe, width=560, height=200, bg='cadet blue', padx=10, pady=2, bd=10, relief=RIDGE)
rightframe2.grid(row=1, column=0)

playerx = IntVar()
player0 = IntVar()

playerx.set(0)
player0.set(0)

button = StringVar()
click = True


def Checker(button):
    global click
    if button['text'] == '' and click == True:
        button['text'] = 'X'
        click = False
    elif button['text'] == '' and click == False:
        button['text'] = '0'
        click = True


def scorekeeper():


    if (button1['text']=='X' and button2['text']=='X' and button3['text']=='X'):
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        n=float(playerx.get())
        score=(n+1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X','You have just won the match')

    if (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
        button4.configure(background='red')
        button5.configure(background='red')
        button6.configure(background='red')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'You have just won the match')

    if (button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
        button7.configure(background='blue')
        button8.configure(background='blue')
        button9.configure(background='blue')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'You have just won the match')

    if (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
        button1.configure(background='green')
        button5.configure(background='green')
        button9.configure(background='green')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'You have just won the match')

    if (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        button3.configure(background='violet')
        button5.configure(background='violet')
        button7.configure(background='violet')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'You have just won the match')

    if (button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
        button1.configure(background='pink')
        button4.configure(background='pink')
        button7.configure(background='pink')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'You have just won the match')

    if (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
        button2.configure(background='gray')
        button5.configure(background='gray')
        button8.configure(background='gray')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'You have just won the match')

    if (button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        button3.configure(background='crimson')
        button6.configure(background='crimson')
        button9.configure(background='crimson')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner X', 'You have just won the match')

    if (button1['text'] == '0' and button2['text'] == '0' and button3['text'] == '0'):
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')

    if (button4['text'] == '0' and button5['text'] == '0' and button6['text'] == '0'):
        button4.configure(background='red')
        button5.configure(background='red')
        button6.configure(background='red')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')

    if (button7['text'] == '0' and button8['text'] == '0' and button9['text'] == '0'):
        button7.configure(background='blue')
        button8.configure(background='blue')
        button9.configure(background='blue')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')

    if (button1['text'] == '0' and button5['text'] == '0' and button9['text'] == '0'):
        button1.configure(background='green')
        button5.configure(background='green')
        button9.configure(background='green')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')

    if (button3['text'] == '0' and button5['text'] == '0' and button7['text'] == '0'):
        button3.configure(background='violet')
        button5.configure(background='violet')
        button7.configure(background='violet')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')

    if (button1['text'] == '0' and button4['text'] == '0' and button7['text'] == '0'):
        button1.configure(background='pink')
        button4.configure(background='pink')
        button7.configure(background='pink')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')

    if (button2['text'] == '0' and button5['text'] == '0' and button8['text'] == '0'):
        button2.configure(background='gray')
        button5.configure(background='gray')
        button8.configure(background='gray')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')

    if (button3['text'] == '0' and button6['text'] == '0' and button9['text'] == '0'):
        button3.configure(background='crimson')
        button6.configure(background='crimson')
        button9.configure(background='crimson')
        n = float(playerx.get())
        score = (n + 1)
        playerx.set(score)
        tkinter.messagebox.showinfo('Winner 0', 'You have just won the match')


def reset():
    button1['text'] = ''
    button2['text'] = ''
    button3['text'] = ''
    button4['text'] = ''
    button5['text'] = ''
    button6['text'] = ''
    button7['text'] = ''
    button8['text'] = ''
    button9['text'] = ''

    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')


def newgame():
    reset()
    playerx.set(0)
    player0.set(0)


# marking score for player X
lblplayerx = Label(rightframe1, text='Player: X', font=('arial', 40, 'bold'), padx=2, pady=2, bg='cadet blue')
lblplayerx.grid(row=0, column=0)
textplayerx = Entry(rightframe1, font=('arial', 40, 'bold'), fg='black', bd=2, textvariable=playerx, width=14,
                    justify=LEFT).grid(row=0, column=1)

# marking score for player 0
lblplayer0 = Label(rightframe1, text='Player: 0', font=('arial', 40, 'bold'), padx=2, pady=2, bg='cadet blue')
lblplayer0.grid(row=1, column=0)
textplayer0 = Entry(rightframe1, font=('arial', 40, 'bold'), fg='black', bd=2, textvariable=player0, width=14,
                    justify=LEFT).grid(row=1, column=1)

# buttons for reset and new game
btnreset = Button(rightframe2, text='Reset', font=('arial', 26, 'bold'), height=1, width=20, bg='gainsboro', command=reset)
btnreset.grid(row=0, column=0, sticky=S + N + E + W, padx=6, pady=10)
btnnewgame = Button(rightframe2, text='New Game', font=('arial', 26, 'bold'), height=1, width=20, bg='gainsboro', command=newgame)
btnnewgame.grid(row=1, column=0, sticky=S + N + E + W, padx=6, pady=10)

button1 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(leftframe, text='', font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro',
                 command=lambda: Checker(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

root.mainloop()
