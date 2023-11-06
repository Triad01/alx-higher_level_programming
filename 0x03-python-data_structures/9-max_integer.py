#!/usr/bin/python3
def max_integer(my_list=[]):

    max_num = my_list[0]

    if not my_list:

        return None

    if my_list:
        for num in my_list:

            if num > max_num:

                max_num = num

        return (max_num)
