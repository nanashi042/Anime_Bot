from tkinter import *


class AnimeGraphic:

    def __init__(self):
        self.submit_button = None
        self.screen = Tk()


    def app(self):
        self.screen.config(width=1280, height=720)
        self.submit_button = Button(text="Submit", width=20)
        self.submit_button.place(x=640, y=360)
        self.screen.mainloop()



screen = AnimeGraphic()

screen.app()
