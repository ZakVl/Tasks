# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

#x = input('Введите имя файла (config_sw1.txt): ')
#f = open(x)
f = open('config_sw1.txt')
config=f.read().rstrip().split('\n')
for line in config:
    for x in ignore:
        if line.count(x) != 0: 
            line = '!' + line
    if line[0] == '!':
        pass
    else:
        print (line)



 
