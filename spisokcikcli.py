# append добавляет в конец списка указонный объект

# a = ("a", True, 77) вывод элемента по индексу
# print(a[0:2])

# ------------------------------------------------------------------------------
# a = ["azim" "beka" "nazik" "malika" "naufal"]
# b = "".join(a)   делает содержимое всех индексев единым
# print(a)
# --------------------------------------------------------------------------------

# дополняет все элементы в указонный список
# a = ["azim", 1233, "kuku", True]
# b = [12, 12.13, 999]
# a.extend(b)
# print(a)

# -----------------------------------------------------------------------------------------

# count - возрощает количество строк в указонной таблице с учетом повторяющихся строк
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]

# print(names.count("Jack"))
# -------------------------------------------------------------------------------------------

# удаляет конкретный названный объект, в однозначном числе тоесть первый попавшийся объект
# names = ['Jack', 'Jimmy', 'Oskar', 'Jackson', 'Oskar', 'Jhon', 'Oskar', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# names.remove("Oskar")
# print(names)
# ----------------------------------------------------------------------------------------

# a = []
# a.append("АЗИМ , 2004 python") данная команда вставляет в масивв определленный объект
# print(a)


# -----------------------------------------------------------------------


# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# print(pythonList[1:3]) 
# -данное значение принтует содержимое индекса по нумераций , счет индекс идет с нуля,


# ---------------------------------------------------------------------
# поп удаляет указанный индекс, индекс вычесляет строку какой она являються индексем по счету
# python = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# index = python.index("loop")
# print(python.pop(index))
# print(python)


# -----------------------------------------------------------------------
# делать арифметические задачи можно и в принте
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for  i in digits:
#         print(i / 9)



# ------------------------------------

# numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
# a = 1
# for i in numbers:
#     a *= i
#     print(a)
#     оператор присваивания *=
# ----------------------------------------

# метод работы с типами данных и определения 
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# numbers = []
# letters = []

# for i in spisok_1:
#     if type(i) == str:
#         letters.append(i)
#     if type(i) == int:
#         numbers.append(i)

# print(numbers)            
# print(letters)

# -------------------------------------------------------------------
# принцип остановки цикла с помощью команды break так же можн и с числами

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     print(i)


# ----------------------------------------------------------------

# нумерация элементов 

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in enumerate(languages):
#     print(i)


# ----------------------------------------------------
# пример как использовать реверс
# a = []
# b = []
# for i in range(1,11):
#     a.append(i)
#     b.append(i)
# b.reverse()
# for i in b:
#     if i < 10:
#         a.append(i)
# print(a)


# for i in range(1,10):
#     print("i =", i)
#     for j in range(1,10):
#         print(i * j)

#------------------------------------------------------------------------------------

# for i проходит циклом по всем индексам в списках , следущий вложенный цикл for j , уже превращает их в один целый список
# a = [[1,2,3], [4,5,6], [7,8,9]]
# b = []
# for i in a:
#     for j in i:
#         if type(j) == int:
#             b.append(j)
# print(b)
# ----------------------------------------------------------------------------------------

# пример работы с циклом и вложенным циклом + с условиями

# lst = [[1,2,3], ["first", "second", 'third'], [7,8,9]]
# letters = []
# numbers = []
# for i in lst:
#     for j in i:
#         if type(j) == str:
#             letters.append(j)
#         else: 
#             numbers.append(j)
# print(letters)
# print(numbers)
# ---------------------------------------------------------------------------------------

# count1 = 0
# count2 = 0

# for i in range(-100, 100):
#     if i % 13 == 0 and i % 2 == 0:
#         print(f'каждое число которое делиться на 13 без остатка четное возведенное в квадрат: {i ** 2}')
#         count1 += 1
# for i in range(-100, 100, 7):
#     if i % 2 != 0:
#         print(f"каждое 7 число не четное: {i}")
#         count2 += 1
# print(f"total_1 = {count1}")
# print(f"total_2 = {count2}")


# --------------------------------------------------------------------------------------------

# Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while)


# >>> for i in 'hello world':
# ...     if i == 'o':
# ...         continue
# ...     print(i * 2, end='')
# ...
# hheellll  wwrrlldd
# -------------------------------------------------------------------------

# метод деление листа по ровну
# list_1 = ['name', 'age', '1', '19']
# len_list = len(list_1)
# middle_index = len_list // 2
# first_half = list_1[:middle_index]
# second_half = list_1[middle_index:]
# first_half.reverse()
# second_half.reverse()
# print(first_half, second_half)

# -------------------------------------

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# метод сравнение двух списков
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(filter(lambda elem: elem in a, b))
# print(result)







    

    









