def qc(sol1, sol2, sol3):
    return (sol2-sol1)/(sol3-sol2)


def d(t):
    if t <= 96:  # 4 days
        while t >= 12:
            t -= 12
        if t <= 0.5:
            return 0
        elif 0.5 < t <= 2:
            return (500 * (t-0.5)) / 17.25
        elif 2 < t <= 12:
            return (-500 * (t-2)) / 115 + 1000 / 23
    else:
        return 0


# other value - 3.84 | 0.0017803
Ka = 0.1
Ket = 0.064 * 60  # hour^-1


def func_MI(t, mi, mp):
    return d(t) - Ka * mi


def func_MP(t, mi, mp):
    return Ka*mi - Ket * mp


def euler_improved(func_mi, func_mp, inital_t, initial_mi, initial_mp, final_t, steps):
    list_t = [inital_t]
    list_mi = [initial_mi]
    list_mp = [initial_mp]
    mi = initial_mi
    mp = initial_mp
    t = inital_t
    h = (final_t - inital_t) / steps
    mi_prev = mi - func_mi(mi, mp) * h
    mp_prev = mp - func_mp(mi, mp) * h
    while t < final_t:
        mi_ = func_mi(t, mi, mp)
        mp_ = func_mp(t, mi, mp)
        p_ = mi_prev + 2 * mi_ * h
        p1_ = mp_prev + 2 * mp_ * h
        mi_prev = mi
        mp_prev = mp

        p_1 = func_mi(t + h, p_, p1_)
        p1_1 = func_mp(t + h, p_, p1_)

        delta_mi = (p_1 + mi_)/2 * h
        delta_mp = (p1_1 + mp_)/2 * h
        mi = mi + delta_mi
        mp = mp + delta_mp
        t = t + h
        list_t.append(t)
        list_mi.append(mi)
        list_mp.append(mp)
    return mi, mp, list_t, list_mi, list_mp


def euler(func_mi, func_mp, inital_t, initial_mi, initial_mp, final_t, steps):
    list_t = [inital_t]
    list_mi = [initial_mi]
    list_mp = [initial_mp]
    mi = initial_mi
    mp = initial_mp
    t = inital_t
    h = (final_t - inital_t) / steps
    while t < final_t:
        t = t + h
        mi = mi + func_mi(t, mi, mp) * h
        mp = mp + func_mp(t, mi, mp) * h
        list_t.append(t)
        list_mi.append(mi)
        list_mp.append(mp)
    print("mi: ", mi)
    print("Mp: ", mp)
    return mi, mp, list_t, list_mi, list_mp


def rk2_systems(func_mi, func_mp, initial_t, initial_mi, initial_mp, final_t, steps):
    list_t = [initial_t]
    list_mi = [initial_mi]
    list_mp = [initial_mp]
    h = (final_t - initial_t) / steps
    t = initial_t
    mi = initial_mi
    mp = initial_mp
    while t < final_t:
        t = t + h
        mi_linha = func_mi(t, mi, mp)
        mp_linha = func_mp(t, mi, mp)
        mi_mid = func_mi(t + h/2, mi + (h/2) * mi_linha, mp + (h/2) * mp_linha)
        mp_mid = func_mp(t + h/2, mi + (h/2) * mi_linha, mp + (h/2) * mp_linha)
        delta_mi = mi_mid * h
        delta_mp = mp_mid * h
        mi = mi + delta_mi
        mp = mp + delta_mp
        list_t.append(t)
        list_mi.append(mi)
        list_mp.append(mp)
    print("mi: ", mi)
    print("Mp: ", mp)
    return mi, mp, list_t, list_mi, list_mp


