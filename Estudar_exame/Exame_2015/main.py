import math as m


def ex1(t, ta):
    return -0.25*(t - ta)


def ex1_euler(t, T, ta, h, function, it):
    _it = 0
    while _it != it:
        print(_it, t, T, ta)
        _it += 1
        T += function(T, ta) * h
        t += h


ex1_euler(5, 3, 37, 0.4, ex1, 3)


def ex4_2(x):
    print(x)
    x = 2*m.log(2*x)
    print(x)


ex4_2(1.1)


def ex5_f(x):
    return m.sqrt(1 + (2.5 * m.exp(2.5 * x))**2)


def ex5_trap(x, xf, function, error, h):
    result = function(x) + function(xf)
    while abs(xf - x - h) > error:
        x += h
        result += 2 * function(x)
    return h / 2 * result


def ex5_simpson(x, xf, function, error, h):
    result = function(x) + function(xf)
    i = 0
    while abs(xf - x - h) > error:
        i += 1
        x += h
        if i % 2:
            result += 4 * function(x)
        else:
            result += 2 * function(x)
    return result * h / 3


value_trap = ex5_trap(0, 1, ex5_f, 10**-4, 0.125)
value_simpson = ex5_simpson(0, 1, ex5_f, 10**-4, 0.125)
print(value_trap, value_simpson)
value_trap_ = ex5_trap(0, 1, ex5_f, 10**-4, 0.125 / 2)
value_simpson_ = ex5_simpson(0, 1, ex5_f, 10**-4, 0.125 / 2)
print(value_trap_, value_simpson_)
value_trap__ = ex5_trap(0, 1, ex5_f, 10**-4, 0.125 / 4)
value_simpson__ = ex5_simpson(0, 1, ex5_f, 10**-4, 0.125 / 4)
print(value_trap__, value_simpson__)
qc_trap = (value_trap_ - value_trap) / (value_trap__ - value_trap_)
qc_simp = (value_simpson_ - value_simpson) / (value_simpson__ - value_simpson_)
print(qc_trap, qc_simp)
error_trap = (value_trap__ - value_trap_) / 3
error_simp = (value_simpson__ - value_simpson_) / 15
print(error_trap, error_simp)


def ex7_f(x):
    return x**3 - 10 * m.sin(x) + 2.8


def ex7_bisection(a, b, it, function):
    _it = 0
    print('\n')
    while _it <= it:
        middle = (a + b) / 2
        print(_it, a, b,  function(a), function(middle))
        if function(a) < function(middle):
            b = middle
        else:
            a = middle
        _it += 1


ex7_bisection(1.5, 4.2, 2, ex7_f)
