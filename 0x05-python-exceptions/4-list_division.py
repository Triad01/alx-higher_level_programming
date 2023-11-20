#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(list_length):

        try:

            result = 0

            if i < len(my_list_1) and i < len(my_list_2):

                is_my_list_1_valid = isinstance(my_list_1[i], (int, float))

                is_my_list_2_valid = isinstance(my_list_2[i], (int, float))

                if is_my_list_1_valid and is_my_list_2_valid:

                    if my_list_2[i] != 0:

                        result = my_list_1[i] / my_list_2[i]

                    else:

                        print("division by 0")

                else:

                    print("wrong type")

            else:

                print("out of range")

            new_list.append(result)

        except ZeroDivisionError:

            print("division by 0")

        except TypeError:

            print("wrong type")

    return new_list
