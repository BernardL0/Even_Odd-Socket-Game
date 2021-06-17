# Bernard Louie C. Estioco

from tkinter import *
# from client import *
import socket


root = Tk()
root.title("Even_ODD Game (A chance game)")

HOST = '127.0.0.1'
PORT = 65432

n = 0
score = 0
life = 5
x = "0"

def one(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton):
    global x
    x = '1'
    
    onebutton['bg'] = 'green'
    twobutton['bg'] = '#808080'
    threebutton['bg'] = '#808080'
    fourbutton['bg'] = '#808080'
    fivebutton['bg'] = '#808080'
    
    submitbutton['state'] = NORMAL


def two(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton):
    global x
    x = '2'

    
    onebutton['bg'] = '#808080'
    twobutton['bg'] = 'green'
    threebutton['bg'] = '#808080'
    fourbutton['bg'] = '#808080'
    fivebutton['bg'] = '#808080'
    
    submitbutton['state'] = NORMAL


def three(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton):
    global x
    x = '3'

    onebutton['bg'] = '#808080'
    twobutton['bg'] = '#808080'
    threebutton['bg'] = 'green'
    fourbutton['bg'] = '#808080'
    fivebutton['bg'] = '#808080'

    submitbutton['state'] = NORMAL


def four(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton):
    global x
    x = '4'

    onebutton['bg'] = '#808080'
    twobutton['bg'] = '#808080'
    threebutton['bg'] = '#808080'
    fourbutton['bg'] = 'green'
    fivebutton['bg'] = '#808080'

    submitbutton['state'] = NORMAL


def five(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton):
    global x
    x = '5'

    onebutton['bg'] = '#808080'
    twobutton['bg'] = '#808080'
    threebutton['bg'] = '#808080'
    fourbutton['bg'] = '#808080'
    fivebutton['bg'] = 'green'

    submitbutton['state'] = NORMAL


def numberAssign(a):
    a = str(a)
    if(a == "1"):
        return 1
    elif(a == "2"):
        return 2
    elif(a == "3"):
        return 3
    elif(a == "4"):
        return 4
    elif(a == "5"):
        return 5


def winner(a, b):

    a = int(numberAssign(a))
    b = int(numberAssign(b))
    c = a + b
    if(c % 2 == 0):
        return 0
    else:
        return 1

def restart(onebutton, twobutton, threebutton, fourbutton, fivebutton, submitbutton, lf, lifetex, texscore):
    global n
    global score
    global life
    score = 0
    n = 0
    life = 5
    lf.destroy()

    lifetex['text'] = life
    texscore['text'] = score

    onebutton['state'] = NORMAL
    twobutton['state'] = NORMAL
    threebutton['state'] = NORMAL
    fourbutton['state'] = NORMAL
    fivebutton['state'] = NORMAL
    
    onebutton['bg'] = '#808080'
    twobutton['bg'] = '#808080'
    threebutton['bg'] = '#808080'
    fourbutton['bg'] = '#808080'
    fivebutton['bg'] = '#808080'
    
    submitbutton['state'] = DISABLED


