my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список {my_list}')
print(f'Новый список {[x for i, x in enumerate(my_list) if i != 0 and my_list[i - 1] < my_list[i]]}')
