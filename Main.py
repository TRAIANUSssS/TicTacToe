from PlayerClass import Player as p
from GridClass import Grid as g


def welcome():
    print('Добро пожаловать в игру крестики нолики')
    print('Введите имя первого игрока')
    palyer1 = p(input(), True)
    print('ВВедите имя второго игрока')
    palyer2 = p(input(), False)
    return (palyer1, palyer2, createGrid())


def createGrid():
    print('Введите размеры поля(ширину и высоту, через пробел)')
    x, y = map(int, input().split())
    if (x <= 2) or (y <= 2):
        print('У вас не выйдет поиграть, введите нормальное значение')
        while (x <= 2) or (y <= 2):
            print('Введите значения по нововой')
            x, y = map(int, input().split())
    if (min(x, y) == 3):
        c = 3
    elif (min(x, y) == 4):
        c = 4
    else:
        c = 5
    print('Введите сколько клеточек должно быть в ряд, чтобы победить. Рекомендуемое значение:', c)
    c = int(input())
    if (c <= 2) or (c > max(x, y)):
        while (c <= 2) or (c > max(x, y)):
            print('Введите корректное значение')
            c = int(input())

    return g(x, y, c)


def Play(p1, p2, grid):
    if (p1.move == True):
        name = p1.name
    else:
        name = p2.name
    print('Ход игрока', name, "введите через пробел координату х(по горизонтали) и y(по вертикали)")
    x, y = map(int, input().split())
    if grid.checkPlace(x - 1, y - 1) != '*':
        while grid.checkPlace(x - 1, y - 1) != '*':
            print('Координаты не корректны, введите их ещё раз')
            x, y = map(int, input().split())

    if (p1.move == True):
        grid.changePlace(x - 1, y - 1, True)
    else:
        grid.changePlace(x - 1, y - 1, False)


def End(win, p1, p2):
    if (win == 'Draw'):
        print('Ничья')
    elif (win == 'X'):
        print('Победил игрок', p1.name)
    else:
        print('Победил игрок', p2.name)

    print("Желаете ещё поиграть? 'Да' - поиграть ещё, 'Нет'- закончить играть")
    s = input()
    if (s != 'Да') or (s != 'Нет'):
        while (s != 'Да') or (s != 'Нет'):
            print('Либо "Да", либо "Нет"')
            s = input()
            print(s)
    if (s == 'Да'):
        main(p1, p2, createGrid())


######################

def welcome1():
    palyer1 = p('1', True)
    palyer2 = p('2', False)
    x, y, WinCount = 3, 4, 3

    return (palyer1, palyer2, g(x, y, WinCount))


def test():
    p1, p2, grid = welcome1()
    grid.changePlace(0, 2, True)
    grid.changePlace(1, 1, True)
    grid.changePlace(2, 0, True)
    # print(grid.checkPlace(0, 0))
    # print(grid.grid[0][0])
    # print(grid.checkPlace(0, 1))
    # print(grid.checkPlace(0, 2))

    grid.printGrid()
    print(set(grid.grid))


######################

def main(p1, p2, grid):
    if (p1 == None):
        p1, p2, grid = welcome()
    grid.printGrid()
    Win = grid.checkWin()
    while Win == "None":
        Play(p1, p2, grid)
        grid.printGrid()
        p1.changeMove()
        p2.changeMove()
        Win = grid.checkWin()
    End(Win,p1,p2)


if __name__ == '__main__':
    main(None, None, None)
    #test()
