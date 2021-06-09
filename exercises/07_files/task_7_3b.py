# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
y = input('Введи номер Vlan (10, 100, 200, 300, 500, 1000): ')
f = open('CAM_table.txt')
list_lines = f.read().rstrip().split('\n')
for line in list_lines:
    x=line.split()
    if len(x) < 4 or x[0].isdigit() == False:
        pass
    elif y == x[0]:
        print('{:8} {:19} {:8}'.format(x[0], x[1], x[3]))
