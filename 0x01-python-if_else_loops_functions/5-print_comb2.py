#!/usr/bin/python3
# Write a program that prints numbers from 0 to 99

for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=",")
