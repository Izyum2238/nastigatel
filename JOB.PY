
# import turtle
# def drawsquar():

#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
# turtle.speed(1)

# drawsquar()
# turtle.goto(150,150)
# drawsquar()
# ----------------------------------------------------------


# ------------------------------------------------- 
# ------------------------------------------------------------
# ------------------------------------------------------

# создание файла через функцию
# def file(text):
#     with open(text, "w")as f:
#         f.write("blal")

# text = input("Введите название: ")
# file(text)
# --------------------------------------------------

# ------------------------------------------------------------------


# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for i in digits:
#     print(i / 9)


# fruits = ('banana','stawberry','apple','orange','limon','ananas')
# print(fruits[0])
# print(fruits[5])


# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# spisok_2.difference(spisok_1)
# print(spisok_2)



# lst1 = []
# for i in range(301):
#     if i % 2 == 0:
#         lst1.append(i)
#     elif i == 237:
#         break
# print(lst1)

# ------------------------------------------------
# from random import randint
# number = randint(1, 11)
# while True:
#     a = int(input("Введи число в диапозоне 10 :"))
#     if a > number:
#         print("число чуть меньше")
#     elif a < number:
#         print("число чуть больше")
#     elif a == number:
#         print("you win")
#         break
        

# --------------------------------------------------
# lst = []
# while True:

#     game = input("Введи слово >>> ")
#     if len(game) < 6:
#         print("введите больше символов")
#     elif len(game) > 6:
#         lst.append(game)
#         len_list = len(lst)
#         middle = len_list // 2
#         print(middle)
# -----------------------------------------------
# cht = 0
# ncht = 0
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# for i in numbers:
#     if i % 2 == 0:
#         cht += 1
#     elif i % 2 != 0:
#         ncht += 1
    

# print(cht)
# print(ncht)
# -------------------------------------------------
# num = []
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# for i in numbers:
#     if i < 0:
#         num.append(-1)
#     elif i > 0:
#         num.append(1)
#     else:
#         i == 0
#         num.append(0)
# print(num)
# -----------------------------------------------


# my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]

# for i in range(0, len(my_list)):
#     if i % 2 == 0:
#         print(my_list[i])

#     else:
#         continue
# print(my_list)

# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
# b = 1
# while b != len(numbers):
#     if numbers[b] > numbers[b - 1]:
#         print(numbers[b], end=' ')
#     b += 1
# -------------------------------------------------
# three = 0
# a = "33333333333333333333333333333333333333333333333333333333333333333333333333"
# for i in a:
#     if i == "3":
#         three += 1
# print(three)

# ---------------------------------------------------------
# y_friends = {
# "Joomart": "+996555246810", 
# "Adinai": "+996555013579",
# "Ermek": "+996777013579",
# "Atai": "+996777246810",
# "Aslan": "+996999246810",}
# his_her_friends = {
# "Lyazat": "+996551123456",
# "Salavat": "+996552234567",
# "Daniyar": "+996553345678",
# "Bolot": "+996554456789",
# "Alymbek": "+996555501234",
# "Dastan": "+996556678912",
# "Maksat": "+996557789012",h
# "Aibek": "+996558890123",
# }
# b = {}
# for i in (y_friends, his_her_friends):
#     b.update(i)
# print(b)





