from tkinter import *
import anime_data


class AnimeGraphic:

    def __init__(self):
        self.submit_button = None
        self.submit_box = None
        self.name = str
        self.banner = None
        self.screen = Tk()

    def app(self):
        self.screen.config(width=1280, height=720)
        self.submit_button = Button(text="Submit", width=20 , command=self.lable)
        self.submit_box = Entry()
        self.submit_box.place(x=610, y=300, width=300)
        self.submit_button.place(x=640, y=360)
        self.screen.mainloop()
        return self.submit_box

    def lable(self):
        self.banner = Label(text=self.submit_box.get(), width=30)
        self.banner.place(y=30, x=600)
        self.name = self.submit_box.get()
        print(self.name)
        print(anime_data.anime(self.name))




