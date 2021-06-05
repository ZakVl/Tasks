# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
z=input('Введите IP адрес в формате 10.0.1.1: ')
count_point=z.count('.')
x=z.split('.')
count_oct=len(x)
numb=''.join(x)
ip_incorrect=False
while not ip_incorrect:
    if numb.isdigit()== False:
        print('Неправильный IP-адрес')
        break
#    try:
#        int(numb)
#    except ValueError:
#        print('Неправильный IP-адрес')
#        break
    elif count_point != 3 or count_oct != 4 or x[3]=='':
        print('Неправильный IP-адрес')
        break
    elif (int(x[0]) not in range(256)) or (int(x[1]) not in range(256)) or (int(x[2]) not in range(256)) or (int(x[3]) not in range(256)):
        print('Неправильный IP-адрес')
        break
    else:
        if z=='0.0.0.0':
            print('unassigned')
        elif z=='255.255.255.255':
            print('local broadcast')
        elif int(x[0])>=1 and int(x[0])<=223:
            print('unicast')
        elif int(x[0])>=224 and int(x[0])<=239:
            print('multicast')
        else: 
            print('unused')
        ip_incorrect=True
        break

