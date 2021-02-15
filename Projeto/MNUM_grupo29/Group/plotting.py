import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from getting_mi_and_mp_rk4 import *


mi3, mp3, list_t, list_mi, list_mp = rk4_systems(
    func_MI, func_MP, 0, 0, 0, 100, 10000)
plt.xlabel("time(h)")
plt.ylabel("mass(g)")
plt.plot(list_t, list_mp)
plt.plot(list_t, list_mi)
plt.legend(["Compartimento plasmático", "Compartimento central"])
plt.show()
