text = str(input('Введите любой текст:'))
x = text.split()
y = 1
for i in x:
    print(y, i[:10])
    y += 1