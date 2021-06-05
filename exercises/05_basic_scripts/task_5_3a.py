# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
x=input('Введите режиме интерфейса (access/trunk):')
y=input('Введите номере интерфейса (тип и номер, вида Gi0/3):')
mode_z={'access':'Введите номер VLAN:', 'trunk':'Введите разрешенные VLANы:'}
z=input(mode_z[x])

temp_interface='''interface {}'''
#temp_vlan_a='''switchport access vlan {}'''
print_temp_a='''
{}
{}
{}
{}
{}
{}'''
print_temp_t='''
{}
{}
{}
{}
'''
a=print_temp_a.format(temp_interface.format(y), access_template[0], access_template[1].format(z), access_template[2], access_template[3], access_template[4])
t=print_temp_t.format(temp_interface.format(y), trunk_template[0], trunk_template[1], trunk_template[2].format(z))

mode_dict={'access':a,'trunk':t}
print(mode_dict[x])
