def my_function(a,b):
    return 1 / a ** abs(b)
print(f'Результат - {my_function(int(input("Введите число: ")), int(input("Введите отрицательное число, для возведения в степень: ")))}')