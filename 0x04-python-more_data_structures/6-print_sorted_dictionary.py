def print_sorted_dictionary(a_dictionary):

    for item in sorted(a_dictionary):

        value = a_dictionary[item]
        print("{}: {}".format(item, value))
