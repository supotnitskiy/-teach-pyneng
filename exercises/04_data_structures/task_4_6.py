# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""
from string import Template

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

list_ospf=ospf_route.replace('[', '').replace(']', '').replace(',','').split()

template_string = Template('''
Prefix               $prefix
AD/Metric            $metric
Next-Hop             $hop
Last update          $update
Outbound Interface   $int''')

prepared_string = template_string.substitute(prefix=list_ospf[0], metric=list_ospf[1], hop=list_ospf[3], update=list_ospf[4],int=list_ospf[5])

print(prepared_string)

