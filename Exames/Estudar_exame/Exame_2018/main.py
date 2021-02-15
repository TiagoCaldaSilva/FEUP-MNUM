import math as m


def ex1_f1(x, y):
    return m.sin(x + y) - m.exp(x-y)


def ex1_f2(x, y):
    return m.cos(x + y) - (x**2)*(y**2)


def ex1_df1_dx(x, y):
    return m.cos(x + y) - m.exp(x + y)


def ex1_df1_dy(x, y):
    return m.cos(x + y) + m.exp(x - y)


def ex1_df2_dx(x, y):
    return -(m.sin(x + y) + 2*x*(y**2))


def ex1_df2_dy(x, y):
    return - (m.sin(x + y) + 2*(x**2)*y)


def newton_system(x, y, f1, df1, f2, df2, it):
    _it = 0
    while _it != it:
        print(_it, x, y)
        x_old = x
        y_old = y
        x = x_old - ((f1(x_old, y_old) * df2[1](x_old, y_old) - f2(x_old, y_old)*df1[1](x_old, y_old)) / (df1[0](x_old, y_old) * df2[1](x_old, y_old) - df1[1](x_old, y_old)*df2[0](x_old, y_old)))
        y = y_old - ((f2(x_old, y_old) * df1[0](x_old, y_old) - f1(x_old, y_old)*df2[0](x_old, y_old)) / (df1[0](x_old, y_old) * df2[1](x_old, y_old) - df1[1](x_old, y_old)*df2[0](x_old, y_old)))
        _it += 1


print("EX1:")
newton_system(0.5, 0.25, ex1_f1, [ex1_df1_dx, ex1_df1_dy], ex1_f2, [ex1_df2_dx, ex1_df2_dy], 3)


def ex4_fz(x, y, z):
    return -7 * z - 4 * y


def ex4_fy(x, y, z):
    return z


def ex4_euler(x, y, z, h, fy, fz, it):
    _it = 0
    while _it != it:
        print(_it, x, y, z)
        y_old = y
        y += h * fy(x, y_old, z)
        z += h * fz(x, y_old, z)
        x += h
        _it += 1


print("EX4:")
ex4_euler(0.4, 2, 1, 0.2, ex4_fy, ex4_fz, 4)


def ex5_f(x):
    return (x - 5)**2 + x**4


def ex5_aurea(x1, x2, function, error):
    B = (m.sqrt(5) - 1) / 2
    A = B**2
    while abs(x1 - x2) > error:
        x3 = x1 + A*(x2 - x1)
        x4 = x1 + B*(x2 - x1)
        if function(x3) < function(x4):
            x2 = x4
        else:
            x1 = x3
    print(x1, function(x1))


ex5_aurea(0.5, 2.5, ex5_f, 10**-4)
