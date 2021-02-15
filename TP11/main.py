import math as m
# import numpy as np


def f(x):
    return x * m.exp(x**2 - 4) - 1


def df_dx(x):
    return m.exp(x**2 - 4) - 1 + x*(2*x*m.exp(x**2 - 4))


def bisection_method(a, b, function, error):
    xn_ = (a + b) / 2
    xn = xn_ + 1
    counter = 0
    while abs(xn_ - xn) > error:
        xn = xn_
        if function(xn_) * function(a) > 0:
            a = xn_
        else:
            b = xn_
        counter += 1
        xn_ = (a + b) / 2
    return xn, counter


def rope_method(a, b, function, error):
    xn_ = (a * function(b) - b * function(a)) / (function(b) - function(a))
    xn = xn_ + 1
    counter = 0
    while abs(xn_ - xn) > error:
        xn = xn_
        if function(xn_) * function(a) < 0:
            b = xn_
        else:
            a = xn_
        xn_ = (a * function(b) - b * function(a)) / (function(b) - function(a))
        counter += 1
    return xn, counter


def newtons_method(guess, error, function, dif):
    xn = guess
    xn_ = xn - function(xn) / dif(xn)
    counter = 0
    while abs(xn_ - xn) > error:
        counter += 1
        xn = xn_
        xn_ = xn - function(xn) / dif(xn)
    return xn_, counter


value, iterations = bisection_method(1.5, 2, f, 10**-4)
print("Bisection method: {} | iterations: {}".format(value, iterations))
value, iterations = rope_method(1.5, 2, f, 10**-4)
print("Rope method: {} | iterations: {}" .format(value, iterations))
value, iterations = newtons_method(2, 10**-4, f, df_dx)
print("Newtons method: {} | iterations: {}" .format(value, iterations))


def dy_dx(x, y, z):
    return z


def dz_dx(x, y, z):
    return x - 8*y


def euler_method(x_min, x_max, y0, z0, h, error, dif_y, dif_z):
    counter = 0
    while (x_min < x_max) and (abs(x_max - x_min) > error):
        yn = y0 + h * dif_y(x_min, y0, z0)
        zn = z0 + h * dif_z(x_min, y0, z0)
        x_min += h
        y0 = yn
        z0 = zn
        counter += 1

    return y0, z0, counter


value_y, value_z, iterations = euler_method(0, 0.25, -1, 0, 0.025, 10**-4, dy_dx, dz_dx)
print("Euler method: y = {} | z = {} | iterations = {}" .format(value_y, value_z, iterations))
value_y_, value_z_, iterations = euler_method(0, 0.25, -1, 0, 0.025 / 2, 10 ** -4, dy_dx, dz_dx)
print("y' = {} | z' = {} | iterations = {}" .format(value_y_, value_z_, iterations))
value_y__, value_z__, iterations = euler_method(0, 0.25, -1, 0, 0.025 / 4, 10 ** -4, dy_dx, dz_dx)
print("y' = {} | z' = {} | iterations = {}" .format(value_y__, value_z__, iterations))
qcy = (value_y_ - value_y) / (value_y__ - value_y_)
qcz = (value_z_ - value_z) / (value_z__ - value_z_)
print("QCY = {} | QCZ = {}" .format(qcy, qcz))
error_y, error_z = (value_y__ - value_y_), (value_z_ - value_z__)
print("ERROR_Y = {} | ERROR_Z = {}".format(error_y, error_z))


def rk2(x_min, x_max, y0, z0, h, error, dif_y, dif_z):
    counter = 0
    while (abs(x_max - x_min) > error) and x_min < x_max:
        yn = y0 + h * dif_y(x_min + h/2, y0 + h*dif_y(x_min, y0, z0)/2, z0 + h*dif_z(x_min, y0, z0)/2)
        zn = z0 + h * dif_z(x_min + h / 2, y0 + h * dif_y(x_min, y0, z0) / 2, z0 + h * dif_z(x_min, y0, z0) / 2)
        x_min += h
        y0 = yn
        z0 = zn
        counter += 1
    return y0, z0, counter


value_y, value_z, iterations = rk2(0, 0.25, -1, 0, 0.025, 10**-4, dy_dx, dz_dx)
print("Rk2 method: y = {} | z = {} | iterations = {}" .format(value_y, value_z, iterations))
value_y_, value_z_, iterations = rk2(0, 0.25, -1, 0, 0.025 / 2, 10 ** -4, dy_dx, dz_dx)
print("y' = {} | z' = {} | iterations = {}" .format(value_y_, value_z_, iterations))
value_y__, value_z__, iterations = rk2(0, 0.25, -1, 0, 0.025 / 4, 10 ** -4, dy_dx, dz_dx)
print("y' = {} | z' = {} | iterations = {}" .format(value_y__, value_z__, iterations))
qcy = (value_y_ - value_y) / (value_y__ - value_y_)
qcz = (value_z_ - value_z) / (value_z__ - value_z_)
print("QCY = {} | QCZ = {}" .format(qcy, qcz))
error_y, error_z = (value_y__ - value_y_) / 3, (value_z_ - value_z__) / 3
print("ERROR_Y = {} | ERROR_Z = {}".format(error_y, error_z))


