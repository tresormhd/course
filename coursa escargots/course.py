# La course d'excargots
 
from tkinter import *
from time import sleep
from random import randint
from tkinter.messagebox import *

solde = 1000



def go():
    global x1, x2, x3, x4
    y = 1000
    while x1<960 and x2<960 and x3<960 and x4<960:
        no = randint(1, 4)
        if no==1:
            x1 += 1
            can.coords(esca1, x1, y1)
            y = y1
        elif no== 2:
            x2 += 1
            can.coords(esca2, x2, y2)
            y = y2
        elif no== 3:
            x3 += 1
            can.coords(esca3, x3, y3)
            y = y3
        else:
            x4 += 1
            can.coords(esca4, x4, y4)
            y = y4
        sleep(0.01)  # délai de 1/100 de secondes
        can.update()
    can.coords(vainqueur, 500, y)


def lecture():
    affichage['text'] = lecture.get()


def pari():
    window=Tk()

    mise1 = IntVar()
    choix1= IntVar()

    window.title('faire un pari')
    window.geometry('700x500')
    frame = Frame(window)
    #canvas = canvas(window, width=800, height=600, bg='silver')
    salutation= Label(frame, text='bienvenu joueur1', font=("Helvetica",20))
    salutation.pack()

    salutation = Label(frame, text='vous avez un solde predefini de 1000 $', font=("Helvetica", 20))
    salutation.pack()

    #labe_solde = Label(frame, text='entrez votre mise  ',font=("Helvetica",15))
    #labe_solde.pack()
   # mise= Spinbox(frame, textvariable=mise1, from_=100,to=1000,width=10)
    #mise.pack()
    label_choix_vainqueur=Label(frame, text='choisi votre jocket',font=("Helvetica",15))
    label_choix_vainqueur.pack()
    choix = Spinbox(frame, textvariable=choix1, from_=1, to=4, width=10)
    choix.pack()
    choix = choix.get()
    btn=Button(window, text ='Partez !', width=15, command=go)
    #btn.grid(row=2,column=5)
    btn.pack(side=BOTTOM)



    # afficher la frame
    frame.pack(expand=YES)
    right_frame.grid(row=0, column=1,sticky=w)


#fonction pour reinisaliser la course
def reinit():
    global x1, x2, x3, x4, y1, y2, y3, y4

    x1, y1  = 130, 75
    x2, y2  = 130, 225
    x3, y3  = 130, 375
    x4, y4  = 130, 525
    can.coords(esca1, x1, y1)
    can.coords(esca2, x2, y2)
    can.coords(esca3, x3, y3)
    can.coords(esca4, x4, y4)
    can.coords(vainqueur, 200, 800)

x1, y1  = 130, 75
x2, y2  = 130, 225
x3, y3  = 130, 375
x4, y4  = 130, 525
#fenetre principale


fen = Tk()
fen.title("Course d'escargots")
can = Canvas(fen, width=1100, height=600, bg ='white')
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(fen, text ='Nouvelle course', width=15, command=reinit)
b1.pack(side=LEFT)
b2 = Button(fen, text ='Partez !', width=15, command=go)
b2.pack(side=LEFT)
b3 = Button(fen, text = 'parier !', width=15, command=pari)
b3.pack(side=LEFT)
b4 = Button(fen, text ='Quitter', width=15, command=fen.quit)
b4.pack(side=RIGHT)

# décor
can.create_line(1080, 0, 1080, 600, width=5, fill="red")
can.create_line(250, 0, 250, 600, width=5, fill="green")
can.create_line(0, 150, 1100, 150, width=5, fill="black")
can.create_line(0, 300, 1100, 300, width=5, fill="black")
can.create_line(0, 450, 1100, 450, width=5, fill="black")

# images
photo1 = PhotoImage(file ='escargot1.gif')
esca1 = can.create_image(x1, y1, image=photo1)
photo2 = PhotoImage(file ='escargot2.gif')
esca2 = can.create_image(x2, y2, image=photo2)
photo3 = PhotoImage(file ='escargot3.gif')
esca3 = can.create_image(x3, y3, image=photo3)
photo4 = PhotoImage(file ='escargot4.gif')
esca4 = can.create_image(x4, y4, image=photo4)
photo5 = PhotoImage(file ='vainqueur.gif')
vainqueur = can.create_image(200, 800, image=photo5) # en dehors de l'image

fen.mainloop()
fen.destroy()

