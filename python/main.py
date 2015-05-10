import os

class Display():
    wall   = "|"
    bottom = "+" + "=" * 10 + "+"
    field = [[0 for i in range(10)] for j in range(20)]

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
            data = self.wall
            for j in range(10):
                cell = self.field[i][j]
                if cell == 0:
                    data += " "
                elif cell == 1:
                    data += "#"
                else:
                    data += cell
            data += self.wall
            print data
        print self.bottom


class Data():
    field = [[0 for i in range(10)] for j in range(20)]

    def DebugPrint(self):
        print self.field


if __name__ == '__main__':
    data     = Data()
    display  = Display()

    data.field[0][0] = 1
    # data.DebugPrint()

    display.Update(data.field)
    # display.DebugPrint()

    display.Print()
