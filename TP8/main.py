def f(x, y, z):
    # return z * y + x
    return z


def g(x, y, z):
    # return z * x + y
    return x - 3 * z - 2 * y


def euler_method(x0, y, z, h, xf):
    while (x0 < xf) & (abs(xf - x0) > 0.00001):
        xn = x0
        yn = y
        zn = z
        x0 = xn + h
        y = yn + h * f(xn, yn, zn)
        z = zn + h * g(xn, yn, zn)
    return y, z


def rk2(x0, y, z, h, xf):
    while (x0 < xf) & (abs(xf - x0) > 0.00001):
        xn = x0
        yn = y
        zn = z
        x0 = xn + h
        y = yn + h * f(xn + h / 2, yn + h / 2 * f(xn, yn, zn), zn + h / 2 * g(xn, yn, zn))
        z = zn + h * g(xn + h / 2, yn + h / 2 * f(xn, yn, zn), zn + h / 2 * g(xn, yn, zn))
    return y, z


def d1(x, y, z, h, i):
    if i == 'y':
        return h * f(x, y, z)
    return h * g(x, y, z)


def d2(x, y, z, h, i):
    if i == 'y':
        return h * f(x + h / 2, y + d1(x, y, z, h, i) / 2, z + d1(x, y, z, h, 'z') / 2)
    return h * g(x + h / 2, y + d1(x, y, z, h, 'y') / 2, z + d1(x, y, z, h, i) / 2)


def d3(x, y, z, h, i):
    if i == 'y':
        return h * f(x + h / 2, y + d2(x, y, z, h, i) / 2, z + d2(x, y, z, h, 'z') / 2)
    return h * g(x + h / 2, y + d2(x, y, z, h, 'y') / 2, z + d2(x, y, z, h, i) / 2)


def d4(x, y, z, h, i):
    if i == 'y':
        return h * f(x + h, y + d3(x, y, z, h, i), z + d3(x, y, z, h, 'z'))
    return h * g(x + h, y + d3(x, y, z, h, 'y'), z + d3(x, y, z, h, i))


def rk4(x0, y, z, h, xf):
    while (x0 < xf) & (abs(xf - x0) > 0.00001):
        xn = x0
        yn = y
        zn = z
        x0 = xn + h
        y = yn + (1 / 6) * d1(xn, yn, zn, h, 'y') + (1 / 3) * d2(xn, yn, zn, h, 'y') + (1 / 3) * d3(xn, yn, zn, h, 'y') + (1 / 6) * d4(xn, yn, zn, h, 'y')
        z = zn + (1 / 6) * d1(xn, yn, zn, h, 'z') + (1 / 3) * d2(xn, yn, zn, h, 'z') + (1 / 3) * d3(xn, yn, zn, h, 'z') + (1 / 6) * d4(xn, yn, zn, h, 'z')
    return y, z


_x0 = 0
_y0 = 0
_z0 = 0
# EULER
_h = 0.025
order = 1
print("EULER METHOD:")
_y, _z = euler_method(_x0, _y0, _z0, _h, 0.5)
_y_, _z_ = euler_method(_x0, _y0, _z0, _h / 2, 0.5)
_y__, _z__ = euler_method(_x0, _y0, _z0, _h / 4, 0.5)
qcy = (_y_ - _y) / (_y__ - _y_)
while int(qcy + 0.5) != 2 ** order:
    _h = _h / 2
    _y = _y_
    _y_ = _y__
    _z = _z_
    _z_ = _z__
    _y__, _z__ = rk4(_x0, _y0, _z0, _h / 4, 0.5)
    qcy = (_y_ - _y) / (_y__ - _y_)
qcz = (_z_ - _z) / (_z__ - _z_)
error_y = (_y__ - _y_)  / (2 ** order - 1)
error_z = (_z__ - _z_) / (2 ** order - 1)
print("Y = {} | Z = {}".format(_y, _z))
print("Y' = {} | Z' = {}".format(_y_, _z_))
print("Y'' = {} | Z'' = {}".format(_y__, _z__))
print("H = {} | QCY = {} | QCZ = {}".format(_h, qcy, qcz))
print("ERROR_Y = {} | ERROR_Z = {}".format(error_y, error_z))
# RK2
print("RK2:")
_h = 0.025
order = 2
_y, _z = rk2(_x0, _y0, _z0, _h, 0.5)
_y_, _z_ = rk2(_x0, _y0, _z0, _h / 2, 0.5)
_y__, _z__ = rk2(_x0, _y0, _z0, _h / 4, 0.5)
qcy = (_y_ - _y) / (_y__ - _y_)
while int(qcy + 0.5) != 2 ** order:
    _h = _h / 2
    _y = _y_
    _y_ = _y__
    _z = _z_
    _z_ = _z__
    _y__, _z__ = rk4(_x0, _y0, _z0, _h / 4, 0.5)
    qcy = (_y_ - _y) / (_y__ - _y_)
qcz = (_z_ - _z) / (_z__ - _z_)
error_y = (_y__ - _y_) / (2 ** order - 1)
error_z = (_z__ - _z_) / (2 ** order - 1)
print("Y = {} | Z = {}".format(_y, _z))
print("Y' = {} | Z' = {}".format(_y_, _z_))
print("Y'' = {} | Z'' = {}".format(_y__, _z__))
print("H = {} | QCY = {} | QCZ = {}".format(_h, qcy, qcz))
print("ERROR_Y = {} | ERROR_Z = {}".format(error_y, error_z))

# RK4
_h = 0.025
order = 4
print("RK4:")
_y, _z = rk4(_x0, _y0, _z0, _h, 0.5)
_y_, _z_ = rk4(_x0, _y0, _z0, _h / 2, 0.5)
_y__, _z__ = rk4(_x0, _y0, _z0, _h / 4, 0.5)
qcy = (_y_ - _y) / (_y__ - _y_)
while int(qcy + 0.5) != 2 ** order:
    _h = _h / 2
    _y = _y_
    _y_ = _y__
    _z = _z_
    _z_ = _z__
    _y__, _z__ = rk4(_x0, _y0, _z0, _h / 4, 0.5)
    qcy = (_y_ - _y) / (_y__ - _y_)
qcz = (_z_ - _z) / (_z__ - _z_)
error_y = (_y__ - _y_) / (2 ** order - 1)
error_z = (_z__ - _z_) / (2 ** order - 1)
print("Y = {} | Z = {}".format(_y, _z))
print("Y' = {} | Z' = {}".format(_y_, _z_))
print("Y'' = {} | Z'' = {}".format(_y__, _z__))
print("H = {} | QCY = {} | QCZ = {}".format(_h, qcy, qcz))
print("ERROR_Y = {} | ERROR_Z = {}".format(error_y, error_z))
