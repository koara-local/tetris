import os
import time

class ColorEnum():
    GREEN   = '\033[32m'
    RED     = '\033[31m'
    YELLOW  = '\033[33m'
    ORANGE  = '\033[1;31m'
    BLUE    = '\033[34m'
    SKYBLUE = '\033[36m'
    PURPLE  = '\033[35m'
    DEFAULT = '\033[0m'

class Cell():
    def __init__(self, num=0, color=ColorEnum().DEFAULT):
        self.num   = num
        self.color = color

class Display():
    left_offset  = " " * 10
    wall = "|"
    bottom = "+" + "=" * 10 + "+"
    field = [[Cell() for i in range(10)] for j in range(20)]

    def __init__(self):
        return

    def _ClearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def DebugPrint(self):
        print self.field

    def Update(self, field):
        self.field = field

    def Print(self):
        # clear screen
        self._ClearScreen()
        # print all cell and frame
        for i in range(20):
            data = self.left_offset + self.wall
            for j in range(10):
                cell = self.field[i][j]
                if cell.num == 0:
                    data += " "
                elif cell.num == 1:
                    data += cell.color + "#" + ColorEnum().DEFAULT
                else:
                    data += cell.num
            data += self.wall
            print data
        print self.left_offset + self.bottom

class Data():
    field = [[Cell() for i in range(10)] for j in range(20)]

    block = [[Cell(1, ColorEnum.YELLOW), Cell(1, ColorEnum.YELLOW)],
             [Cell(1, ColorEnum.YELLOW), Cell(1, ColorEnum.YELLOW)]]

    pos_x = 0
    pos_y = 0

    def DebugPrint(self):
        print self.field

    def Next(self):
        next_field = self.field

        next_field[self.pos_y][self.pos_x] = self.block[0][0]

        if self.pos_y == 19:
            self.pos_y = 0
        else:
            self.pos_y += 1

        return next_field


if __name__ == '__main__':
    data     = Data()
    display  = Display()

    for i in range(40):
        display.Update(data.Next())
        display.Print()
        time.sleep(0.33)
