import math as m


def bisection_method(a, b, function, error):
    counter = 0
    while abs(a - b) > error:
        m = (a + b) / 2
        if function(a) * function(m) < 0:
            b = m
        else:
            a = m
        counter += 1
    return a, counter


def rope_method(a, b, function, error):
    counter = 0
    while abs(a - b) > error:
        w = (a * function(b) - b * function(a)) / (function(b) - function(a))
        if function(a) * function(w) < 0:
            b = w
        else:
            a = w
        counter += 1
    return a, counter


def newtons_method(guess, function, diff, error):
    new_x = guess
    old_x = guess + 10
    counter = 0
    while abs(new_x - old_x) > error:
        old_x = new_x
        new_x = old_x - function(old_x) / diff(old_x)
        counter += 1
    return new_x, counter


def picard_peano_method(guess, function, error):
    old_x = guess + 10
    new_x = guess
    counter = 0
    while abs(new_x - old_x) > error:
        old_x = new_x
        new_x = function(old_x)
        counter += 1
    return new_x, counter


# functions tests


def f1(x):
    return 2**(m.sqrt(x)) - 10*x + 1    # 2 raizes, 1 próxima de 0.2-0.4 e outra próxima de 98-100


def diff_f1(x):
    return ((m.log(2) * 2**(m.sqrt(x) - 1)) / m.sqrt(x)) - 10


print("Function 1:")
print("Bisection method:")
value, counter_v = bisection_method(0.1, 0.5, f1, 10**-4)
print("{} | {}" .format(value, counter_v))
print("Rope method:")
value, counter_v = rope_method(0.1, 0.3, f1, 10**-4)
print("{} | {}" .format(value, counter_v))
print("Newtons method:")
value, counter_v = newtons_method(0.5, f1, diff_f1, 10**-4)
print("{} | {}" .format(value, counter_v))


def f2(x):
    return x - 2*m.log(x) - 5   # 2 raizes, 1 proxima de 0-0.3 e a outra 9-10


def diff_f2(x):
    return 1 - 2/x


print("Function 2:")
print("Bisection method:")
value, counter_v = bisection_method(0.05, 0.2, f2, 10**-4)
print("{} | {}" .format(value, counter_v))
print("Rope method:")
value, counter_v = rope_method(0.05, 0.2, f2, 10**-4)
print("{} | {}" .format(value, counter_v))
print("Newtons method:")
value, counter_v = newtons_method(0.05, f2, diff_f2, 10**-4)
print("{} | {}" .format(value, counter_v))


def g1(x):
    return m.exp((x - 5) / 2)


print("Picard-peano method:")
value, counter_v = picard_peano_method(0.05, g1, 10**-4)
print("{} | {}" .format(value, counter_v))


def g2(x):
    return 2 * m.log(x) + 5


print("Picard-peano method:")
value, counter_v = picard_peano_method(9, g2, 10**-4)
print("{} | {}" .format(value, counter_v))


def newtons_method_to_system(guess_x, guess_y, function1, function2, diff_f1, diff_f2, error):
    old_x = guess_x + 10
    old_y = guess_y + 10
    new_x = guess_x
    new_y = guess_y
    counter = 0
    while abs(new_x - old_x) > error or abs(new_y - old_y) > error:
        old_x = new_x
        old_y = new_y
        new_x = old_x - (function1(old_x, old_y) * diff_f2[1](old_x, old_y) - function2(old_x, old_y) * diff_f1[1](old_x, old_y)) / (diff_f1[0](old_x, old_y) * diff_f2[1](old_x, old_y) - diff_f1[1](old_x, old_y) * diff_f2[0](old_x, old_y))
        new_y = old_y - (function2(old_x, old_y) * diff_f1[0](old_x, old_y) - function1(old_x, old_y) * diff_f1[0](old_x, old_y)) / (diff_f2[1](old_x, old_y) * diff_f1[0](old_x, old_y) - diff_f1[1](old_x, old_y) * diff_f2[0](old_x, old_y))
        counter += 1
    return new_x, new_y, counter


