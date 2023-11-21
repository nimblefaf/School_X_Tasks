a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]
#   answer = [0, 0, 3, 0, 5]

def mask_list(array: list[int], mask: list[int]) -> list[int]:
    return [val * mask[i] * .5 for i, val in enumerate(array)]

def test_mask_list():
    print("проверяем тест маск лист")
    assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0], 'маска работает неправильно'

test_mask_list()
answer = mask_list(a, b)
print(answer)
# answer = [val * b[i] for i, val in enumerate(a)]
# print(answer)

# answer = [i for i in a] # 1 вариант

# for i in a:
#     answer.append(i)    # 2 вариант