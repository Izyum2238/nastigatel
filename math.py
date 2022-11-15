# способ нахождение суммы чисел
# total = 0 
# for i in range(1, 1001):
#     if i % 5 == 0 or i % 3 == 0:
#         total += i
# print(total)
# ----------------------------------------
# МЕТОД ФИБЕНАЧЧИ
# fib1 = fib2 = 1
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(fib1, fib2, end = "")
# for i in n:
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2)
# ----------------------------------------------

# Конвертация
# >>> number = 999
# >>> number_as_string = str(number)
# >>> number_as_string
# '999'
# ---------------------------------------------
# ПРОВЕРКА НА НЕЧЕТНОСТЬ ЧИСЕЛ 
# def func(a):
#     while a < 50:
#         if a % 2 != 0:
#             print(a)
#             return func(a + 1)
#         else:
#             return func(a + 1)
# func(3)
# ------------------------------------
# ФАКТОРИАЛ ВООБЩЕМ
# def factorial(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr = pr * i
#     print(pr)
# factorial(4)
