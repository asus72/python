#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      isdobnikov
#
# Created:     26.02.2019
# Copyright:   (c) isdobnikov 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
#
first_list = [1, 3, 5, 7, 9]
second_list = [3, 8, 6, 5]
res = []
print(first_list, second_list)
for i in first_list:
    if i not in second_list:
        res.append(i)
lst1 = res
print(first_list, second_list)
print()