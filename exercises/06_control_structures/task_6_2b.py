# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
z=input('Введите IP адрес в формате 10.0.1.1: ')

ip_incorrect=False
while not ip_incorrect:
    count_point=z.count('.')
    x=z.split('.')
    print(x)
    count_oct=len(x)
    print(count_oct)
    numb=''.join(x)
   
    if numb.isdigit()== False:
        print('Неправильный IP-адрес')
        z=input('Введите IP адрес в формате 10.0.1.1: ')
    elif count_point != 3 or count_oct != 4 or x[3]=='':
        print('Неправильный IP-адрес')
        z=input('Введите IP адрес в формате 10.0.1.1: ')
    elif (int(x[0])<0 or int(x[0])>255) or (int(x[1])<0 or int(x[1])>255) or (int(x[2])<0 or int(x[2])>255) or (int(x[3])<0 or int(x[3])>255):
        print('Неправильный IP-адрес')
        z=input('Введите IP адрес в формате 10.0.1.1: ')
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
    
