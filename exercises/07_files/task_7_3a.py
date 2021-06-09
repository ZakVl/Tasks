# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт:  Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open('CAM_table.txt')
list_lines = f.read().rstrip().split('\n')
sort_list = []
dict = {}
for line in list_lines:
    x=line.split()
    if len(x) < 4 or x[0].isdigit() == False:
        pass
    else:
         line_for_sort_list = ('{:<8} {:19} {}'.format(x[0], x[1], x[3])).split()
         line_for_sort_list[0] = int(x[0])
         sort_list = sort_list + [line_for_sort_list]
sorted_list = sorted(sort_list)
for z in sorted_list:
    print('{:<8} {:19} {}'.format(z[0], z[1], z[2]))


