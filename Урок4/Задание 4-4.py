my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Исходный список {my_list}')
print(f'Новый список {[x for x in my_list if my_list.count(x) == 1]}')
