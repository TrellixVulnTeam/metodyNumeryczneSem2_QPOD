import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f2(x):
    return (x - 2) ** 2 - 1


def dfdx(x):
    h = 10 ** -7
    return float(f2(x + h) - f2(x)) / h


def newton(f, x, eps=10 ** -4, max_iter=100):
    count_iters = 0

    while abs(f(x)) > eps and count_iters < max_iter:
        count_iters += 1

        x = x - float(f(x)) / dfdx(x)

    print(count_iters)  # TODO Usun to pod koniec
    return x


print(newton(f2, 4))

# TODO Usun to pod koniec
newton_f = optimize.newton(f2, 4, tol=10 ** -4)
print("this is newton value from sci ", newton_f)
