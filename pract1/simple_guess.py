# ввод - любое целое число
# вывол - корень числа
# если такого корня нет - "трудно, не смог"

# def guess(num: int) -> int:

# БЕЗ ПРОСТОГО ВЫВЕДЕНИЯ ИЗ ПОД КОРНЯ

#81
#9
number = int(input("Введите число: "))

def guess(num: int) -> int:
    for n in range(1, num + 1):
        if num < 0:
            return -1
        elif n**2 == num:
            return n
        elif n == num:
            return -1
        
result = guess(number)
if result == -1:
    print("Корень не найден")
else:
    print(f"Корень числа {number} = {result}")