def submit(sckt,playerno,submitbutton,texscore,texsystem,lifetex, onebutton, twobutton, threebutton, fourbutton, fivebutton):
    global score
    global n
    global life
    z = 0
    
    try:
        sckt.send(str.encode(x))

        client_choice = sckt.recv(1024)
    except socket.error as e:
        print(e)
        
    
    print("Player 1: ",x, " Player 2: ", client_choice.decode())
    
    
    if(playerno == 1):
        winnerPlayer = winner(x, client_choice.decode())
    else:
        winnerPlayer = winner(client_choice.decode(), x)

    # print("Winner Player: ", winnerPlayer)

    
    # print(n,"=",n,"+",score,"+","1")
    # print("n: ", n)
    if (n % 2 == 0):
        z = 0
    else:
        z = 1
    # print("z: ", z)
    # print("Systemtext: ", n)

    
    if(winnerPlayer == z):
        score += 1
        texscore['text'] = score
    else:
        life -= 1
        lifetex['text'] = life


    if(life < 1):
        lf = Tk()
        lf.title("GAME OVER")
        lf.geometry("250x125")
        lf.protocol ('WM_DELETE_WINDOW', (lambda: 'pass') ())

        tex = Label(lf, text="You both all lost your life.")
        tex.config(font=("Courier", 10))
        tex.pack()
        tex1 = Label(lf, text="You have both of the score: ")
        tex1.config(font=("Courier", 10))
        tex1.pack()
        tex2 = Label(lf, text=score)
        tex2.config(font=("Courier", 10))
        tex2.pack()
        tex3 = Label(lf, text="Do you want to play again?")
        tex3.config(font=("Courier", 10))
        tex3.pack()

        onebutton['state'] = DISABLED
        twobutton['state'] = DISABLED
        threebutton['state'] = DISABLED
        fourbutton['state'] = DISABLED
        fivebutton['state'] = DISABLED
        submitbutton['state'] = DISABLED

        btnres = Button(lf, text="RESTART", command=lambda:restart(onebutton, twobutton, threebutton, fourbutton, fivebutton, submitbutton, lf, lifetex, texscore))
        btnres.pack()
        
        # btnno = Button(lf, text="RESTART", command=lambda:no(onebutton, twobutton, threebutton, fourbutton, fivebutton, submitbutton, lf, lifetex, texscore))
        # btnno.pack()
        
        lf.resizable(False, False)
        lf.mainloop()
        

    if(n < 10000):
        n = n + score + 1
    else:
        n = n - score + 1
    
    
    if (n % 2 == 0):
        texsystem['text'] = "EVEN"
    else:
        texsystem['text'] = "ODD"
    # print("next n: ", n)

    onebutton['state'] = NORMAL
    twobutton['state'] = NORMAL
    threebutton['state'] = NORMAL
    fourbutton['state'] = NORMAL
    fivebutton['state'] = NORMAL
    onebutton['bg'] = '#808080'
    twobutton['bg'] = '#808080'
    threebutton['bg'] = '#808080'
    fourbutton['bg'] = '#808080'
    fivebutton['bg'] = '#808080'
    submitbutton['state'] = DISABLED


