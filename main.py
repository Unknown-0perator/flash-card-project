import tkinter
BACKGROUND_COLOR = "#B1DDC6"


# -----------------User Interface------------------------- #
window = tkinter.Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

unknown_btn_image = tkinter.PhotoImage(file='images/wrong.png')
unknown_btn = tkinter.Button(image=unknown_btn_image, highlightthickness=0)
unknown_btn.grid(row=1, column=0)

known_btn_image = tkinter.PhotoImage(file='images/right.png')
known_btn = tkinter.Button(image=known_btn_image, highlightthickness=0)
known_btn.grid(row=1, column=1)
window.mainloop()
