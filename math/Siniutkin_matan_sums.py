# сумма чисел в диапазоне [0; N]  которые делятся либо на 3, либо на 5. БЕЗ ЦИКЛОВ.
# Выполнил Синюткин Андрей

N = int(input("Введите N: "))

max_three = N//3
sum_three = (3+3*max_three)/2*max_three
# print(threes)

max_fives = N//5
sum_five = (5+5*max_fives)/2*max_fives
# print(fives)

max_fifteen = N//15
sum_fifteen = (15+15*max_fifteen)/2*max_fifteen
# print(fifteens)

# result = sum_three + sum_five - sum_fifteen
# Если в итоговой сумме должны присутсвовать числа кратные 3 и 5


result = sum_three + sum_five - 2 * sum_fifteen
# Если в итоговой сумме числа кратные 3 и 5 должны отсутствовать
print("Сумма чисел кратных 3 либо 5 = ", int(result))