def server():
    HOST = str(ip.get())
    root.quit()
    print(HOST)

    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.bind((HOST, PORT))
    s1.listen()
    clientsocket, address = s1.accept()
    root.destroy()
    
    player1 = Tk()
    player1.title("Even_Odd - Player 1")
    player1.geometry("400x200")

    scoretex = Label(player1, text="SCORE: ")
    scoretex.pack()
    scoretex.place(x=0,y=0)

    texscore = Label(player1, text="0")
    texscore.pack()
    texscore.place(x=60,y=0)

    texlife = Label(player1, text="LIFE: ")
    texlife.pack()
    texlife.config(font=("Courier", 10))
    texlife.place(x=325,y=0)

    lifetex = Label(player1, text="5")
    lifetex.pack()
    lifetex.config(font=("Courier", 10))
    lifetex.place(x=375,y=0)

    texsystem = Label(player1, text="EVEN")
    texsystem.config(font=("Courier", 15))
    texsystem.pack()
    texsystem.place(x=180,y=20)

    onebutton = Button(player1, text="One", width=7,height=2, bg='#808080', fg='white', command=lambda:one(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    onebutton.pack()
    onebutton.place(x=10,y=100)
    twobutton = Button(player1, text="Two", width=7,height=2,  bg='#808080', fg='white', command=lambda:two(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    twobutton.pack()
    twobutton.place(x=90,y=100)
    threebutton = Button(player1, text="Three", width=7,height=2, bg='#808080', fg='white', command=lambda:three(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    threebutton.pack()
    threebutton.place(x=170,y=100)
    fourbutton = Button(player1, text="Four", width=7,height=2, bg='#808080', fg='white', command=lambda:four(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    fourbutton.pack()
    fourbutton.place(x=250,y=100)
    fivebutton = Button(player1, text="Five", width=7,height=2, bg='#808080', fg='white', command=lambda:five(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    fivebutton.pack()
    fivebutton.place(x=330,y=100)
    submitbutton = Button(player1, text="Submit", width=6,height=1, state=DISABLED, command=lambda:submit(clientsocket,1,submitbutton,texscore, texsystem, lifetex, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    submitbutton.pack()
    submitbutton.place(x=345,y=165)

    player1.resizable(False, False)
    player1.mainloop()


def client():
    HOST = str(ip.get())
    root.quit()

    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((HOST, PORT))

    
    root.destroy()
    
    player2 = Tk()
    player2.title("Even_Odd - Player 2")
    player2.geometry("400x200")

    scoretex = Label(player2, text="SCORE: ")
    scoretex.pack()
    scoretex.place(x=0,y=0)

    texscore = Label(player2, text="0")
    texscore.pack()
    texscore.place(x=60,y=0)

    
    texlife = Label(player2, text="LIFE: ")
    texlife.pack()
    texlife.config(font=("Courier", 10))
    texlife.place(x=325,y=0)

    lifetex = Label(player2, text="5")
    lifetex.pack()
    lifetex.config(font=("Courier", 10))
    lifetex.place(x=375,y=0)

    texsystem = Label(player2, text="EVEN")
    texsystem.config(font=("Courier", 15))
    texsystem.pack()
    texsystem.place(x=180,y=20)


    onebutton = Button(player2, text="One", width=7,height=2, bg='#808080', fg='white', command=lambda:one(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    onebutton.pack()
    onebutton.place(x=10,y=100)
    twobutton = Button(player2, text="Two", width=7,height=2, bg='#808080', fg='white', command=lambda:two(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    twobutton.pack()
    twobutton.place(x=90,y=100)
    threebutton = Button(player2, text="Three", width=7,height=2, bg='#808080', fg='white', command=lambda:three(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    threebutton.pack()
    threebutton.place(x=170,y=100)
    fourbutton = Button(player2, text="Four", width=7,height=2, bg='#808080', fg='white', command=lambda:four(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    fourbutton.pack()
    fourbutton.place(x=250,y=100)
    fivebutton = Button(player2, text="Five", width=7,height=2, bg='#808080', fg='white', command=lambda:five(submitbutton, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    fivebutton.pack()
    fivebutton.place(x=330,y=100)
    submitbutton = Button(player2, text="Submit", width=6,height=1, state=DISABLED, command=lambda:submit(s2, 2,submitbutton, texscore, texsystem, lifetex, onebutton, twobutton, threebutton, fourbutton, fivebutton))
    submitbutton.pack()
    submitbutton.place(x=345,y=165)

    player2.resizable(False, False)
    player2.mainloop()


def instruction():
    instr = Tk()
    instr.title("INSTRUCTION of the Game Even_Odd")

    sbar = Scrollbar(instr)
    ins = Text(instr, height=11, width=75)
    sbar.pack(side=RIGHT, fill=Y)
    ins.pack(side=LEFT, fill=Y) 
    sbar.config(command=ins.yview)
    ins.config(yscrollcommand=sbar.set)
    quote = """
INSTRUCTION:
This game is a cooperative at the same time a chance game with 2 players.
That will test the 2 people who know each other.
The mechanics of the game is simple, first the system will say if it is
even or odd and both the players have 5 choice whether 1, 2, 3, 4 or 5.
When both the players have choose the two numbers will be added
to find the sum.
If the system say ODD then the sum of both the numbers choose by the
players mustbe odd if not they will lose a life. 
"""
    ins.insert(END, quote)

    instr.resizable(False, False)
    instr.mainloop()


root.geometry("355x80")
title = Label(root, text="Server IP: ")
title.pack()
title.place(x=3,y=5)
ip = Entry(root, width=45, borderwidth=5)
ip.pack()
ip.place(x=70,y=0)

# txtname = Label(root, text="Name: ")
# name = Entry(root, width=50, borderwidth=5)


hostButton = Button(root, text="Host Game", command=server)
hostButton.pack()
hostButton.place(x=3,y=40)
joinButton = Button(root, text="Join Game", command=client)
joinButton.pack()
joinButton.place(x=143,y=40)
instructionbutton = Button(root, text="Instruction", command=instruction)
instructionbutton.pack()
instructionbutton.place(x=283,y=40)

# txtname.pack()
# name.pack()

root.resizable(False, False)
root.mainloop()

# reference https://realpython.com/python-sockets/
# 