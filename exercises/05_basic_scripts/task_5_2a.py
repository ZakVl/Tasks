# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
x=input('Введите IP-сети в формате: 10.1.1.0/24 ')
ip_address_mask_list=x.split('/')
ip_address=ip_address_mask_list[0]
ip_sepr=ip_address.split('.')
mask=int(ip_address_mask_list[1])
networkzero_mask='0'*int(32-mask)
#ip_oct1_bin=(bin(int(ip_sepr[0]))[2:])
#ip_oct1_bin_8bit='0'*(8-len(ip_oct1_bin))+str(ip_oct1_bin)
#ip_oct2_bin=(bin(int(ip_sepr[1]))[2:])
#ip_oct2_bin_8bit='0'*(8-len(ip_oct2_bin))+str(ip_oct2_bin)
#ip_oct3_bin=(bin(int(ip_sepr[2]))[2:])
#ip_oct3_bin_8bit='0'*(8-len(ip_oct3_bin))+str(ip_oct3_bin)
#ip_oct4_bin=(bin(int(ip_sepr[3]))[2:])
#ip_oct4_bin_8bit='0'*(8-len(ip_oct4_bin))+str(ip_oct4_bin)
#ip_address_bin=ip_oct1_bin_8bit+ip_oct2_bin_8bit+ip_oct3_bin_8bit+ip_oct4_bin_8bit

template_ip_adress_bin='{0:08b}{1:08b}{2:08b}{3:08b}'
ip_address_bin=template_ip_adress_bin.format(int(ip_sepr[0]), int(ip_sepr[1]), int(ip_sepr[2]), int(ip_sepr[3]))
ip_network_bin=ip_address_bin[0:(32-len(networkzero_mask))]+networkzero_mask
oct1_ip_dec=str(int(ip_network_bin[0:8],2))
oct2_ip_dec=str(int(ip_network_bin[8:16],2))
oct3_ip_dec=str(int(ip_network_bin[16:24],2))
oct4_ip_dec=str(int(ip_network_bin[24:32],2))
ip_network=oct1_ip_dec+'.'+oct2_ip_dec+'.'+oct3_ip_dec+'.'+oct4_ip_dec
ip_network=ip_network.split('.')

mask_b='1'*int(mask)+networkzero_mask
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
print(template_ip.format(int(ip_network[0]), int(ip_network[1]), int(ip_network[2]), int(ip_network[3])))
print(template_mask_b.format(mask, mask_oct1_dec, mask_oct2_dec, mask_oct3_dec, mask_oct4_dec, mask_oct1, mask_oct2, mask_oct3, mask_oct4))