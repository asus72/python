#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Илья
#
# Created:     02.03.2019
# Copyright:   (c) Илья 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ticket(t_numb):
    if (len(str(t_numb))!= 6) or (type(t_numb) is not int):
        return 'Некорректный номер билета'
    else:
        t_numb1 = list(str(t_numb))
        sum1 = int(t_numb1[0]) + int(t_numb1[1]) + int(t_numb1[2])
        sum2 = int(t_numb1[3]) + int(t_numb1[4]) + int(t_numb1[5])
        if sum1 == sum2:
            return 'Билет %s счастливый' %t_numb
        else:
            return 'Билет %s несчастливый' %t_numb

number = int(input('Введите номер билета:'))
