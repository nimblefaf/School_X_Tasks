# На вход вы принимаете: массив целых чисел неопределенной длины, где каждый элемент в последовательности больше предыдущего
# Вам нужно найти индекс (порядковый номер) чисел, которые отличаются от предыдущего на более, чем 1.
# Если таковых в массиве нет - вывести на экран "Не найдено"
# Если числе много - вывести список индексов, если один - простым числом
# Длина массива >= 2

# Выполннил Синюткин Андрей


numbers: list = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
result_indexes: list = [int]

def check_array_for_wrongs(nums: list) -> list:
    result: list[int] = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] != 1:
            result.append(i)
    return result

result_indexes = check_array_for_wrongs(numbers)

if len(result_indexes) == 0:
    print("Не найдено")
elif len(result_indexes) == 1:
    print(result_indexes[0])
else:
    print(result_indexes)