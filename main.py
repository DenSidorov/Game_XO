print('Игра "Крестики нолики"')
print('Вводите координаты x и y')
print('x - номер строки')
print('y - номер столбца')

pole = [[" "] * 3 for i in range(3)]

def show_pole():
    print(f'   0 1 2')
    for i in range(3):
        row = " ".join(pole[i])
        print(f"{i}  {row}")

def ask():
    while True:
        coords = input("Ведите координаты через пробел: ").split()
        if len(coords) !=2:
            print("Неверные координаты!!!!")
            continue
        x,y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Неверные координаты")
            continue

        x,y=int(x), int(y)
        if x<0 or x>2 or y>2 or y<0 or pole[x][y] != " ":
            print("Неверные координаты.")
            continue
        return x, y

def win():
    win_coords = (((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                  ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)),
                  ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0)))
    for coords in win_coords:
        symbols = []
        for a in coords:
            symbols.append(pole[a[0]][a[1]])
            if symbols == ["X", "X", "X"]:
                print('___ ИГРА ОКОНЧЕНА___')
                print('Выиграл "X"!!!')
                show_pole()
                return True
            if symbols == ["0", "0", "0"]:
                print('___ ИГРА ОКОНЧЕНА___')
                print('Выиграл "0"!!!')
                show_pole()
                return True
    return False

num = 0
while True:
    num += 1

    show_pole()

    if num%2 == 1:
        print('Ход "X"')
    else:
        print('Ход "0"')

    x,y = ask()

    if num%2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "0"

    if win():
        break

    if num == 9:
        print('Ничья!')
        break