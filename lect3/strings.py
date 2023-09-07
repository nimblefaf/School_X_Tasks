# new_name: str = input('type name: ')

# greet_message: str = 'hello bob'

# # greet_message: str = (
# #     greet_message[:-3] + new_name
# # )

# greet_message: str = \
#     greet_message.replace('bob', new_name)

# print(greet_message)

# river: str = 'mmmmissisippi'
# print('m' + river.lstrip('m'))

# web_address: str = "https://threads.com/notifications"

# print(web_address.lstrip('https://')) #оставит "reads.com/notifications"

import string

numbers: str = string.digits
word: str = 'hell123o b32ob ho321w ar3e yo333u'

for num in numbers:
    word = word.replace(num, '')

print(word)