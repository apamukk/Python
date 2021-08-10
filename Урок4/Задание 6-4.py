from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el)
    if el == 10: break

from itertools import cycle

i = 0
my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)
    i += 1
    if i == 10: break