#!/usr/bin/python3
def safe_print_integer(value):

    try:
        if isinstance(value, int):

            print(value)

            return True

        elif isinstance(value, str):

            return False

    except (TypeError, ValueError):

        return "Type Error"
