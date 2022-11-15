# метод вызова вложенной функций
# def one():
#     print("я ne главный")
# def two():
#     print("я главный")
#     one()
# two()
# ----------------------------------------------

# метод объеденения словаре через функцию 
#                                          return возращает значение функций
# def dictplus(dict1, dict2):
#     dict1.update(dict2)
#     return dict1
# dict_1 = {'one':1}
# dict_2 = {'two': 2}
# print(dictplus(dict_1, dict_2))
# ---------------------------------------------------


# посчитал количество символов без помощи len.
# def word(a):
#     syms = str(a)  : создал переменную и указал тип данных в нем передал аргумент
#     words = a.count("") - 1 : создал переменную что бы считала кол. символов в аргументе_  - 1 значит убрать пробел
#     print(words)
# word("azimkaagchgmh")  
# ----------------------------------------------------
#  разбор вложенного словаря 
# dict = {"333":
#     {
#         "name": "azat",
#         "age": 18,
#         "gender": "m",
#         "id": 23949250




#     }

# }
# for i in dict.values():
#     for j in i.values():
#         print(j)
# ----------------------------------------------------

# def gen_number():
#     from random import choice
#     num = "0444"
#     for _ in range(6):
#         num += choice("145790")
#         return num
# for i in range(10):


# from random import randint


# list1 = []
# def get(func):
#     def wrap(list1):
#         for _ in range(101):
#             num = randint(10,50)
#             list1.append(num)
#             func(list1)
#     return wrap
# @get
# def func(list1):
#     a = set(list1)
#     print(list1(a))
# func(list1)