def rk4_systems(func_mi, func_mp, intial_t, initial_mi, initial_mp, final_t, steps):
    list_t = [intial_t]
    list_mi = [initial_mi]
    list_mp = [initial_mp]
    h = (final_t - intial_t) / steps
    t = intial_t
    mi = initial_mi
    mp = initial_mp
    while t < final_t:
        t = t + h
        d1_mi = h * func_mi(t, mi, mp)
        d1_mp = h * func_mp(t, mi, mp)

        d2_mi = h * func_mi(t + h/2, mi + d1_mi/2, mp + d1_mp/2)
        d2_mp = h * func_mp(t + h/2, mi + d1_mi/2, mp + d1_mp/2)

        d3_mi = h * func_mi(t + h/2, mi + d2_mi/2, mp + d2_mp/2)
        d3_mp = h * func_mp(t + h/2, mi + d2_mi/2, mp + d2_mp/2)

        d4_mi = h * func_mi(t + h, mi + d3_mi, mp + d3_mp)
        d4_mp = h * func_mp(t + h, mi + d3_mi, mp + d3_mp)

        mi = d1_mi/6 + d2_mi/3 + d3_mi/3 + d4_mi/6 + mi
        mp = d1_mp/6 + d1_mp/3 + d3_mp/3 + d4_mp/6 + mp

        list_t.append(t)
        list_mi.append(mi)
        list_mp.append(mp)
    print("mi: ", mi)
    print("Mp: ", mp)
    return mi, mp, list_t, list_mi, list_mp


step = 30


def test_rk4():
    mi1, mp1, list_t, list_mi, list_mp = rk4_systems(
        func_MI, func_MP, 0, 0, 0, 96, step)
    mi2, mp2, list_t, list_mi, list_mp = rk4_systems(
        func_MI, func_MP, 0, 0, 0, 96, step * 2)
    mi3, mp3, list_t, list_mi, list_mp = rk4_systems(
        func_MI, func_MP, 0, 0, 0, 96, step * 4)

    print("RK4: ")
    print("Qc for mi: ", qc(mi1, mi2, mi3))
    print("Qc for mp: ", qc(mp1, mp2, mp3))
    estimated_error_mi = abs(mi3 - mi2) / (qc(mi1, mi2, mi3) - 1)
    print("Estimated error for Mi value: ", estimated_error_mi)
    estimated_error_mp = abs(mp3 - mp2) / (qc(mp1, mp2, mp3) - 1)
    print("Estimated error for Mi value: ", estimated_error_mp)


def test_rk2():
    mi1, mp1, list_t, list_mi, list_mp = rk2_systems(
        func_MI, func_MP, 0, 0, 0, 96, step)
    mi2, mp2, list_t, list_mi, list_mp = rk2_systems(
        func_MI, func_MP, 0, 0, 0, 96, step * 2)
    mi3, mp3, list_t, list_mi, list_mp = rk2_systems(
        func_MI, func_MP, 0, 0, 0, 96, step * 4)

    print("RK2: ")
    print("Qc for mi: ", qc(mi1, mi2, mi3))
    print("Qc for mp: ", qc(mp1, mp2, mp3))
    estimated_error_mi = abs(mi3 - mi2) / (qc(mi1, mi2, mi3) - 1)
    print("Estimated error for Mi value: ", estimated_error_mi)

    estimated_error_mp = abs(mp3 - mp2) / (qc(mp1, mp2, mp3) - 1)
    print("Estimated error for Mi value: ", estimated_error_mp)


def test_euler():
    mi1, mp1, list_t, list_mi, list_mp = euler(
        func_MI, func_MP, 0, 0, 0, 96, step)
    mi2, mp2, list_t, list_mi, list_mp = euler(
        func_MI, func_MP, 0, 0, 0, 96, step * 2)
    mi3, mp3, list_t, list_mi, list_mp = euler(
        func_MI, func_MP, 0, 0, 0, 96, step * 4)
    print("EULER: ")
    print("Qc for mi: ", qc(mi1, mi2, mi3))
    print("Qc for mp: ", qc(mp1, mp2, mp3))
    estimated_error_mi = abs(mi3 - mi2) / (qc(mi1, mi2, mi3) - 1)
    print("Estimated error for Mi value: ", estimated_error_mi)

    estimated_error_mp = abs(mp3 - mp2) / (qc(mp1, mp2, mp3) - 1)
    print("Estimated error for Mi value: ", estimated_error_mp)


if __name__ == "__main__":
    test_rk4()
    test_rk2()
    test_euler()
