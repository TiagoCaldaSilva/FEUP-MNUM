import math as m

B = (m.sqrt(5) - 1) / 2
A = B ** 2


def f1(x, a):
    return (x - a) ** 2 + x ** 4


def ex1(x1, x2, a, function, error):
    while abs(x1 - x2) > error:
        x3 = x1 - A * (x2 - x1)
        x4 = x1 - B * (x2 - x1)
        if function(x3, a) > function(x4, a):
            x1 = x3
        else:
            x2 = x4
    return x1


print("EX1")
x_value = ex1(0, 2, 5, f1, 10 ** -4)
print("x = {} | f(x) = {}".format(x_value, f1(x_value, 5)))


def ex2_trap(x, xf, h, function, error):
    result = function(x) + function(xf)
    x += h
    while abs(xf - x) > error:
        result += 2 * function(x)
        x += h
    return result * h / 2


def ex2_simpson(x, xf, h, function, error):
    result = function(x) + function(xf)
    x += h
    i = 0
    while abs(xf - x) > error:
        i += 1
        if i % 2:
            result += 4 * function(x)
        else:
            result += 2 * function(x)
        x += h
    return result * h / 3


def diff2_y(x):
    return 2.5 * m.exp(2.5 * x)


def f2(x):
    return m.sqrt(1 + (diff2_y(x) ** 2))

print("EX2")
_result = ex2_trap(0, 1, 0.125, f2, 10**-4)
_result_ = ex2_trap(0, 1, 0.125 / 2, f2, 10**-4)
_result__ = ex2_trap(0, 1, 0.125 / 4, f2, 10**-4)
qc = (_result_ - _result) / (_result__ - _result_)
_error = (_result__ - _result_) / 3
print(_result, _result_, _result__, qc, _error)

_result = ex2_simpson(0, 1, 0.125, f2, 10**-4)
_result_ = ex2_simpson(0, 1, 0.125 / 2, f2, 10**-4)
_result__ = ex2_simpson(0, 1, 0.125 / 4, f2, 10**-4)
qc = (_result_ - _result) / (_result__ - _result_)
_error = (_result__ - _result_) / 15
print(_result, _result_, _result__, qc, _error)


def f3(x):
    return m.exp(x) - x - 5


def diff_f3(x):
    return m.exp(x) - 1


def g1(x):
    return m.exp(x) - 5


def g2(x):
    return m.log(x + 5)


def ex3_pp(guess, function, error):
    guess_old = guess + error * 10
    counter = 0
    while abs(guess - guess_old) > error:
        guess_old = guess
        guess = function(guess)
        counter += 1
    return guess, counter


def ex3_n(guess, function, diff, error):
    guess_old = guess + 10 * error
    counter = 0
    while abs(guess - guess_old) > error:
        guess_old = guess
        guess = guess - function(guess) / diff(guess)
        counter += 1
    return guess, counter


value, c = ex3_pp(-5.2, g1, 10**-4)
print("Picard peano, GUESS = -5.2\nx = {} | counter = {}" .format(value, c))
value, c = ex3_n(-5.2, f3, diff_f3, 10**-4)
print("Newton, GUESS = -5.2\nx = {} | counter = {}" .format(value, c))
value, c = ex3_pp(2, g2, 10**-4)
print("Picard peano, GUESS = 2\nx = {} | counter = {}" .format(value, c))
value, c = ex3_n(2, f3, diff_f3, 10**-4)
print("Newton, GUESS = 2\nx = {} | counter = {}" .format(value, c))


def ex_4_c(_c, t):
    return -m.exp(-0.5 / (t + 273)) * _c


def ex_4_t(_c, t):
    return 30 * m.exp(-0.5 / (t + 273)) * _c - 0.5 * (t - 20)


def ex4_euler(x, y, z, h, function1, function2, it):
    _it = 0
    while _it != it:
        print(_it, x, y, z)
        y_old = y
        z_old = z
        y = y + function1(y_old, z_old) * h
        z = z + function2(y_old, z_old) * h
        x += h
        _it += 1
    print(_it, x, y, z)
    return y, z


print("EULER:") # help
y_value, z_value = ex4_euler(0, 2.5, 25, 0.25, ex_4_c, ex_4_t, 2)
print("h'")
y_value_, z_value_ = ex4_euler(0, 2.5, 25, 0.25/2, ex_4_c, ex_4_t,2*2)
print("h''")
y_value__, z_value__ = ex4_euler(0, 2.5, 25, 0.25/4, ex_4_c, ex_4_t, 2*4)
qt = (z_value_ - z_value) / (z_value__ - z_value_)
_error = (z_value__ - z_value_)
print("Qt= {} | Error = {}".format(qt, _error))


def ex_4_rk2(x, y, z, h, function1, function2, it):
    _it = 0
    while _it != it:
        y_old = y
        z_old = z
        print(_it, x, y, z)
        y = y_old + function1(y_old + function1(y_old, z_old)*h/2, z_old + function2(y_old, z_old) * h/2)*h
        z = z_old + function2(y_old + function1(y_old, z_old)*h/2, z_old + function2(y_old, z_old) * h/2)*h
        x += h
        _it += 1
    return y, z


print("RK2:")
y_value_, z_value_ = ex_4_rk2(0, 2.5, 25, 0.25, ex_4_c, ex_4_t, 3)


def w(x, y):
    return -1.1*x*y + 12*y + 7*x**2 - 8*x


def dw_dx(x, y):
    return -1.1*y + 14*x - 8


def dw_dy(x, y):
    return -1.1*x + 12


def ex5_grad(x, y, lamb, diff_x, diff_y):
    x_old = x
    x = x - lamb * diff_x(x, y)
    y = y - lamb * diff_y(x_old, y)
    print(x, y, w(x, y))


print("EX5:")
ex5_grad(3, 1, 0.1, dw_dx, dw_dy)
