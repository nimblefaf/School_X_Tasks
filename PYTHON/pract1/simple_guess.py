# ввод - любое целое число
# вывол - корень числа
# если такого корня нет - "трудно, не смог"
# def guess(num: int) -> int:
# БЕЗ ПРОСТОГО ВЫВЕДЕНИЯ ИЗ ПОД КОРНЯ
#
# 
# Выполнил Синюткин Андрей

number = int(input("Введите число: "))

def guess(num: int) -> int:
    for n in range(1, num + 1):
        if num < 0:
            return -1
        elif n**2 == num:
            return "Найден корень: " + str(n)
        elif n == num:
            return "Слишком сложно, не могу"
        
result = guess(number)
print(result)