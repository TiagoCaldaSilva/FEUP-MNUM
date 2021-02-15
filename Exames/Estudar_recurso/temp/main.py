import math as m


def quadratic(x, y, gradient_xy, hessian, error, it):
    x_old = x + 10 * error
    y_old = y + 10 * error
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        det = hessian[0][0](x_old, y_old) * hessian[1][1](x_old, y_old) - hessian[1][0](x_old, y_old) * hessian[0][1](x_old, y_old)
        x -= (hessian[1][1](x_old, y_old) * gradient_xy[0](x_old, y_old) - hessian[0][1](x_old, y_old) * gradient_xy[1](x_old, y_old)) / det
        y -= (hessian[0][0](x_old, y_old) * gradient_xy[1](x_old, y_old) - hessian[0][1](x_old, y_old) * gradient_xy[0](x_old, y_old)) / det
        # _it += 1
    return x, y


def f(x, y):
    return y**2 - 2*x*y - 6*y + 2*x**2 + 12 + m.cos(4*x)


def fx(x, y):
    return -2*y + 4*x - 4*m.sin(4*x)


def fy(x, y):
    return 2*y - 2*x -6


def fxx(x, y):
    return 5 - 16*m.cos(4*x)


def fxy(x, y):
    return -2


def fyy(x, y):
    return 2


print(quadratic(1, 1, [fx, fy], [[fxx, fxy], [fxy, fyy]], 10**-4, 100))


def levenberg(x, y, h, g, lam, fu, error):
    x_old = x + 10 * error
    y_old = y + 10 * error
    while abs(x - x_old) > error or abs(y - y_old) > error:
        x_old = x
        y_old = y
        det = h[0][0](x_old, y_old)*h[1][1](x_old, y_old) - h[1][0](x_old, y_old)*h[0][1](x_old, y_old)
        quad1 = (h[1][1](x_old, y_old)*g[0](x_old, y_old) - h[0][1](x_old, y_old)*g[1](x_old, y_old)) / det
        quad2 = (h[0][0](x_old, y_old)*g[1](x_old, y_old) - h[0][1](x_old, y_old)*g[0](x_old, y_old)) / det
        x -= (quad1 + lam*g[0](x_old, y_old))
        y -= (quad2 + lam*g[1](x_old, y_old))
        if fu(x, y) < fu(x_old, y_old):
            lam /= 2
        else:
            lam *= 2
    print(fu(x, y))
    return x, y


def g(x, y):
    return (x + 1)**2 + (y-4)**2


def gx(x, y):
    return 2*x + 2


def gy(x, y):
    return 2*y - 8


def gxx(x, y):
    return 2


def gyy(x, y):
    return 2


def gxy(x, y):
    return 0


print(levenberg(1,1, [[fxx, fxy], [fxy, fyy]], [fx, fy], 0.05, f, 10**-4))
print(levenberg(0,0, [[gxx, gxy], [gxy, gyy]], [gx, gy], 0.05, g, 10**-4))


# EX 2
F = [0.0, 0.30, 0.60, 0.90, 1.20, 1.50, 1.80, 2.1, 2.4]
alpha = [0.0, 0.07, 0.13, 0.20, 0.26, 0.33, 0.40, 0.46, 0.53]


def trap(F, alpha, h):
    area = 0
    for i in range(0, len(F), h):
        if i == 0 or i == len(F)-1:
            area += F[i]*m.cos(alpha[i])
        else :
            area += 2*F[i]*m.cos(alpha[i])
    return area * 2.0*  m.pi * h/2.0

#Resolveu-se com a regra dos trapézios com h = 4, h' = 2, h'' = 1
# seja S o resultado com h, S' com h' e S'' com h'':
s = trap(F, alpha, 4)
s1 = trap(F, alpha, 2)
s2 = trap(F, alpha, 1)
qc = (s1-s)/(s2-s1)
e = (s2-s1)/3.0
print("s =", s)
print("s' =", s1)
print("s'' =", s2)
print("Qc =", qc)
#que nao é exatamente aproximado a 4 (2^ordem do método) logo não
#se pode estimar o erro. Calcula-se na mesma mas é de menção que teóricamente
#só se pode estimar se o quociente de convergência for aproximadamente 4
print("e'' =", e, "\n")


