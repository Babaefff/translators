import random

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
from random import choice

first_card={}
dict={}
try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("tr.csv/tr - Sayfa1.csv")
    dict=original_file.to_dict(orient='records')
else:
    dict = file.to_dict(orient="records")




def generate_word_wrong():
    global first_card,flip_timer
    window.after_cancel(flip_timer)
    first_card = choice(dict)

    canvas.itemconfig(french_text, text="Turkish",fill="black")
    canvas.itemconfig(english_text, text=first_card["Turkish"],fill="black")
    canvas.itemconfig(canvas_image,image=front)
    flip_timer=window.after(3000, flip_cards)



def  generate_word_right():
    generate_word_wrong()

    dict.remove(first_card)
    datas=pandas.DataFrame(dict)
    datas.to_csv("data/words_to_learn.csv",index=False)



def flip_cards():

    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(french_text, fill="white")
    canvas.itemconfig(english_text, fill="white")
    canvas.itemconfig(french_text,text="English")
    canvas.itemconfig(english_text,text=first_card["English"])



window=Tk()
window.title("Translator")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, flip_cards)



canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front=PhotoImage(file="images/card_front.png")
back=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,263,image=front,)
french_text=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
english_text=canvas.create_text(400,263,text=f"word",font=("Ariel",60,"bold"))
canvas.grid(column=1,row=1,columnspan=2)


right = PhotoImage(file="images/right.png")
button1 = Button(image=right, highlightthickness=0,command=generate_word_right)
button1.grid(column=2,row=2)
wrong = PhotoImage(file="images/wrong.png")
button2 = Button(image=wrong, highlightthickness=0,command=generate_word_wrong)
button2.grid(column=1,row=2)
generate_word_wrong()



window.mainloop()

