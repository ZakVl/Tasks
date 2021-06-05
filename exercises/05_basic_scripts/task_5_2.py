# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'



Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
x=input('Введите IP-сети в формате: 10.1.1.0/24 ')
ip_address_mask_list=x.split('/')
ip_address=ip_address_mask_list[0]
ip_sepr=ip_address.split('.')
mask=int(ip_address_mask_list[1])
mask_b='1'*int(mask)+'0'*int(32-mask)
mask_oct1=int(mask_b[0:8])
mask_oct1_dec=int(mask_b[0:8], 2)
mask_oct2=int(mask_b[8:16])
mask_oct2_dec=int(mask_b[8:16], 2)
mask_oct3=int(mask_b[16:24])
mask_oct3_dec=int(mask_b[16:24], 2)
mask_oct4=int(mask_b[24:32])
mask_oct4_dec=int(mask_b[24:32], 2)
template_ip='''
Network
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}'''
template_mask_b='''
Mask:
/{0:0}
{1:<10}{2:<10}{3:<10}{4:<10}
{5:<08}  {6:<08}  {7:<08}  {8:<08}
'''
print(template_ip.format(int(ip_sepr[0]), int(ip_sepr[1]), int(ip_sepr[2]), int(ip_sepr[3])))
print(template_mask_b.format(mask, mask_oct1_dec, mask_oct2_dec, mask_oct3_dec, mask_oct4_dec, mask_oct1, mask_oct2, mask_oct3, mask_oct4))