from typing import TypeAlias
IntOrNoneType: TypeAlias = int | None

alphabet: dict[
    int | str | None | float,
    str | int | float | dict[int, str | int | dict[int|str, str|int]]] = {
    1: 'A',
    2: [1,2],
    3: set([1, 1, 2, 3, 3, 4]),
    4: {
        1: 'A',
        2: 3,
        3: {
            'A': 12,
            3: 31
        }
    },
    10: 'Y',
    'Z' : 10,
    0.1: 'SDA',
    True: 'sdasd',
    False: 123123,
    None: 'dasdasd',
    # [1,2]: 3, #unhashible type list
}


print(alphabet.get(4).get(3))
# o_letter = alphabet.get('Z', None)
# if not bool(o_letter):
#     print("NO O")


for key, value in alphabet.items():
    print(f'Ключ: {key} Значение: {value}')