def f3(x, y):
    return 2*x**2 - x*y - 5*x + 1


def f4(x, y):
    return x + 3*m.log(x) - y**2


def diff_f3_x(x, y):
    return 4*x - y - 5


def diff_f3_y(x, y):
    return -x


def diff_f4_x(x, y):
    return 1 + 3/x


def diff_f4_y(x, y):
    return -2*y


print("Newtons method to systems:")
value_x, value_y, counter_v = newtons_method_to_system(4, 4, f3, f4, [diff_f3_x, diff_f3_y], [diff_f4_x, diff_f4_y], 10**-6)
print("{} | {} | {}" .format(value_x, value_y, counter_v))


def picard_peano_method_to_system(guess_x, guess_y, function1, function2, error):
    old_x = guess_x + 10
    old_y = guess_y + 10
    new_x = guess_x
    new_y = guess_y
    counter = 0
    while abs(new_x - old_x) > error or abs(new_y - old_y) > error:
        old_x = new_x
        old_y = new_y
        new_x = function1(old_x, old_y)
        new_y = function2(old_x, old_y)
        counter += 1
    return new_x, new_y, counter


def g3(x, y):
    return m.sqrt((x*y+5*x-1) / 2)


def g4(x, y):
    return m.sqrt(x + 3*m.log(x))


print("Picard-peano method to systems:")
value_x, value_y, counter_v = picard_peano_method_to_system(4, 4, g3, g4, 10**-6)
print("{} | {} | {}" .format(value_x, value_y, counter_v))


def gauss_seidel_method_to_system(guess_x, guess_y, function1, function2, error):
    old_x = guess_x + 10
    old_y = guess_y + 10
    new_x = guess_x
    new_y = guess_y
    counter = 0
    while abs(new_x - old_x) > error or abs(new_y - old_y) > error:
        old_x = new_x
        old_y = new_y
        new_x = function1(old_x, old_y)
        new_y = function2(new_x, old_y)
        counter += 1
    return new_x, new_y, counter


print("Gauss seidel method to systems:")
value_x, value_y, counter_v = gauss_seidel_method_to_system(4, 4, g3, g4, 10**-6)
print("{} | {} | {}" .format(value_x, value_y, counter_v))


def method_gauss_jacobi(matrix, x1, x2, x3, error):
    counter = 0
    x1_n = x1 + error + 1
    x2_n = x2 + error + 2
    x3_n = x3 + error + 3
    while abs(x1_n - x1) > error or abs(x2_n - x2) > error or abs(x3_n - x3) > error:
        x1 = x1_n
        x2 = x2_n
        x3 = x3_n
        x1_n = (matrix[0][3] - matrix[0][1]*x2 - matrix[0][2]*x3) / matrix[0][0]
        x2_n = (matrix[1][3] - matrix[1][0]*x1 - matrix[1][2]*x3) / matrix[1][1]
        x3_n = (matrix[2][3] - matrix[2][0]*x1 - matrix[2][1]*x2) / matrix[2][2]
        counter += 1
    return x1_n, x2_n, x3_n, counter


print("Gauss jacobi method:")
_x1, _x2, _x3, counter_v = method_gauss_jacobi([[3, 1, 1, 7], [1, 4, 2, 4], [0, 2, 5, 5]], 0, 0, 0, 10**-4)
print("{} | {} | {} | {}" .format(_x1, _x2, _x3, counter_v))


def method_gauss_seidel(matrix, x1, x2, x3, error):
    counter = 0
    x1_n = x1
    x2_n = x2
    x3_n = x3
    x1 += 1
    x2 += 2
    x3 += 3
    while abs(x1_n - x1) > error or abs(x2_n - x2) > error or abs(x3_n - x3) > error:
        x1 = x1_n
        x2 = x2_n
        x3 = x3_n
        x1_n = (matrix[0][3] - matrix[0][1]*x2 - matrix[0][2]*x3) / matrix[0][0]
        x2_n = (matrix[1][3] - matrix[1][0]*x1_n - matrix[1][2]*x3) / matrix[1][1]
        x3_n = (matrix[2][3] - matrix[2][0]*x1_n - matrix[2][1]*x2_n) / matrix[2][2]
        counter += 1
    return x1_n, x2_n, x3_n, counter


