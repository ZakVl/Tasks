# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
f = open('ospf.txt')
list_lines = f.read().replace(',','').replace('[','').replace(']','').rstrip().split('\n')
x = 0
template = '''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}'''
for line in list_lines:
    line_x = line.split() 
    print(template.format(line_x[1], line_x[2], line_x[4], line_x[5], line_x[6]))
   

