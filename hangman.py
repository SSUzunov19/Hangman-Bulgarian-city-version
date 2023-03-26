import random
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase

class Hangman:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman - Bulgarian cities version")

        file = open('words.txt', 'r')
        self.word_list = [word.strip() for word in file.readlines()]
        file.close()

        self.photos = [PhotoImage(file="images/hang{}.png".format(i)) for i in range(12)]

        self.img_label = Label(self.master)
        self.img_label.grid(row=1, column=0, columnspan=3, padx=60, pady=120)
        self.img_label.config(image=self.photos[0])

        self.lbl_word = StringVar()
        Label(self.master, textvariable=self.lbl_word, font=("Consolas 24 bold")).grid(row=1, column=3, columnspan=6, padx=10)

        self.buttons = []
        n = 0
        for c in ascii_uppercase:
            button = Button(self.master, text=c, command=lambda c=c: self.guess(c), font=("Helvetica 18"), width=7)
            button.grid(row=2+n//9, column=n%9)
            self.buttons.append(button)
            n += 1

        Button(self.master, text="New\nGame", command=self.new_game, font=("Helvetica 10 bold")).grid(row=4, column=8, sticky="NSWE")

        # add a new label to display the score
        self.score = 0
        self.score_label = Label(self.master, text="Score: {}".format(self.score), font=("Helvetica 14 bold"))
        self.score_label.grid(row=0, column=0, columnspan=9)

        self.new_game()

    def new_game(self):
        self.number_of_guesses = 0
        self.img_label.config(image=self.photos[0])
        self.the_word = random.choice(self.word_list)
        self.the_word_with_spaces = " ".join(self.the_word)
        self.lbl_word.set(" ".join("_" * len(self.the_word)))
        for button in self.buttons:
            button.config(state="normal", disabledforeground="")

    def guess(self, letter):
        if self.number_of_guesses < 11:
            txt = list(self.the_word_with_spaces)
            guessed = list(self.lbl_word.get())
            if self.the_word_with_spaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                self.lbl_word.set("".join(guessed))
                if self.lbl_word.get() == self.the_word_with_spaces:
                    messagebox.showinfo("Hangman", "You guessed it!")
                    self.score += 1
                    self.score_label.config(text="Score: {}".format(self.score))
            else:
                self.number_of_guesses += 1
                self.img_label.config(image=self.photos[self.number_of_guesses])
                if self.number_of_guesses == 11:
                    messagebox.showwarning("Hangman", "Game Over\nThe word was: " + self.the_word)
            for button in self.buttons:
                if button["text"] == letter:
                    button.config(state="disabled", disabledforeground="red")

root = Tk()
game = Hangman(root)
root.mainloop()
