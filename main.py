import math

print("ax2+bx+c=0")
a = int(input())
b = int(input())
c = int(input())
d = (b ** 2) - (4 * a * c)
if (d < 0):
    print("Нет корней")
else:
    x_1 = (-b + math.sqrt(d)) / 2 * a
    x_2 = (-b - math.sqrt(d)) / 2 * a
    print(x_1)
    print(x_2)
