import math as m


# Valores para h = 1, h = 2 e h = 4 no intervalo [0, 8]
function_values = [0, 0.45, 0.9, 1.35, 1.8, 2.25, 2.7, 3.15, 3.6]
ang_values = [0, 0.07, 0.14, 0.2, 0.27, 0.34, 0.41, 0.47, 0.54]

# # Valores para h = 0.5 no intervalo [2, 6]
# function_values_2 = [0.9,  1.13, 1.35, 1.58, 1.8, 2.03, 2.25, 2.48, 2.7]
# ang_values_2 = [0.14, 0.17, 0.2, 0.24, 0.27, 0.3, 0.34, 0.37, 0.41]
# # Valores para h = 2 e h = 1 no intervalo [2, 6]
# function_values_22 = [0.9, 1.35, 1.8, 2.25, 2.7]
# ang_values_22 = [0.14, 0.2, 0.27, 0.34, 0.41]
#
#
# def simpson_2(h):
#     result = 0
#     for i in range(0, 9):
#         if i == 0 or i == 8:
#             result += function_values_2[i] * m.cos(ang_values_2[i])
#         elif i % 2:
#             result += 4 * function_values_2[i] * m.cos(ang_values_2[i])
#         else:
#             result += 2*function_values_2[i]*m.cos(ang_values_2[i])
#     print(2 * m.pi * result * h / 3, result * h / 3)
#     # return 2 * m.pi * result * h / 2
#     return result * h / 3
#
#
# def simpson_22(h):
#     result = 0
#     for i in range(0, len(function_values_22), h):
#         if i == 0 or i == len(function_values_22) - 1:
#             result += function_values_22[i] * m.cos(ang_values_22[i])
#         elif i % 2:
#             result += 4 * function_values_22[i] * m.cos(ang_values_22[i])
#         else:
#             result += 2*function_values_22[i]*m.cos(ang_values_22[i])
#     print(2 * m.pi * result * h / 3, result * h / 3)
#     # return 2 * m.pi * result * h / 2
#     return result * h / 3


def simpson(h):
    result = 0
    _it = 0
    for i in range(0, 9, h):
        if i == 0 or i == 8:
            result += function_values[i] * m.cos(ang_values[i])
        elif _it % 2:
            result += 4 * function_values[i] * m.cos(ang_values[i])
        else:
            result += 2*function_values[i]*m.cos(ang_values[i])
        _it += 1
    print(2 * m.pi * result * h / 3, result * h / 3)
    return 2 * m.pi * result * h / 3


print("EX2:")
s = simpson(4)
s_ = simpson(2)
s__ = simpson(1)
qc = (s_ - s)/(s__ - s_)
error = (s__ - s_) / 15
print(qc, error)
# print("Trap2")
# s = simpson_22(2)
# s_ = simpson_22(1)
# s__ = simpson_2(0.5)
# qc = (s_ - s)/(s__ - s_)
# error = (s__ - s_) / 3
# print(qc, error)


def gauss_seidel(x0, y0, z0, t0, matrix, b, error, it):
    _it = 0
    x = x0
    y = y0
    z = z0
    t = t0
    x0 += error * 10
    y0 += error * 10
    z0 += error * 10
    t0 += error * 10
    while (abs(x - x0) > error or abs(y - y0) > error or abs(z - z0) > error or abs(t - t0) > error) and _it != it:
        print(x, y, z, t, _it)
        x0 = x
        y0 = y
        z0 = z
        t0 = t
        x = (b[0] - matrix[0][1]*y0 - matrix[0][2]*z0 - matrix[0][3]*t0) / matrix[0][0]
        y = (b[1] - matrix[1][0]*x - matrix[1][2]*z0 - matrix[1][3]*t0) / matrix[1][1]
        z = (b[2] - matrix[2][0]*x - matrix[2][1]*y - matrix[2][3]*t0) / matrix[2][2]
        t = (b[3] - matrix[3][0]*x - matrix[3][1]*y - matrix[3][2]*z) / matrix[3][3]
        _it += 1
    print(x, y, z, t, _it)
    return x, y, z, t


print("EX3:")
gauss_seidel(0, 0, 0, 0, [[6, 0.5, 3, 0.25], [1.2, 3, 0.25, 0.2], [-1, 0.25, 4, 2], [2, 4, 1, 8]], [19, -2.2, 9, 15], 10**-4, 1)


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


def ex5_f(x):
    return x**3 + 2 * x**2 + 10*x - 23


def ex5_df(x):
    return 3*x**2 + 4*x + 10


print("EX5:")
newton(0, ex5_f, ex5_df, 10**-4, 2)
