#!/usr/bin/python3
def read_file(filename=""):
    """reads file and prints it to stdout"""
    with open(filename, "w+") as my_file:
        my_file.write("""We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.""")
        my_file.seek(0)
        data = my_file.read()
        print(data)
