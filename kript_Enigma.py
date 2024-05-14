from tkinter import *
import pyperclip

alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rotors = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO']
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

window = Tk()
window.geometry("370x260")
w = Label(window)
w.pack()

text = Text(width = 20, height = 3)
text.place(x = 10,y = 130)
lb0 = Label(text = "Текст")
lb0.place(x = 75,y = 105)

rotor_place = Entry(width = 4)
rotor_place.place(x = 150,y = 30)
lb1 = Label(text = "Порядок роторов")
lb1.place(x = 120,y = 5)

rotor_one = Entry(width = 2)
rotor_one.place(x = 135,y = 80)
rotor_two = Entry(width = 2)
rotor_two.place(x = 160,y = 80)
rotor_three = Entry(width = 2)
rotor_three.place(x = 185,y = 80)
lb1 = Label(text = "Роторы")
lb1.place(x = 150,y = 55)

text_out = Text(width = 20, height = 3)
text_out.place(x = 185,y = 130)
lb3 = Label(text = "Вывод")
lb3.place(x = 250,y = 105)

def inp():
    poryadok = str(rotor_place.get())
    rotor_1, rotor_2, rotor_3 = rotors[int(poryadok[0]) - 1], rotors[int(poryadok[1]) - 1], rotors[int(poryadok[2]) - 1]
    key_1 = int(rotor_one.get())
    key_2 = int(rotor_two.get())
    key_3 = int(rotor_three.get())
    opentxt = text.get("1.0",END)
    return rotor_1, rotor_2, rotor_3, key_1, key_2, key_3, opentxt

def onechar(rotor_1, rotor_2, rotor_3, r,v,c,one):
    rot_1 = rotor_1[(alf.find(one) + (r - 1)) % 26]

    k = alf.find(rot_1) + v - r
    if k >= 26:
        k = k % 26
    rot_2 = rotor_2[k]

    k = alf.find(rot_2) + c - v
    if k >= 26:
        k = k % 26
    rot_3 = rotor_3[k]

    ref = reflector[alf.find(rot_3) - (c - 1)]

    rot_3 = alf[rotor_3.find(alf[(alf.find(ref) + (c - 1)) % 26])]

    k = (alf.find(rot_3) - (c - v))
    if k >= 26:
        k = k % 26
    rot_2 = alf[rotor_2.find(alf[k])]

    k = alf.find(rot_2) - (v - r)
    if k >= 26:
        k = k % 26
    rot_1 = alf[rotor_1.find(alf[k])]

    out = alf[alf.find(rot_1) - (r - 1)]

    return out

def main():
    rotor_1, rotor_2, rotor_3, key_1, key_2, key_3, opentxt = inp()
    opentxt = opentxt.upper()
    out = ''
    for sim in opentxt:
        if alf.find(sim) >= 0:
            out += onechar(rotor_1, rotor_2, rotor_3, key_1, key_2, key_3, sim)
            key_1 += 1
            if key_1 > 26:
                key_1 = 0
                key_2 += 1
            if key_2 > 26:
                key_2 = 0
                key_3 += 1
            if key_3 > 26:
                key_3 = 0
        else:
            out += sim
    text_out.insert("1.0", out)

def inser():
    bufer = pyperclip.paste()
    text.insert("1.0",bufer)

def coping():
    bufer = text_out.get("1.0",END)
    pyperclip.copy(bufer)

def clearing():
    text.delete("1.0",END)
    text_out.delete("1.0",END)
    rotor_place.delete(0,END)
    rotor_one.delete(0,END)
    rotor_two.delete(0,END)
    rotor_three.delete(0, END)

b0 = Button(text = "Вставить текст",width = 13, height = 1)
b0.config(command = inser)
b0.place(x = 130,y = 200)

b1 = Button(text = "Копировать вывод",width = 15, height = 1)
b1.config(command = coping)
b1.place(x = 10,y = 200)

b2 = Button(text = "Очистка полей",width = 15, height = 1)
b2.config(command = clearing)
b2.place(x = 235,y = 200)

b3 = Button(text = "Выполнить",width = 13, height = 1)
b3.config(command = main)
b3.place(x = 130,y = 230)

window.mainloop()

