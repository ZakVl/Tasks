
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
cfg_lines_list = []
x = input('имя исходного файла конфигурации (config_sw1.txt): ')
y = input('Вимя итогового файла конфигурации (Test1.txt, Test2.txt...): ')
f = open(x)
config=f.read().rstrip().split('\n')
for line in config:
    for x in ignore:
        if line.count(x) != 0: 
            line = '!' + line
    if line[0] == '!':
        pass
    else:
        cfg_lines_list.append(line +'\n')
#print(cfg_lines_list)
ff = open(y, 'w')
ff.writelines(cfg_lines_list)
ff.close()
