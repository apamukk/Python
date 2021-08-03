def my_sum():
    a = False
    sum_ = 0
    while a == False:
        number = input('Введите числа через проблел и Q чтобы закончить программу: ').split()
        c = 0
        for b in range(len(number)):
            if number[b] == 'q' or number[b] == 'Q':
                a = True
                break
            else:
                c = c + int(number[b])
        sum_ = sum_ + c
        print(f'Сумма введенных числе составляет: {sum_}')
    print(f'Общая сумма введеных числе составляет: {sum_}')
my_sum()