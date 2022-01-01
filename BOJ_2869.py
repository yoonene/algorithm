from math import ceil

A, B, V = map(int, input().split())

d = (V-B)/(A-B)
print(ceil(d))
