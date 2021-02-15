import math


def f(x_value, y_value):
    return math.exp(y_value - x_value)


# Deduzir expressões? que expressões?
# Se n for diferente de 2 temos de proceder de forma diferente
# (se n for par -> de forma recursiva, se n for ímpar -> deduzir expressões)


def trapezios(intg1_b, intg1_c, intg2_b, intg2_c, nx, ny):
    sum_v = 0
    sum_pi = 0
    vertices = [(intg1_b, intg2_c), (intg1_b, intg2_b), (intg1_c, intg2_c), (intg1_c, intg2_b)]
    pontos_int = [(intg1_b, intg2_c / 2), (intg1_c / 2, intg2_b), (intg1_c, intg2_c / 2), (intg1_c / 2, intg2_c)]
    central = (intg1_c / 2, intg2_c / 2)
    for i in range(0, len(vertices)):
        sum_v += f(vertices[i][0], vertices[i][1])
        sum_pi += f(pontos_int[i][0], pontos_int[i][1])
    sum_c = f(central[0], central[1])

    hx = (intg1_c - intg1_b) / nx
    hy = (intg2_c - intg2_b) / ny

    return ((hx * hy) / 4) * (sum_v + 2 * sum_pi + 4 * sum_c)


def simpson(intg1_b, intg1_c, intg2_b, intg2_c, nx, ny):
    sum_v = 0
    sum_pi = 0
    vertices = [(intg1_b, intg2_c), (intg1_b, intg2_b), (intg1_c, intg2_c), (intg1_c, intg2_b)]
    pontos_int = [(intg1_b, intg2_c / 2), (intg1_c / 2, intg2_b), (intg1_c, intg2_c / 2), (intg1_c / 2, intg2_c)]
    central = (intg1_c / 2, intg2_c / 2)
    for i in range(0, len(vertices)):
        sum_v += f(vertices[i][0], vertices[i][1])
        sum_pi += f(pontos_int[i][0], pontos_int[i][1])
    sum_c = f(central[0], central[1])

    hx = (intg1_c - intg1_b) / nx
    hy = (intg2_c - intg2_b) / ny

    return ((hx * hy) / 9) * (sum_v + 4 * sum_pi + 16 * sum_c)


def y_linha(_x, _y):
    return _x * _x + _y * _y


# A partir destes métodos a condição deveria ser enquanto que o valor de x que estamos
#   a alterar é diferente do valor máximo que queremos (x final)
# Mas como estámos a trabalhar com floats, podem haver erros ao fazer " while x0 < xf: ",
#   por isso temos de arranjar forma de solucionar o problema
# A minha foi usar o critério da convergência


def euler(x0, y0, xf, h):
    while abs(xf - x0) > 0.000001:
        y_ = y_linha(x0, y0)  # y_linha de x e n e nao de x(n+1) e y(n+1)
        x0 += h
        y0 = y0 + h * y_
    return y0


def rk2(x0, y0, xf, h):
    while abs(xf - x0) > 0.00001:
        temp_x = x0
        temp_y = y0
        x0 = temp_x + h
        y0 = temp_y + h * y_linha(temp_x + h/2, temp_y + h/2 * y_linha(temp_x, temp_y))
    return y0


def rk4(x0, y0, xf, h):
    while abs(xf - x0) > 0.00001:
        delta_1 = h * y_linha(x0, y0)
        delta_2 = h * y_linha(x0 + h / 2, y0 + delta_1 / 2)
        delta_3 = h * y_linha(x0 + h / 2, y0 + delta_2 / 2)
        delta_4 = h * y_linha(x0 + h, y0 + delta_3)
        x0 = x0 + h
        y0 += 1/6 * delta_1 + 1/3 * delta_2 + 1/3 * delta_3 + 1/6 * delta_4
    return y0


x = trapezios(0, 0.5, 0, 0.5, 2, 2)
print("Método dos Trapézios = ", x)
x_ = trapezios(0, 0.5, 0, 0.5, 4, 4)
print("Método dos Trapézios ' = ", x_)
x__ = trapezios(0, 0.5, 0, 0.5, 8, 8)
print("Método dos Trapézios '' = ", x__)
qc = (x_ - x) / (x__ - x_)
print("QC = ", qc)
nx = 2
ny = 2
x = simpson(0, 0.5, 0, 0.5, nx, ny)
print("Método de Simpson = ", x)
x_ = simpson(0, 0.5, 0, 0.5, 2*nx, 2*ny)
print("Método de Simpson ' = ", x_)
x__ = simpson(0, 0.5, 0, 0.5, 4*nx, 4*ny)
print("Método de Simpson '' = ", x__)
qc = (x_ - x) / (x__ - x_)
print("QC = ", qc)
print('\n')
_h = 0.1
x = euler(0, 0, 1.40000, _h)
print("Método de Euler = ", x)
x_ = euler(0, 0, 1.4, _h / 2)
print("Método de Euler ' = ", x_)
x__ = euler(0, 0, 1.4, _h / 4)
print("Método de Euler '' = ", x__)
qc = (x_ - x) / (x__ - x_)
print("QC = ", qc)
print("Como QC é igual à ordem do método, passo adequado = ", _h)
error__ = (x__ - x_)
print("Epsilon '' = ", error__)
print('\n')
_h = 0.1
x = rk2(0, 0, 1.4, _h)
print("RK2 = ", x)
x_ = rk2(0, 0, 1.4, _h / 2)
print("RK2 ' = ", x_)
x__ = rk2(0, 0, 1.4, _h / 4)
print("RK2 '' = ", x__)
qc = (x_ - x) / (x__ - x_)
print("QC = ", qc)
print("Como QC é igual à ordem do método, passo adequado = ", _h)
error__ = (x__ - x_) / 3
print("Epsilon '' = ", error__)
print('\n')
_h = 0.1
x = rk4(0, 0, 1.4, _h)
print("RK4 = ", x)
x_ = rk4(0, 0, 1.4, _h / 2)
print("RK4 ' = ", x_)
x__ = rk4(0, 0, 1.4, _h / 4)
print("RK4 '' = ", x__)
qc = (x_ - x) / (x__ - x_)
print("QC = ", qc)
error__ = (x__ - x_) / 15
print("Epsilon '' = ", error__)
_h = 0.1
print("\nComo QC é diferente de 16, temos de ajustar:")
while int(qc + 0.5) < 16:
    print("h = {0} | h' = {1} | h'' = {2}" .format(_h / 2, _h / 4, _h / 8))
    _h /= 2
    x = x_
    x_ = x__
    x__ = rk4(0, 0, 1.4, _h)
    qc = (x_ - x) / (x__ - x_)
print("QC = ", int(qc + 0.5))
print("Passo adequado = ", _h)
