import math as m
from numpy import arange
from matplotlib.pyplot import plot, show, scatter, xlabel, ylabel, legend


ERROR = 10 ** -4

ket = 0.064 * 60  # hour^-1
tMax = 2  # hour


# Methods used to discover Ka


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


def function_ka(ka):
    return ka * m.exp(-ka * tMax) - ket * m.exp(-ket * tMax)


def diff_function_ka(ka):
    return m.exp(-2 * ka) - 2 * ka * m.exp(-2 * ka)


def function_g(ka):
    return - m.log(0.001773983611321541 / ka) / 2


def function_g2(ka):
    return (ket * m.exp(-ket * tMax)) / m.exp(-ka * tMax);


print("\n1 Zero:\n")
temp_ka = bisection_method(0.001, 0.002, function_ka, ERROR)
print("Bisection: {}".format(temp_ka))
temp_ka = rope_method(0.001, 0.002, function_ka, ERROR)
print("Rope: {}".format(temp_ka))
temp_ka = newtons_method(0.0015, function_ka, diff_function_ka, ERROR)
print("Newton: {}".format(temp_ka))
temp_ka = picard_peano_method(0.0010, function_g2, ERROR)
print("Picard-peano: {}".format(temp_ka))

print("\n2 Zero:\n")
temp_ka = bisection_method(3.8, 3.9, function_ka, ERROR)
print("Bisection: {}".format(temp_ka))
temp_ka = rope_method(3.8, 3.9, function_ka, ERROR)
print("Rope: {}".format(temp_ka))
temp_ka = newtons_method(3.9, function_ka, diff_function_ka, ERROR)
print("Newton: {}".format(temp_ka))
temp_ka = picard_peano_method(3.9, function_g, ERROR)
print("Picard-peano: {}".format(temp_ka))

# Valor do maxima = 3.84

Ka = 3.84


def d(t):
    if t <= 96:  # 4 days
        while t >= 12:
            t -= 12
        if t <= 0.5:
            return 0
        elif 0.5 < t <= 2:
            return (500 * (t-0.5)) / 17.25
        elif 2 < t <= 12:
            return (-500 * (t-2)) / 115 + 1000 / 23
    else:
        return 0


# Methods used to discover the final values


def euler_method(x0, y, z, h, xf, diff_y, diff_z):
    list_x = [x0]
    list_y = [y]
    list_z = [z]
    while (x0 < xf) & (abs(xf - x0) > 0.00001):
        xn = x0
        yn = y
        zn = z
        x0 = xn + h
        y = yn + h * diff_y(xn, yn, zn)
        z = zn + h * diff_z(xn, yn, zn)
        list_x.append(x0)
        list_y.append(y)
        list_z.append(z)
    return y, z, list_x, list_y, list_z


def rk2(x0, y, z, h, xf, diff_y, diff_z):
    list_x = [x0]
    list_y = [y]
    list_z = [z]
    i = 0
    while (x0 < xf) & (abs(xf - x0) > 0.00001):
        i += 1
        xn = x0
        yn = y
        zn = z
        x0 = xn + h
        y = yn + h * diff_y(xn + h / 2, yn + h / 2 * diff_y(xn, yn, zn), zn + h / 2 * diff_z(xn, yn, zn))
        z = zn + h * diff_z(xn + h / 2, yn + h / 2 * diff_y(xn, yn, zn), zn + h / 2 * diff_z(xn, yn, zn))
        list_x.append(x0)
        list_y.append(y)
        list_z.append(z)
    return y, z, list_x, list_y, list_z


def d1(x, y, z, h, i, f, g):
    if i == 'y':
        return h * f(x, y, z)
    return h * g(x, y, z)


def d2(x, y, z, h, i, f, g):
    if i == 'y':
        return h * f(x + h / 2, y + d1(x, y, z, h, i, f, g) / 2, z + d1(x, y, z, h, 'z', f, g) / 2)
    return h * g(x + h / 2, y + d1(x, y, z, h, 'y', f, g) / 2, z + d1(x, y, z, h, i, f, g) / 2)


def d3(x, y, z, h, i, f, g):
    if i == 'y':
        return h * f(x + h / 2, y + d2(x, y, z, h, i, f, g) / 2, z + d2(x, y, z, h, 'z', f, g) / 2)
    return h * g(x + h / 2, y + d2(x, y, z, h, 'y', f, g) / 2, z + d2(x, y, z, h, i, f, g) / 2)


def d4(x, y, z, h, i, f, g):
    if i == 'y':
        return h * f(x + h, y + d3(x, y, z, h, i, f, g), z + d3(x, y, z, h, 'z', f, g))
    return h * g(x + h, y + d3(x, y, z, h, 'y', f, g), z + d3(x, y, z, h, i, f, g))


