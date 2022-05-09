import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    original_data = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_word['French'], fill='black')
    canvas.itemconfig(background_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(background_image, image=card_back_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_word['English'], fill='white')


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()
# -----------------User Interface------------------------- #


window = tkinter.Tk()
window.title('Flashy')
flip_timer = window.after(3000, func=flip_card)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file='images/card_front.png')
card_back_image = tkinter.PhotoImage(file='images/card_back.png')
background_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))

unknown_btn_image = tkinter.PhotoImage(file='images/wrong.png')
unknown_btn = tkinter.Button(image=unknown_btn_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

known_btn_image = tkinter.PhotoImage(file='images/right.png')
known_btn = tkinter.Button(image=known_btn_image, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)
next_card()
window.mainloop()
