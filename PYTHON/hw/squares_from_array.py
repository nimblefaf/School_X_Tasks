# Вывести массив числе от -N до N включительно возведённых в квадрат.
# Выполнил Синюткин Андрей

N: int = int(input("Введите число N:"))
squares: list = []

for i in range(-N, N + 1):
    squares.append(i ** 2)

print(squares)