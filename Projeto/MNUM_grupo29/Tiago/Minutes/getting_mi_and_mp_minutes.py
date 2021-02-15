from numpy import arange
from matplotlib.pyplot import plot, show, xlabel, ylabel, legend

ket = 0.064
tMax = 120
Ka = 0.064


def d(t):
    if t <= 4*24*60:  # 4 days
        while t >= 12*60:
            t -= 12*60
        if t <= 30:
            return 0
        elif 30 < t <= 120:
            return (5 * (t-30)) / 621
        elif 120 < t <= 12*60:
            return (-1 * (t-120)) / 828 + 50/69
    else:
        return 0


# Methods used to discover the final values


# Methods used to discover the final values


def euler_method(t0, mi, mp, h, tf, diff_mi, diff_mp):
    list_t = [t0]
    list_mi = [mi]
    list_mp = [mp]
    while (t0 < tf) & (abs(tf - t0) > 0.00001):
        t_n = t0
        mi_n = mi
        mp_n = mp
        t0 = t_n + h
        mi = mi_n + h * diff_mi(t_n, mi_n, mp_n)
        mp = mp + h * diff_mp(t_n, mi_n, mp_n)
        list_t.append(t0)
        list_mi.append(mi)
        list_mp.append(mp)
    return mi, mp, list_t, list_mi, list_mp


def rk2(t0, mi, mp, h, tf, diff_mi, diff_mp):
    list_t = [t0]
    list_mi = [mi]
    list_mp = [mp]
    i = 0
    while (t0 < tf) & (abs(tf - t0) > 0.00001):
        i += 1
        t_n = t0
        mi_n = mi
        mp_n = mp
        t0 = t_n + h
        mi = mi_n + h * diff_mi(t_n + h / 2, mi_n + h / 2 * diff_mi(t_n, mi_n, mp_n), mp_n + h / 2 * diff_mp(t_n, mi_n, mp_n))
        mp = mp_n + h * diff_mp(t_n + h / 2, mi_n + h / 2 * diff_mi(t_n, mi_n, mp_n), mp_n + h / 2 * diff_mp(t_n, mi_n, mp_n))
        list_t.append(t0)
        list_mi.append(mi)
        list_mp.append(mp)
    return mi, mp, list_t, list_mi, list_mp


def d1(t, mi, mp, h, i, f, g):
    if i == 'mi':
        return h * f(t, mi, mp)
    return h * g(t, mi, mp)


def d2(t, mi, mp, h, i, f, g):
    if i == 'mi':
        return h * f(t + h / 2, mi + d1(t, mi, mp, h, i, f, g) / 2, mp + d1(t, mi, mp, h, 'mp', f, g) / 2)
    return h * g(t + h / 2, mi + d1(t, mi, mp, h, 'mi', f, g) / 2, mp + d1(t, mi, mp, h, i, f, g) / 2)


def d3(t, mi, mp, h, i, f, g):
    if i == 'mi':
        return h * f(t + h / 2, mi + d2(t, mi, mp, h, i, f, g) / 2, mp + d2(t, mi, mp, h, 'mp', f, g) / 2)
    return h * g(t + h / 2, mi + d2(t, mi, mp, h, 'mi', f, g) / 2, mp + d2(t, mi, mp, h, i, f, g) / 2)


def d4(t, mi, mp, h, i, f, g):
    if i == 'mi':
        return h * f(t + h, mi + d3(t, mi, mp, h, i, f, g), mp + d3(t, mi, mp, h, 'mp', f, g))
    return h * g(t + h, mi + d3(t, mi, mp, h, 'mi', f, g), mp + d3(t, mi, mp, h, i, f, g))


def rk4(t0, mi, mp, h, tf, diff_mi, diff_mp):
    list_t = [t0]
    list_mi = [mi]
    list_mp = [mp]
    i = 0
    result_mp = 0
    while (t0 < tf) & (abs(tf - t0) > 0.00001):
        i += 1
        t_n = t0
        mi_n = mi
        mp_n = mp
        t0 = t_n + h
        result_mp += mi
        mi = mi_n + (1 / 6) * d1(t_n, mi_n, mp_n, h, 'mi', diff_mi, diff_mp) + (1 / 3) * d2(t_n, mi_n, mp_n, h, 'mi', diff_mi, diff_mp) + (1 / 3) * d3(t_n, mi_n, mp_n, h, 'mi', diff_mi, diff_mp) + (1 / 6) * d4(t_n, mi_n, mp_n, h, 'mi', diff_mi, diff_mp)
        mp = mp_n + (1 / 6) * d1(t_n, mi_n, mp_n, h, 'mp', diff_mi, diff_mp) + (1 / 3) * d2(t_n, mi_n, mp_n, h, 'mp', diff_mi, diff_mp) + ( 1 / 3) * d3(t_n, mi_n, mp_n, h, 'mp', diff_mi, diff_mp) + (1 / 6) * d4(t_n, mi_n, mp_n, h, 'mp', diff_mi, diff_mp)
        list_t.append(t0)
        list_mi.append(mi)
        list_mp.append(mp)
    return mi, mp, list_t, list_mi, list_mp


def mi_eq(t, mi, mp):
    return d(t) - Ka * mi


def mp_eq(t, mi, mp):
    return Ka * mi - ket * mp


def plot_Dt(D, tf):
    instants = arange(0, tf, 0.1)
    dosages = [d(t) for t in instants]
    xlabel("time (h)")
    ylabel("Dosage D(t) (mg/h)")
    plot(instants,dosages)
    show()


# plot_Dt(d, 24*60)


h_val = 17.349
_mi, _mp, t_list, mi_list, mp_list = rk2(0, 0, 0, h_val, 5*60*24, mi_eq, mp_eq)
_mi_, _mp_, t_list_, mi_list_, mp_list_ = rk2(0, 0, 0, h_val / 2, 60*24, mi_eq, mp_eq)
_mi__, _mp__, t_list__, mi_list__, mp_list__ = rk2(0, 0, 0, h_val / 4, 60*24, mi_eq, mp_eq)
print((_mi_ - _mi) / (_mi__ - _mi_))
print((_mp_ - _mp) / (_mp__ - _mp_))

plot(t_list, mi_list, label="mi")
plot(t_list, mp_list, label="mp")
xlabel("time (h)")
ylabel("(mg)")
legend()
show()
