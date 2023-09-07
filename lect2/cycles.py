numbers: list = [
    1,2,3,4,5,6,7,8,9
    ]

# for n in numbers:
#     if n % 3 == 0:
#         print(f"Число - {n} кратно 3")
#     if n % 3 != 0:
#         print(f"Число - {n} не кратно 3")

# for n in numbers:
#     if n % 3 and n % 5:
#         print(f"Число - {n} чётное")
#     elif n % 5 == 0:
#         print()
#     elif n % 3:
#         print()
#     else:
#         print(f"Число - {n} нечётное")

# word: str = input("Введите слово: ")
# vowels: str = 'aeiouy'

# vowel_count: int = 0
# for ch in word:
#     if ch in vowels:
#         vowel_count += 1
# print(vowel_count)

# n: int = int(input("N:"))
# sum_3, sum_5, sum_3_5 = 0, 0, 0

# for i in range(n+1):
#     if i % 3 == 0 and n % 5 == 0:
#         sum_3_5 = sum_3_5 + i
#     elif i % 3 == 0:
#         sum_3 = sum_3 + i
#     elif i % 5 == 0:
#         sum_5 = sum_5 + i
# print(sum_3_5)

n: int = int(input("n: "))
array: list = list(range(n))

i = 0
while(True):
    if array[i] % 123 == 0:
        print(array[i], "делится")
        break
    i += 1