def rk4_delta_1(x, y, z, h, c):
    if c == 'y':
        return h * dy_dx(x, y, z)
    return h*dz_dx(x, y, z)


def rk4_delta_2(x, y, z, h,  c):
    if c == 'y':
        return h * dy_dx(x + h/2, y + rk4_delta_1(x, y, z, h, c) / 2, z + rk4_delta_1(x, y, z, h, 'z') / 2)
    return h * dz_dx(x + h/2, y + rk4_delta_1(x, y, z, h, 'y') / 2, z + rk4_delta_1(x, y, z, h, c) / 2)


def rk4_delta_3(x, y, z, h, c):
    if c == 'y':
        return h * dy_dx(x + h/2, y + rk4_delta_2(x, y, z, h, c) / 2, z + rk4_delta_2(x, y, z, h, 'z') / 2)
    return h * dz_dx(x + h/2, y + rk4_delta_2(x, y, z, h, 'y') / 2, z + rk4_delta_2(x, y, z, h, c) / 2)


def rk4_delta_4(x, y, z, h, c):
    if c == 'y':
        return h * dy_dx(x + h, y + rk4_delta_3(x, y, z, h, c), z + rk4_delta_3(x, y, z, h, 'z'))
    return h * dz_dx(x + h, y + rk4_delta_3(x, y, z, h, 'y'), z + rk4_delta_3(x, y, z, h, c))


def rk4(x_min, x_max, y0, z0, h, error, dif_y, dif_z):
    counter = 0
    while (abs(x_max - x_min) > error) and x_min < x_max:
        yn = y0 + (1/6) * rk4_delta_1(x_min, y0, z0, h, 'y') + (1/3) * rk4_delta_2(x_min, y0, z0, h, 'y') + (1/3) * rk4_delta_3(x_min, y0, z0, h, 'y') + (1/6) * rk4_delta_4(x_min, y0, z0, h, 'y')
        zn = z0 + (1/6) * rk4_delta_1(x_min, y0, z0, h, 'z') + (1/3) * rk4_delta_2(x_min, y0, z0, h, 'z') + (1/3) * rk4_delta_3(x_min, y0, z0, h, 'z') + (1/6) * rk4_delta_4(x_min, y0, z0, h, 'z')
        x_min += h
        y0 = yn
        z0 = zn
        counter += 1
    return y0, z0, counter


test_x_ = 0
text_x = 0.25
test_y = -1
test_z = 0
_h = 0.025
err = 10**-4
value_y, value_z, iterations = rk4(test_x_, text_x, test_y, test_z, _h, err, dy_dx, dz_dx)
print("Rk4 method: y = {} | z = {} | iterations = {}" .format(value_y, value_z, iterations))
value_y_, value_z_, iterations = rk4(test_x_, text_x, test_y, test_z, _h / 2, err, dy_dx, dz_dx)
print("y' = {} | z' = {} | iterations = {}" .format(value_y_, value_z_, iterations))
value_y__, value_z__, iterations = rk4(test_x_, text_x, test_y, test_z, _h / 4, err, dy_dx, dz_dx)
print("y' = {} | z' = {} | iterations = {}" .format(value_y__, value_z__, iterations))
qcy = (value_y_ - value_y) / (value_y__ - value_y_)
qcz = (value_z_ - value_z) / (value_z__ - value_z_)
print("QCY = {} | QCZ = {}" .format(qcy, qcz))
error_y, error_z = (value_y__ - value_y_) / 15, (value_z_ - value_z__) / 15
print("ERROR_Y = {} | ERROR_Z = {}".format(error_y, error_z))

B = (m.sqrt(5) - 1) / 2
A = B * B


def g(x):
    return (x - 5)**2 + m.sin(7*x)


def minimum(x1, x2, error, function):
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
    return x1


def maximum(x1, x2, error, function):
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        if function(x3) > function(x4):
            x2 = x4
        else:
            x1 = x3
    return x1


min_x = -1
max_x = 0
err = 10 ** -4
result = minimum(min_x, max_x, err, g)
print("Minimum: {}".format(result))
result = maximum(min_x, max_x, err, g)
print("Maximum: {}".format(result))
