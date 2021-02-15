import math as m


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


def ex1_f(x):
    return (x - 3.6) + ((m.cos(x + 1.2)) **3)


def ex1_df(x):
    return 1 - 3*((m.cos(x + 1.2))**2)*m.sin(x + 1.2)


newton(0.5, ex1_f, ex1_df, 10**-4, 1)
