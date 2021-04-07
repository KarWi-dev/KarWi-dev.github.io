"""
to start the script open CMD -> filepath -> py [filename]
"""

import os

def loop_list():
    for i in list_one:
        print(i)

list_one = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


os.system('cls')
print()
print('This list is' , len(list_one) , 'items long!')
print(list_one)
print(list_one[3])
print('-----------------------')

print(list_one[2:6])
print(list_one[:4])
print('-----------------------')

list_one[3] = 'penis'
print(list_one[3])
print(list_one)
print('-----------------------')

loop_list()
print('-----------------------')

if 'apple' in list_one:
    print(list_one[1])
print('-----------------------')
    
list_one.append('vagina')
print(list_one[3:])
print('-----------------------')

list_one.insert(2, 'tits')
print(list_one)
print('-----------------------')

list_one.remove('penis')
list_one.pop(2)
del list_one[6]
print(list_one)
print('-----------------------')

list_two = list_one.copy()
print(list_two)
list_one.clear()
print(list_one)