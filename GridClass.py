class Grid:

    def __init__(self, x, y, WinCount):
        self.x = x
        self.y = y
        self.WinCount = WinCount
        self.grid = [['*'] * x for _ in range(y)]
        self.dict_vertical = {
            0: 1,
            1: 0,
            2: 1,
            3: -1
        }
        self.dict_horizontal = {
            0: 0,
            1: 1,
            2: 1,
            3: 1
        }

    def printGrid(self, ):
        print(" ", end=' ')
        for i in range(self.x):
            if (i != self.x - 1):
                print(i + 1, end=' ')
            else:
                print(i + 1)

        for j in range(self.y):
            print(j + 1, end=' ')
            for i in range(self.x):
                if (i == self.x - 1):
                    print(self.grid[j][i])
                else:
                    print(self.grid[j][i], end=' ')

    def checkPlace(self, x, y):  # на вход идут значения для массива !!!!!!
        if (x >= self.x) or (x < 0):
            return 'Wrong X'
        if (y >= self.y) or (y < 0):
            return "Wrong Y"
        return self.grid[y][x]

    def changePlace(self, x, y, Xor0):  # на вход идут значения для массива !!!!!!
        if (Xor0 == True):
            self.grid[y][x] = 'X'
        else:
            self.grid[y][x] = '0'

    def checkWin(self):
        Draw = "Draw"
        for y in range(self.y):
            for x in range(self.x):
                # print(x,y)
                for i in range(4):
                    V = self.dict_vertical[i]
                    H = self.dict_horizontal[i]
                    Temp_win = 0
                    # print(i)
                    if(self.checkPlace(x, y) == '*'):
                        Draw = 'None'
                    for k in range(1, self.WinCount):
                        if (self.checkPlace(x, y) == self.checkPlace(x + (k * V), y + (H * k))) and (
                                (self.checkPlace(x, y) == 'X') or (self.checkPlace(x, y) == '0')):
                            #print(x + (k * V), y + (H * k), self.checkPlace(x + (k * V), y + (H * k)))
                            Temp_win += 1
                        else:
                            break
                    if (Temp_win == self.WinCount - 1):
                        return self.checkPlace(x, y)
        return Draw


'''
#1 проверка по горизонтали
- - - >
* * * *
* * * *
* * * *

#2 проверка по вертикали
| * * *
| * * *
| * * *
\/ * * *

#3 проверка по правой диагонали
\ * * *
* \ * *
* * \ *
* * * \/

№4 проверка по левой диагонали

* * * /
* * / *
* / * *
\/ * * *

проврка происходит так- для каждой клетки матрицы применяется все четыре пункта 

'''
