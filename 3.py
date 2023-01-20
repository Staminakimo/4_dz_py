# Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 0.001 -> 3.142
from math import pi

num = input()
num_list = list(num)
new_list = num_list[2:]
count = 0
for i in new_list:
    count += 1
p = pi
print(round(p, count))
