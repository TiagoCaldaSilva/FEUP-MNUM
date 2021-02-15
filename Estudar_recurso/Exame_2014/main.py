import math as m


def ex1_dfv(t, x, v):
    return (-v - 20 * x)/20


def ex1_dfx(t, x, v):
    return v


def euler_system(x, xf, y, z, functions, h, error, it):
    _it = 0
    while abs(xf - x) > error and _it != it:
        print(x, y, z, _it)
        y_old = y
        y += functions[0](x, y, z) * h
        z += functions[1](x, y_old, z) * h
        x += h
        _it += 1
    print(x, y, z, _it)
    return y

print("Solução da pergunta 1.3")
euler_system(0, 1.6, 1, 0, [ex1_dfx, ex1_dfv], 0.1, 10**-4, 100000)


def newton(guess, function, diff, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        print(guess, new_guess, function(new_guess), _it)
        guess = new_guess
        new_guess = guess - (function(guess) / diff(guess))
        _it += 1
    print(guess, new_guess, function(guess), _it)
    return new_guess


def ex2_g(x):
    return -x + 40*m.cos(m.sqrt(x)) + 3


def ex2_dg(x):
    return -20*m.sin(m.sqrt(x))/m.sqrt(x) - 1


print("EX2:")
newton(1.7, ex2_g, ex2_dg, 10**-4, 2 )


def aurea(x1, x2, function, error, it):
    _it = 0
    B = (m.sqrt(5) - 1) / 2
    A = B**2
    while abs(x1 - x2) > error and _it != it:
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        print(x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4), _it)
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
        _it += 1
    print(x1, x2, x3, x4, function(x1), function(x2), function(x3), function(x4), _it)
    print("Amplitude = {}".format(abs(x1 - x2)))
    return x1, x2


def ex5_f(x):
    return 5*m.cos(x) - m.sin(x)


print("EX5:")
aurea(2, 4, ex5_f, 10**-4, 3)


def ex7_g(x):
    return (4*x**3 - x + 3)**(1/4)


def picard_peano(guess, g, error, it):
    _it = 0
    new_guess = guess
    guess += error * 10
    while abs(new_guess - guess) > error and _it != it:
        print(new_guess, g(new_guess), _it)
        guess = new_guess
        new_guess = g(guess)
        _it += 1
    print(new_guess, g(new_guess), _it)
    return new_guess


print("EX7:")
picard_peano(3.5, ex7_g, 10**-4, 2)


