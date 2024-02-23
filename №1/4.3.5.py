from math import *
while True: print(eval((input(">> "))))

# V2
# def e1(a, b):
#     return e ** (a + b)
# def e2(a, b):
#     return sin(a + b)
# def e3(a, b):
#     return cos(a + b)
# def e4(a, b):
#     return a ** b
# def plus(a, b):
#     return a + b
# def minus(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     if b == 0:
#         return "Ошибка"
#     else:
#         return a / b
# vibor = ''
# vibor2 = ''
# num1 = float(input("Введите первое число "))
# num2 = float(input("Введите второе число "))
# operation = input("Выберите действие: ""\n"" 1. +, -, *, / ""\n"" 2. e^(x+y), sin(x+y), cos(x+y), x^y ""\n")
# if operation == '1':
#     vibor = input("Выберите действие: ""\n"" 1. +, -, *, / ")
# elif operation == '2':
#     vibor2 = input("Выберите действие: 2.  1 - e^(x+y), 2 - sin(x+y), 3 - cos(x+y), 4 - x^y ")
# elif operation != '1' or operation != '2':
#     print("Ошибка выбора")
# 
# if vibor == '+':
#     print(f"{num1} + {num2} = {plus(num1, num2)}")
# elif vibor == '-':
#     print(f"{num1} - {num2} = {minus(num1, num2)}")
# elif vibor == '*':
#     print(f"{num1} * {num2} = {multiply(num1, num2)}")
# elif vibor == '/':
#     print(f"{num1} / {num2} = {divide(num1, num2)}")
# elif vibor:
#     print("Неверная операция. Пожалуйста, выберите из списка: +, -, *, /")
# 
# if vibor2 == '1':
#     print(f"e^(x+y) = {e1(num1, num2)}")
# elif vibor2 == '2':
#     print(f"sin(x+y) = {e2(num1, num2)}")
# elif vibor2 == '3':
#     print(f"cos(x+y) = {e3(num1, num2)}")
# elif vibor2 == '4':
#     print(f"x^y = {e4(num1, num2)}")
# elif vibor2:
#     print("Неверная операция. Пожалуйста, выберите из списка: 1, 2, 3, 4")
