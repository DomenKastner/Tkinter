# -*- coding: utf-8 -*-
import random
import Tkinter as Tk

window = Tk.Tk()
window.title("greetings______")
window.geometry("500x450")


#____Functions_________
def phrase_generator():

    phrases = ["Hello ", "What's up ", "Pozdravljen ", "Ojla ", "Hafa Adai ", "Mirëdita ", "Hei ", "Bonjour "]

    name = str(entry1.get())

    return phrases[random.randint(0, 4)] + name

def phrase_display():
    pozdrav = phrase_generator()

    # This create the text field
    pozdrav_display = Tk.Text(master=window, height=10, width=30)
    pozdrav_display.grid(column=0, row=3)

    pozdrav_display.insert(Tk.END, pozdrav)


#______Label________
label1 =Tk.Label(text="Walcome")
label1.grid(column=0, row=0)

label2 = Tk.Label(text="What is your name")
label2.grid(column=0, row=1)

#____Entry fields______
entry1 = Tk.Entry()
entry1.grid(column=1, row=1)

#____Button_____
button1 = Tk.Button(text="Click me", command=phrase_display)
button1.grid(column=0, row=2)

window.mainloop()


# Sledil predavanju na YouTubu https://www.youtube.com/watch?v=JrWHyqonGj8