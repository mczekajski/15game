from random import randint, choice
from tkinter import *

class Game():

    base_grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    grid = base_grid

    def get_position(self, num):
        row = 0
        for x in self.grid:
            if num in x:
                return(row, x.index(num))
            row += 1

    def is_next_to_zero(self, num):
        if num == 0:
            return False
        num_pos = self.get_position(num)
        zero_pos = self.get_position(0)
        if abs(num_pos[0] - zero_pos[0]) == 1 and num_pos[1] - zero_pos[1] == 0:
            return True
        elif num_pos[0] - zero_pos[0] == 0 and abs(num_pos[1] - zero_pos[1]) == 1:
            return True
        else:
            return False

    def move(self, num):
        if self.is_next_to_zero(num):
            num_pos = self.get_position(num)
            zero_pos = self.get_position(0)
            self.grid[zero_pos[0]][zero_pos[1]] = num
            self.grid[num_pos[0]][num_pos[1]] = 0

    def shuffle(self, steps):
        game.move(15)
        game.move(11)
        game.move(10)
        game.move(6)
        nums_to_shuffle = []
        chosen_nums = set()
        for x in range(steps):
            for y in range(1, 16):
                if self.is_next_to_zero(y):
                    nums_to_shuffle.append(y)
            if len(chosen_nums) < 15:
                for z in range(10):
                    chosen_num = nums_to_shuffle[randint(1, len(nums_to_shuffle)) - 1]
                    if chosen_num not in chosen_nums:
                        break
            else: chosen_nums = set()
            self.move(chosen_num)
            if choice([True, False]):
                chosen_nums.add(chosen_num)

# Shuffle buttons according to the grid
def create_buttons():
    for x in range(9):
        buttons.append(Button(root, text="{}".format(x+1), bg="#99ccff", padx=35, pady=20, font="verdana", command=lambda x=x: button_click(x+1)))
    for x in range(9,15):
        buttons.append(Button(root, text="{}".format(x+1), bg="#99ccff", padx=30, pady=20, font="verdana", command=lambda x=x: button_click(x+1)))

def redraw_buttons():
    for x in range(15):
        pos = game.get_position(x+1)
        buttons[x].grid(row=pos[0], column=pos[1])

def button_click(num):
    game.move(num)
    redraw_buttons()

game = Game()
game.shuffle(5000)

root = Tk()
root.title("15 game")
root.resizable(0, 0)
root.iconbitmap('tiles.ico')

buttons = []

create_buttons()
redraw_buttons()

root.mainloop()

