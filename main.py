'''
1) Напишите программу, которая считает сумму чисел от 1 до 10 включительно.
'''
# for i in range(1,11):
#     print(i)
'''
2) Напишите программу, которая выводит все четные числа от 2 до 20 включительно.
'''
# for i in range(2,21,2):
#     print(i)
'''
3) Напишите программу, которая выводит таблицу умножения на 5.
'''
# for i in range(1, 11):
#     result = i * 5
#     print(f'{i} * 5 = {result}')
'''
4) Напишите программу, которая выводит элементы списка в обратном порядке без
использования встроенных методов.
'''
# my_list = [1, 2, 3, 4, 5]
# for i in range(len(my_list) - 1, -1, -1):
#     print(my_list[i])
'''
5) Напишите программу, которая считает количество гласных букв в данной строке.
'''
# vowels_US = ['a', 'e', 'i', 'o', 'u', 'y']
# vowels_RU = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# vowels = vowels_US + vowels_RU
# text = 'Напишите программу, которая считает количество гласных букв в данной строке'
# count = 0
# for i in text:
#     if i in vowels:
#         count += 1
# print(count)
'''
6) Написать программу для выбора и оплаты кофе. (Условие для этой задачи можно
внести от себя).
'''
# menu = [
#     {'code': 100, 'name': 'Американо', 'price': 160},
#     {'code': 101, 'name': 'Эспрессо', 'price': 140},
#     {'code': 102, 'name': 'Латте', 'price': 180},
#     {'code': 103, 'name': 'Капучино', 'price': 170},
#     {'code': 104, 'name': 'Макиато', 'price': 150},
#     {'code': 105, 'name': 'кофе 3-в-1', 'price': 50}
# ]


# result = None
# while True:
#     code = int(input('Введите код кофе: '))
#     for coffee in menu:             
#         if code == coffee['code']:
#             result = coffee
#             break
#     if result:
#         break
#     else:
#         print('Не верный формат кода, введите обратно!')


# pay = int(input(f'С вас {result['price']} сом за {result['name']}.\nВнесите оплату: '))
# if pay > result['price']:
#     cashback = pay - result['price']
#     print(f'ОПЛАЧЕНО! Ваша сдача {cashback} сом')
# elif pay == result['price']:
#     print('ОПЛАЧЕНО! Держите ваш кофе!')
# else:
#     print('ОШИБКА! Недостаточно средств на балансе!')
'''
7) Задание «Список гостей»
'''
# Задание находится в отдельном файле my_guest.py

'''
50б.
1) Создайте список чисел, кратных 3, в диапазоне от 3 до 30.
'''
# for i in range(3,31, 3):
#     print(i)
'''
2) Создайте список четных чисел от 2 до 1 000 включительно.
'''
# my_list = []
# for i in range(1,1001):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list)
'''
3) Суммируйте все числа внутри списка четных чисел
'''
# summa = 0
# for i in range(1,1001):
#     summa += i
# print(summa)
'''
4) **Кубы: результат возведения числа в третью степень называется кубом.
Например, куб 2 записывается в языке Python в виде 2**3.
Создайте список первых 10 кубов (то есть кубов всех целых чисел от 1 до 10)
и выведите значения всех кубов в цикле for.
'''
# cube_list = []
# for i in range(1, 10):
#     cube_list.append(i**3)
# print(cube_list)
'''
Задача: Поиск наименьшего числа
Напишите программу на Python, которая запрашивает у пользователя ввод целых чисел до тех пор,
пока пользователь не введет 0. После ввода 0 программа должна вывести наименьшее введенное число,
не считая 0.
Эта задача поможет вам попрактиковаться в использовании цикла while для обработки ввода пользователя
и условий для обновления минимального значения.
	
    Примерный алгоритм решения:
 - Инициализируйте переменную для хранения наименьшего числа значением None или первым введенным значением.
 - Используйте цикл while для запрашивания чисел у пользователя.
 - Если пользователь вводит 0, завершите цикл.
 - Проверьте, является ли текущее введенное число меньше сохраненного наименьшего числа.
 Если да, обновите наименьшее число.
 - После выхода из цикла выведите наименьшее введенное число.
 - В этой задаче нужно продемонстрировать базовое использование цикла while, обработку условий
 и работу с пользовательским вводом в Python.
'''
# numbers = []
# while True:
#     num = int(input('Введите число: '))    
#     if num == 0:
#         break
#     else:
#         numbers.append(num)

# print(f'Число {min(numbers)} наименьшее из тех что вы ввели!')