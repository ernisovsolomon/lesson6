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
menu = [
    {'code': 100, 'name': 'Американо', 'price': 160},
    {'code': 101, 'name': 'Эспрессо', 'price': 140},
    {'code': 102, 'name': 'Латте', 'price': 180},
    {'code': 103, 'name': 'Капучино', 'price': 170},
    {'code': 104, 'name': 'Макиато', 'price': 150},
    {'code': 105, 'name': 'кофе 3-в-1', 'price': 50}
]
result = None
while True:
    code = int(input('Введите код кофе: '))
    for coffee in menu:             
        if code == coffee['code']:
            result = coffee
            break
    if result:
        break
    else:
        print('Не верный формат кода, введите обратно!')

        


pay = int(input(f'С вас {result['price']} сом за {result['name']}.\nВнесите оплату: '))

if pay > result['price']:
    cashback = pay - result['price']
    print(f'ОПЛАЧЕНО! Ваша сдача {cashback} сом')
elif pay == result['price']:
    print('ОПЛАЧЕНО! Держите ваш кофе!')
else:
    print('Недостаточно средств на балансе!')