def rk4(x0, y, z, h, xf, diff_y, diff_z):
    list_x = [x0]
    list_y = [y]
    list_z = [z]
    i = 0
    result_mi = 0
    while (x0 < xf) & (abs(xf - x0) > 0.00001):
        i += 1
        xn = x0
        yn = y
        zn = z
        x0 = xn + h
        result_mi += y
        y = yn + (1 / 6) * d1(xn, yn, zn, h, 'y', diff_y, diff_z) + (1 / 3) * d2(xn, yn, zn, h, 'y', diff_y, diff_z) + (1 / 3) * d3(xn, yn, zn, h, 'y', diff_y, diff_z) + ( 1 / 6) * d4(xn, yn, zn, h, 'y', diff_y, diff_z)
        z = zn + (1 / 6) * d1(xn, yn, zn, h, 'z', diff_y, diff_z) + (1 / 3) * d2(xn, yn, zn, h, 'z', diff_y, diff_z) + (1 / 3) * d3(xn, yn, zn, h, 'z', diff_y, diff_z) + (1 / 6) * d4(xn, yn, zn, h, 'z', diff_y, diff_z)
        list_x.append(x0)
        list_y.append(y)
        list_z.append(z)
    print(i, result_mi, z)
    return y, z, list_x, list_y, list_z


def mi_eq(t, mi, mp):
    return d(t) - Ka * mi


def mp_eq(t, mi, mp):
    return Ka * mi - ket * mp


def plot_Dt(D, tf):
    instants = arange(0, tf, 0.1)
    dosages = [D(t) for t in instants]
    xlabel("time (h)")
    ylabel("Dosage D(t) (mg/h)")
    plot(instants, dosages)
    show()


plot_Dt(d, 9*12)


def runge_kutta2_higher_order(x0, y0, z0, xf, n, f, g):
    y = y0
    z = z0
    x = x0
    h = (xf-x0)/n
    list_x = [x0]
    list_y = [y]
    list_z = [z]

    for i in range(n):
        d1 = h * f(x, y, z)
        l1 = h * g(x, y, z)
        y_copy = y
        y = y + h * f(x + h/2.0, y + d1/2.0, z + l1/2.0)
        z = z + h * g(x + h/2.0, y_copy + d1/2.0, z + l1/2.0)
        x = x + h
        list_x.append(x)
        list_y.append(y)
        list_z.append(z)
    return y, z, list_x, list_y, list_z


# temp_ki, a, mylist = euler_method(0, 0, 0, 200, 72, mi_eq, mp_eq)
# print(temp_ki)
# t, mi, mp = rk2(0, 0, 0, 200, *24, mi_eq, mp_eq)
# plot(t, mi, label = "mi")
# plot(t, mp, label = "mp")
# legend()
# show()


# h = 0.0125
# _y, _z, temp_ki, a, mylist = rk4(0, 0, 0, h, 5*24, mi_eq, mp_eq)
# _y_, _z_, temp_ki_, a_, mylist_ = rk4(0, 0, 0, h / 2, 5*24, mi_eq, mp_eq)
# _y__, _z__, temp_ki__, a__, mylist__ = rk4(0, 0, 0, h / 4, 5*24, mi_eq, mp_eq)
# print((_y_ - _y) / (_y__ - _y_))

# h = 0.0125
# _y, _z, temp_ki, a, mylist = rk4(0, 0, 0, h, 6*24, mi_eq, mp_eq)
# _y_, _z_, temp_ki_, a_, mylist_ = rk4(0, 0, 0, h / 2, 6*24, mi_eq, mp_eq)
# _y__, _z__, temp_ki__, a__, mylist__ = rk4(0, 0, 0, h / 4, 6*24, mi_eq, mp_eq)
# print((_y_ - _y) / (_y__ - _y_))

h = 0.0125
_y, _z, temp_ki, a, mylist = rk2(0, 0, 0, h, 5*24, mi_eq, mp_eq)
_y_, _z_, temp_ki_, a_, mylist_ = rk2(0, 0, 0, h / 2, 5*24, mi_eq, mp_eq)
_y__, _z__, temp_ki__, a__, mylist__ = rk2(0, 0, 0, h / 4, 5*24, mi_eq, mp_eq)
print((_y_ - _y) / (_y__ - _y_))


# _y, _z, temp_ki, a, mylist = runge_kutta2_higher_order(0, 0, 0, 5*24, 240, mi_eq, mp_eq)


# h = 0.0018125
# _y, _z, temp_ki, a, mylist = euler_method(0, 0, 0, h, 5*24, mi_eq, mp_eq)
# _y_, _z_, temp_ki_, a_, mylist_ = euler_method(0, 0, 0, h / 2, 5*24, mi_eq, mp_eq)
# _y__, _z__, temp_ki__, a__, mylist__ = euler_method(0, 0, 0, h / 4, 5*24, mi_eq, mp_eq)
# print((_y_ - _y) / (_y__ - _y_))

# h = 0.0125
# _y, _z, temp_ki, a, mylist = rk4(0, 0, 0, h, 24, mi_eq, mp_eq)
# _y_, _z_, temp_ki_, a_, mylist_ = rk4(0, 0, 0, h / 2, 24, mi_eq, mp_eq)
# _y__, _z__, temp_ki__, a__, mylist__ = rk4(0, 0, 0, h / 4, 24, mi_eq, mp_eq)
# print((_y_ - _y) / (_y__ - _y_))

plot(temp_ki, a, label = "mi")
plot(temp_ki, mylist, label = "mp")
xlabel("time (h)")
ylabel("(mg)")
legend()
show()
