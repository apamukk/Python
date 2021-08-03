def my_func(name,surname,birth,city,email,tel):
 name = str(input("Введите Ваше имя:"))
 surname = str(input("Введите Вашу фамилию:"))
 birth = int(input("Введите Ваш год рождения:"))
 city = str(input("Введите Ваш город проживания"))
 email = str(input("Введите Ваш электронный адрес:"))
 tel = int(input("Введите Ваш номер телефона"))
 return (name,surname,birth,city,email,tel)
print(my_func("name","surname","birth","city","email","tel"))