print("Gauss seidel method:")
_x1, _x2, _x3, counter_v = method_gauss_seidel([[3, 1, 1, 7], [1, 4, 2, 4], [0, 2, 5, 5]], 0, 0, 0, 10**-4)
print("{} | {} | {} | {}" .format(_x1, _x2, _x3, counter_v))


def trapezoids_method(n, function, a, b):
    h = (b - a) / n
    result = function(a)
    for i in range(1, n + 1, 1):
        result += 2*function(a + i*h)
    return result * h/2


def f5(x):
    return m.sin(x) / (x**2)


print("Trapezoids method:")
_result = trapezoids_method(4, f5, m.pi/2, m.pi)
_result__ = trapezoids_method(8, f5, m.pi/2, m.pi)
_result___ = trapezoids_method(16, f5, m.pi/2, m.pi)
qc = (_result__ - _result) / (_result___ - _result__)
_error = (_result___ - _result__) / 3
print("{} | {} | {}" .format(_result, _result__, _result___))
print(qc)
print(_error)


def simpsons_method(n, function, a, b):
    h = (b - a) / n
    result = function(a) + function(b)
    for i in range(1, n, 1):
        if i % 2 == 0:
            result += 2*function(a + i * h)
        else:
            result += 4*function(a + i * h)
    return result * h/3


print("Simpsons method:")
_result = simpsons_method(4, f5, m.pi/2, m.pi)
_result_ = simpsons_method(8, f5, m.pi/2, m.pi)
_result__ = simpsons_method(16, f5, m.pi/2, m.pi)
_result___= simpsons_method(32, f5, m.pi/2, m.pi)
qc = (_result_ - _result) / (_result__ - _result_)
_error = (_result__ - _result_) / 15
print("{} | {} | {}" .format(_result, _result_, _result__))
print(qc)
print(_error)
qc = (_result__ - _result_) / (_result___ - _result__)
print(qc)

#
#
#   Falta cubatura e chalensky
#
#


def euler_method(x0, y0, h, xf, function, error):
    xn = x0
    while abs(xf - x0) > error:
        xn = x0
        x0 += h
        y0 += function(xn, y0)*h
    return y0


def f6(x, y):
    return x**2 + y**2


value = euler_method(0, 0, 0.1, 1.4, f6, 10**-4)
value_ = euler_method(0, 0, 0.05, 1.4, f6, 10**-4)
value__ = euler_method(0, 0, 0.025, 1.4, f6, 10**-4)
qc = (value_ - value) / (value__ - value_)
_error = (value__ - value_) / 1
print("{} | {} | {}" .format(value, qc, _error))


def rk2(x0, y0, h, xf, function, error):
    while abs(xf - x0) > error:
        y0 += function(x0 + h/2, y0 + h/2*function(x0, y0))*h
        x0 += h
    return y0


value = rk2(0, 0, 0.1, 1.4, f6, 10**-4)
value_ = rk2(0, 0, 0.05, 1.4, f6, 10**-4)
value__ = rk2(0, 0, 0.025, 1.4, f6, 10**-4)
qc = (value_ - value) / (value__ - value_)
_error = (value__ - value_) / 3
print("{} | {} | {}" .format(value, qc, _error))


def d1(x, y, function, h):
    return h*function(x, y)


def d2(x, y, function, h):
    return h * function(x + h/2, y + (d1(x, y, function, h) / 2))


def d3(x, y, function, h):
    return h * function(x + h/2, y + (d2(x, y, function, h) / 2))


def d4(x, y, function, h):
    return h * function(x + h, y + d3(x, y, function, h))


def delta_y(x, y, function, h):
    return 1/6*d1(x, y, function, h) + 1/3*d2(x, y, function, h)+ 1/3*d3(x, y, function, h) + 1/6*d4(x, y, function, h)


