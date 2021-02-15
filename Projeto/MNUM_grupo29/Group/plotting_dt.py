from numpy import arange
from matplotlib.pyplot import plot, show, scatter, xlabel, ylabel, legend


def plot_Dt(D, tf):
    instants = arange(0, tf, 0.1)
    dosages = [D(t) for t in instants]
    xlabel("time (h)")
    ylabel("Dosage D(t) (mg/h)")
    plot(instants, dosages)
    show()


plot_Dt(d, 48)
