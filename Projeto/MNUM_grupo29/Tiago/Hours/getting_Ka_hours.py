import math as m


ERROR = 10 ** -4

ket = 0.064 * 60  # hour^-1
tMax = 2  # hour


# Methods used to discover Ka


def bisection_method(a, b, function, error):
    counter = 0
    while abs(a - b) > error:
        middle = (a + b) / 2
        if function(a) * function(middle) < 0:
            b = middle
        else:
            a = middle
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
    return m.exp(-tMax * ka) - 2 * ka * m.exp(-tMax * ka)


def function_g(ka):
    return - m.log(0.001773983611321541 / ka) / 2


def function_g2(ka):
    return (ket * m.exp(-ket * tMax)) / m.exp(-ka * tMax)


print("\n1 Zero:\n")
temp_ka = bisection_method(0.001, 0.002, function_ka, ERROR)
print("Bisection: {}".format(temp_ka))
temp_ka = rope_method(0.001, 0.002, function_ka, ERROR)
print("Rope: {}".format(temp_ka))
temp_ka = newtons_method(0.0015, function_ka, diff_function_ka, ERROR)
print("Newton: {}".format(temp_ka))
temp_ka = picard_peano_method(0.0010, function_g2, ERROR)
print("Picard-peano: {}".format(temp_ka))

# Valor do maxima = 0.001780311356330923

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