def rk4(x0, y0, h, xf, function, error):
    while abs(xf - x0) > error:
        y0 += delta_y(x0, y0, function, h)
        x0 += h
    return y0


_h = 0.1
ordem = 4
value = rk4(0, 0, _h, 1.4, f6, 10**-4)
value_ = rk4(0, 0, _h / 2, 1.4, f6, 10**-4)
value__ = rk4(0, 0, _h / 4, 1.4, f6, 10**-4)
qc = (value_ - value) / (value__ - value_)
print("{} | {} | {}" .format(value, value_, value__))
while int(qc+0.5) != 2**ordem:
    print("h = {0} | h' = {1} | h'' = {2}" .format(_h / 2, _h / 4, _h / 8))
    _h /= 2
    value = value_
    value_ = value__
    value__ = rk4(0, 0, _h / 4, 1.4, f6, 10**-4)
    qc = (value_ - value) / (value__ - value_)
_error = (value__ - value_) / 15
print("{} | {} | {}" .format(value, qc, _error))


B = (m.sqrt(5) - 1) / 2
A = B**2


def minimum_aurea(x1, x2, function, error):
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
    return x1


def maximum_aurea(x1, x2, function, error):
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        if function(x3) > function(x4):
            x2 = x4
        else:
            x1 = x3
    return x1


def function_aurea(x):
    return (2 * x**2 + 1) - 5*m.cos(10*x)


min_x = minimum_aurea(-1, 0, function_aurea, 10 ** -4)
max_x = maximum_aurea(-1, 0, function_aurea, 10 ** -4)
print("Regra aurea :")
print("Minimum = {}\nMaximum = {}" .format(min_x, max_x))


def optimization_multidimensional(x, y, function, gradient, error):
    xn = x
    yn = y
    y = yn + 10*error
    x = xn + 10*error
    h = 1
    while abs(xn - x) > error or abs(yn - y) > error:
        x = xn
        y = yn
        xn = x - h * gradient[0](x, y)
        yn = y - h * gradient[1](x, y)
        if function(xn, yn) < function(x, y):
            h *= 2
        else:
            h /= 2
    return x, y


def func(x, y):
    return y**2 - 2 * x * y + 2 * x**2 - 6*y + 12


def d_func_dx(x, y):
    return -2*y + 4*x


def d_func_dy(x, y):
    return 2*y - 2*x - 6


x_value, y_value = optimization_multidimensional(1, 1, func, [d_func_dx, d_func_dy], 10 ** -4)
print("Optimization multidimensional:\nx = {} | y = {} | f(x, y) = {}" .format(x_value, y_value, func(x_value, y_value)))


def func_q(x, y):
    return y ** 2 - 2 * x * y - 6 * y + 2 * (x ** 2) + 12 + m.cos(4 * x)


import numpy as np


def quadratic_method(x, y, function, gradient, delta, error):
    xn = x
    yn = y
    x = xn + 10 * error
    y = yn + 10 * error
    while abs(xn - x) > error or abs(yn - y) > error:
        x = xn
        y = yn
        print(np.dot(delta(x, y), gradient(x, y))[0])
        input()
        xn = x - np.dot(delta(x, y), gradient(x, y))[0]
        yn = y - np.dot(delta(x, y), gradient(x, y))[1]
        if func_q(xn, yn) > func_q(x, y):
            xn -= 1
            yn -= 1
    return x, y


def h_inv(x, y):
    return [[-1 / (16*m.cos(4*x) - 2), -1 / (16*m.cos(4*x) - 2)], [-1 / (16*m.cos(4*x) - 2), (4* m.cos(4*x) - 1) / (8*m.cos(4*x) - 1)]]


def gradient_q(x, y):
    return [-2*y + 4*x -4*m.sin(4*x), 2*y-2*x-6]


x_value, y_value = quadratic_method(1, 1, func_q, gradient_q, h_inv,  10*-4)
print("Quadratic method:\nx = {} | y = {} | f(x, y) = {}" .format(x_value, y_value, func_q(x_value, y_value)))
