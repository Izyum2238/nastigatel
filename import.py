 
# a = []
# b = []
# c = []
# p = []

# from random import choice
# names = ["azim", "aibek", "joomart", "andrey", "stepan", "volk", "naufal", "rauf", "kamila", "malika", "valya", "dosya", "akram"]

# while len(a) < 3:
#     names.remove
#     b = choice(names)
#     if b not in a:
#         a.append(b)
# print(a)        

# while len(c) < 3:
#     y = choice(names)
#     if y not in c:
#         c.append(y)
# print(c)

# while len(p) < 3:
#     z = choice(names)
#     if z not in p:
#         p.append(z)
# print(p)



# -------------------------------------------------
# from random import randint, randrange, choice, shuffle


# a = ['beka', 'azat', 'bob', 'john', 'alex']
# shuffle(a) = рандонмно раставляет порядок списка
# print(a)
# print(choice(a)) = достает рандомное значение
# ------------------------------------------ 
# num = randrange(1,100,3)= достает рандомное число с шагом
# print(num)
# a = randint(1,100) = просто рандомные числа в указонном диапозоне
# print(a)
# ----------------------------------

# a = ['beka', 'azat', 'bob', 'john', 'alex']

# from time import sleep
# for i in a:
#     print(i)
#     sleep(2) =  можно управлять скоростью итераций
# -------------------------------------------

# from datetime import datetime, time, timedelta
# now = datetime.now() 
# print(now) указывает точное время до милисекунд
# print(now.day) показывает день месяца
# print(now.date()) год месяц и число
# print(now.year) год
# print(now.time()) время
# timeobj = time(8,1,45) можно указать время
# print(timeobj)
    

                    #  %b  месяц в виде строки
# print(now.strftime("%d - %m - %y")) вывод даты в виде строки


# now += timedelta(days = 1000) - прибавил к текущей дате 1000 дней
# print(now)

# ---------------------------------------------


# import os
# os.system("ls") работа с терминалом через пайтон
# -------------------------------------------------

# from string import ascii_letters, digits
# from random import choice
# from time import sleep

#   пример генерацй  паролей или логинов 
# while True:
#     password = ""
#     while len(password) < 8:
#         # choice1 = choice(ascii_letters) все буквы
#         choice1 = choice(digits) числа
#         password += choice1

#     print(password)
#     sleep(3)

# ---------------------------------------------------
# import sys, os
# a = 124123123
# print(sys.getsizeof(a))
# -----------------------------------------
# from random import randint as r
#                            через as можна выберать псевдоним для модуля
# number = r(1,1000)
# print(number)
# ----------------------------------------------------

    
    
    




