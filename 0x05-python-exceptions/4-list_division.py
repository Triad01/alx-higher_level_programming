def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:

            if my_list_2[i] == 0:

                raise ValueError("division by 0")

            division_result = my_list_1[i] / my_list_2[i]

            result.append(division_result)

        except ZeroDivisionError:

            print("division by 0")

            result.append(0)

        except (TypeError, ValueError):

            print("wrong type")

            result.append(0)

        except IndexError:

            print("out of range")

            result.append(0)

        finally:

            pass

    return result
