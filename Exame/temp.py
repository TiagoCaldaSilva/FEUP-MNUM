import math as m


def g(x):
    f = 0.45 * int(x)
    alpha = 0
    for i in range(int(x)):
        if i % 2 or i == 0:
            alpha += 0.07
        else:
            alpha += 0.06
    if x - int(x):
        f += 0.23
        if int(x) % 2:
            alpha += 0.04
        else:
            alpha += 0.03

    
def trap():
    result =  0 + 3.6*m.cos(0.54)
    result += 0.45*m.cos(0.07)
    result += 0.9*m.cos(0.14)
    result += 1.13*m.cos(0.17)
    result += 1.35*m.cos(0.2)
    result += 1.58*m.cos(0.24)
    result += 1.8*m.cos(0.27)
    result += 2.03*m.cos(0.3)
    result += 2.25*m.cos(0.34)
    result += 2.48*m.cos(0.37)
    result += 2.7*m.cos(0.41)
    result += 3.15*m.cos(0.47)
    result += 3.6*m.cos(0.54)
    return result * 2 * m.pi

print(trap())


def f(x):
    return x**3 + 2*x**2 + 10*x - 23


def dif_f(x):
    return 3*x**2 + 4*x + 10


def newton(x, dif, f, it):
    _it = 0
    while _it != it:
        print(_it, x)
        x -= f(x) / dif(x)
        _it += 1
        
        
newton(0, dif_f, f, 3)
