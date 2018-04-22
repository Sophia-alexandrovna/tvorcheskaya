from tkinter import *
from random import *

def paint():
    start.place(x=-100, y=-100)
    canvas.itemconfig(player,fill='yellow',outline='black')
    finish.place(x=285, y=40)
    canvas.delete('info')
    Move_laser()
    mainwindow.after(3500,Move_surprice)
    mainwindow.bind('<Motion>', Move)

def Move(event):
    global end
    if end == 0 and win == 0:
        canvas.coords(player, event.x-15, event.y-15, event.x+15, event.y+15)
        coords = canvas.coords(player)
        for i in lasers:
            las = canvas.coords(i)
            if las[1]+5 > coords[1]-15 and las[1]-5 < coords[3]+15 and ((coords[0]<las[2] and las[0]==0) or (coords[0]<las[2] and las[2]==0)):
                lose()
    

def Move_surprice():
    global win
    if win == 0:
        canvas.move(surprice1,10,0)
        canvas.move(surprice2,-10,0)
        mainwindow.after(20,Move_surprice)
        coords = canvas.coords(player)
        for i in surprices:
            sur = canvas.coords(i)
            if sur[0]+5>coords[0] and sur[0]-5<coords[2] and coords[1]<400:
                lose()

def Move_laser():
    global win
    if win == 0:
        for i in lasers:
            canvas.move(i,0,10)
        mainwindow.after(50,Move_laser)

def hide(event):
    global win
    canvas.itemconfig(player,fill='white',outline='white')
    canvas.create_text(300,400,text='Вы выиграли!',font='Arial 20', fill='green')
    finish.place(x=-200, y=-200)
    for i in surprices:
        canvas.delete(i)
    for a in lasers:
        canvas.delete(a)
    win = 1

def lose():
    global end
    canvas.itemconfig(player,fill='white',outline='white')
    canvas.create_text(300,400,text='Вы проиграли',font='Arial 20', fill='red')
    finish.place(x=-200, y=-200)
    end = 1

end = 0
win = 0
mainwindow = Tk()
mainwindow.title('Move! Fast!')
mainwindow.resizable(0,0)
canvas = Canvas(width='600', height='800', bg='white')
canvas.pack()

player = canvas.create_oval(0,30,0,30,fill='white',outline='white')
canvas.create_text(300,400,
                   text='Чтобы выиграть, вам нужно дойти до кнопки "Финиш", управляя мышью\nСтарайтесь не задеть ни одного лазера',
                   font='Arial 13', fill='black', tag='info')
start = Button(canvas,text='Старт',command=paint)
start.place(x=285, y=760)

finish = Button(canvas,text='Финиш')
finish.place(x=-200, y=-200)
finish.bind('<Motion>',hide)


pass1 = randint(0,540)
pass2 = randint(0,540)
pass3 = randint(0,540)

laser11=canvas.create_line(0,-10,pass1,-10,fill='red',capstyle='round', width='10')
laser12=canvas.create_line(pass1+100,-10,600,-10,fill='red',capstyle='round', width='10')
laser21=canvas.create_line(0,-160,pass2,-160,fill='red',capstyle='round', width='10')
laser22=canvas.create_line(pass2+100,-160,600,-160,fill='red',capstyle='round', width='10')
laser31=canvas.create_line(0,-310,pass3,-310,fill='red',capstyle='round', width='10')
laser32=canvas.create_line(pass3+100,-310,600,-310,fill='red',capstyle='round', width='10')
surprice1=canvas.create_line(-10,0,-10,400,fill='red',capstyle='round', width='10')
surprice2=canvas.create_line(610,0,610,400,fill='red',capstyle='round', width='10')

lasers = [laser11,laser12,laser21,laser22,laser31,laser32]
surprices=[surprice1,surprice2]

mainwindow.mainloop()
