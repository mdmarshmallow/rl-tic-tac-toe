from tkinter import *
import tkinter.messagebox
import numpy as np
import game_ai as ai

tk = Tk()
tk.title("Tic Tac Toe")

button_click_flag = True
state = np.full(9, 'b')


def main():

    def button_click(buttons):
        global button_click_flag, state
        if buttons["text"] == " " and button_click_flag:
            buttons["text"] = "X"
            button_click_flag = False
            index = ai.choose_move(state)
            state[index] = "O"
            button_array[index]["text"] = "O"
            button_click_flag = True
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Space already played!")

    button_array = []

    for i in range(0, 9):
        if i < 3:
            row = 1
        elif i < 6:
            row = 2
        else:
            row = 3
        button_array.append(Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8))
        button_array[i].grid(row=row, column=i % 3)

    button_array[0]["command"] = lambda: button_click(button_array[0])
    button_array[1]["command"] = lambda: button_click(button_array[1])
    button_array[2]["command"] = lambda: button_click(button_array[2])
    button_array[3]["command"] = lambda: button_click(button_array[3])
    button_array[4]["command"] = lambda: button_click(button_array[4])
    button_array[5]["command"] = lambda: button_click(button_array[5])
    button_array[6]["command"] = lambda: button_click(button_array[6])
    button_array[7]["command"] = lambda: button_click(button_array[7])
    button_array[8]["command"] = lambda: button_click(button_array[8])

    tk.mainloop()


if __name__ == "__main__":
    main()
