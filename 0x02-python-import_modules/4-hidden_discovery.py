#!/usr/bin/python3

import py_compile
import dis


def extract_names_from_pyc(pyc_file):

    names = []
    code = dis.Bytecode(pyc_file)
    for instruction in code:
        if instruction.opname == 'LOAD_GLOBAL':
            name = instruction.argval
            if not name.startswith("__"):
                names.append(name)
    return sorted(names)


if __name__ == "__main":

    with open("hidden_4.pyc", "rb") as pyc_file:
        names = extract_names_from_pyc(pyc_file)

    for name in names:
        print(name)
