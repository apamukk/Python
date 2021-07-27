import time
sec = int(input('Введите секунды: '))
print(time.strftime('%H:%M:%S', time.gmtime(sec)))