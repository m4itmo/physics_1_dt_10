import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from time import sleep


class PointCharge:
    def __init__(self, q, x, y):
        self.q = q
        self.x = x
        self.y = y


def electric_field(charges, x, y):
    """
    Вычисление компонентов электростатического поля в точке (x, y).
    """
    Ex, Ey = 0, 0
    k = 8.99e9

    for charge in charges:
        dx = x - charge.x
        dy = y - charge.y
        r_squared = dx ** 2 + dy ** 2
        if r_squared < 1e-6:
            continue

        r = np.sqrt(r_squared)
        E = k * charge.q / r_squared
        Ex += E * (dx / r)
        Ey += E * (dy / r)

    return Ex, Ey


print("Введите параметры для моделирования электростатического поля")

q1 = float(input("Значение заряда 1 (рекомендуется 0.02 Кл): ") or 0.02)
x1 = float(input("X-координату заряда 1 (рекомендуется -2): ") or -2)
y1 = float(input("Y-координату заряда 1 (рекомендуется -1): ") or -1)

q2 = float(input("Значение заряда 2 (рекомендуется -0.002 Кл): ") or -0.002)
x2 = float(input("X-координату заряда 2 (рекомендуется 2): ") or 2)
y2 = float(input("Y-координату заряда 2 (рекомендуется 1): ") or 1)

charges = [
    PointCharge(q1, x1, y1),
    PointCharge(q2, x2, y2)
]

linspace_r = 10
grids = 500
x = np.linspace(-linspace_r, linspace_r, grids)
y = np.linspace(-linspace_r, linspace_r, grids)
X, Y = np.meshgrid(x, y)

Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Ex[i, j], Ey[i, j] = electric_field(charges, X[i, j], Y[i, j])

plt.figure(figsize=(10, 10))
colors = np.sqrt(Ex ** 2 + Ey ** 2)
plt.streamplot(X, Y, Ex, Ey, color=colors, linewidth=1, density=2.5, cmap=cm.rainbow, arrowstyle='->', arrowsize=1.5)

for charge in charges:
    if charge.q > 0:
        plt.plot(charge.x, charge.y, 'ro', markersize=15)
    else:
        plt.plot(charge.x, charge.y, 'bo', markersize=15)

plt.xlabel('X')
plt.ylabel('Y', rotation=0)
plt.title('Электростатическое поле системы неподвижных точечных зарядов')
plt.grid()
plt.axis('equal')
plt.show()
