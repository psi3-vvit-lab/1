#!/usr/bin/env python3

from math import sqrt

[a, b, c] = [int(x) for x in input().split()]
D = (b ** 2) - (4 * a * c)
if D >= 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(x1, x2)
else:
    print("корней нет")
