import numpy as np
import matplotlib.pyplot as plt


def plot_quadratic():
    x = np.linspace(-5, 5, 400)
    y = x**2 - 3*x + 1
    plt.figure()
    plt.plot(x, y, label=r'$f(x)=x^2-3x+1$')
    plt.title('Courbe de la fonction $f(x)=x^2-3x+1$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()


def plot_height():
    v0 = 10
    g = 9.81
    t = np.linspace(0, 2*v0/g, 400)
    y = v0 * t - 0.5 * g * t**2
    plt.figure()
    plt.plot(t, y, label=r'$y(t)=v_0 t - \frac{1}{2} g t^2$')
    plt.title('Graphe de la hauteur en fonction du temps')
    plt.xlabel('temps (s)')
    plt.ylabel('hauteur (m)')
    plt.grid(True)
    plt.legend()


if __name__ == '__main__':
    plot_quadratic()
    plot_height()
    plt.show()
