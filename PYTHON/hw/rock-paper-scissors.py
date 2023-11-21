# На входе: два слова, разделённых пробелами. Слова могут быть только - "камень" "ножницы" "бумага" в нижнем регистре.
# Задача: вывести какой игрок победил в игру "Камень, ножницы, бумага", если учесть, что первое слово - 1 игрок, второе слово - 2 игрок.
# 
# Выполнил Синюткин Андрей

players: list = str(input().lower()).split(sep=' ')
states: list = ["камень", "ножницы", "бумага"]

def input_is_valid() -> bool:
    if len(players) != 2:
        return False
    else:
        return players[0] in states and players[1]  in states

if input_is_valid():
    if players[0] == "камень":
        if players[1] == "ножницы":
            print("игрок 1 выиграл")
        elif players[1] == "бумага":
            print("игрок 2 выиграл")
        else:
            print("ничья")
    elif players[0] == "ножницы":
        if players[1] == "бумага":
            print("игрок 1 выиграл")
        elif players[1] == "камень":
            print("игрок 2 выиграл")
        else:
            print("ничья")
    else: #Игрок 1 выбрал бумагу
        if players[1] == "камень":
            print("игрок 1 выиграл")
        elif players[1] == "ножницы":
            print("игрок 2 выиграл")
        else:
            print("ничья")
else:
    print("ERROR: INVALID INPUT")