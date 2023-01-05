from tkinter import *
from random import choice
from tkinter import messagebox


def play(event):
    global wrong, so_far, max_wrong
    while wrong < max_wrong and so_far != word:
        info = str(entry.get())
        if info in word:
            new = ''
            messagebox.showinfo(title='Поздравляем!', message=f'Вы угадали букву {info}')
            for i in range(len(word)):
                if info == word[i]:
                    new += info
                else:
                    new += so_far[i]
            so_far = new
        else:
            messagebox.showerror(title='Ошибка', message=f'Буквы {info} не было в слове')
            wrong += 1


root = Tk()
HANGMAN = (
    """
         ------
         |    |
         |
         |
         |
         |
         |
        ----------
        """,
    """
         ------
         |    |
         |    O
         |
         |
         |
         |
        ----------
        """,
    """
         ------
         |    |
         |    O
         |    |
         | 
         |   
         |    
        ----------
        """,
    """
         ------
         |    |
         |    O
         |   /|
         |   
         |   
         |   
        ----------
        """,
    """
         ------
         |    |
         |    O
         |   /|\\
         |   
         |   
         |     
        ----------
        """,
    """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |   
         |    
        ----------
        """,
    """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |   
         |   
        ----------
        """
)
max_wrong = len(HANGMAN) - 1
WORDS = ("пит")

word = choice(WORDS)
so_far = "_" * len(word)
wrong = 0
used = []

label_information = Label(root, width=30, height=30, bg='bisque2')
label_information.grid(row=0, column=0)

label_stud = Label(label_information, text='Ваше текущее положение', bg='bisque2', font='Courier 15',
                   borderwidth=2, relief="groove")
label_stud.grid(row=0, column=0)

label_hangman = Label(label_information, text=HANGMAN[wrong], bg='bisque2')
label_hangman.grid(row=1, column=0)

label_word = Label(label_information, text=f'Слово - {so_far}', bg='bisque2', borderwidth=2, relief="groove",
                   font='Courier 13')
label_word.grid(row=2, column=0)

entry_info = Label(label_information, text='Введите букву', bg='bisque2', borderwidth=2, relief="groove",
                   font='Courier 15')
entry_info.grid(row=0, column=3, ipadx=100)

entry = Entry(label_information, font=12)
entry.grid(row=1, column=3)
btn_play = Button(label_information, text='Отправить', bg='bisque2', borderwidth=2, relief="groove",
                  font='Courier 15')
btn_play.grid(row=2, column=3)
btn_play.bind('<Button-1>', play)

root.mainloop()


