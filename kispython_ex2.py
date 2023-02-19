import math


def f(z):
    if z < -20:
        return math.tan(59 * z + (z ** 3 / 41) + (z ** 2 / 3)) ** 7
    elif -20 <= z < 18:
        return 69 * z ** 2 - 85 - 47 * z ** 5
    elif 18 <= z < 77:
        return 95 * z ** 4 - 73 * (39 * z ** 2) ** 5 - 13
    elif 77 <= z < 117:
        return z ** 2 / 19
    elif z >= 117:
        return 71 * (z ** 2 - z ** 3 - 76 * z) ** 3 - \
               math.log10(81 * z ** 3) ** 6 - z ** 2


print(f(61))
print(f(99))
print(f(-38))
print(f(137))
print(f(-9))
