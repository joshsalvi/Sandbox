def hopfstoch(mu, noiseSTD, tvec):
    import math
    import numpy as num

    # Parameter initialization
    xzero = 1
    yzero = -1
    Dtfac = 10 ** 2
    Dt = (tvec[1] - tvec[0]) / Dtfac
    n = int(tvec[len(tvec) - 1] / Dt)

    # Generate random seed and values
    num.random.seed(100)
    xdW = math.sqrt(Dt) * num.random.randn(n)
    ydW = math.sqrt(Dt) * num.random.randn(n)

    # Initialize the variables
    xdet = num.zeros(n)
    xdet[0] = xzero
    ydet = num.zeros(n)
    ydet[0] = yzero
    xsto = num.zeros(n)
    xsto[0] = xzero
    ysto = num.zeros(n)
    ysto[0] = yzero

    for ind in range(1, n):
        xdet[ind] = xdet[ind - 1] + Dt * (
            mu * xdet[ind - 1] - 2 * math.pi * ydet[ind - 1] - xdet[ind - 1] * (
            xdet[ind - 1] ** 2 + ydet[ind - 1] ** 2))
        ydet[ind] = ydet[ind - 1] + Dt * (
            2 * math.pi * xdet[ind - 1] + mu * ydet[ind - 1] - ydet[ind - 1] * (
            xdet[ind - 1] ** 2 + ydet[ind - 1] ** 2))

        xsto[ind] = xsto[ind - 1] + Dt * (mu * xsto[ind - 1] - 2 * math.pi * ysto[ind - 1] - xsto[ind - 1] * (
            xsto[ind - 1] ** 2 + ysto[ind - 1] ** 2)) + noiseSTD * xdW[ind]
        ysto[ind] = ysto[ind - 1] + Dt * (2 * math.pi * xsto[ind - 1] + mu * ysto[ind - 1] - ysto[ind - 1] * (
            xsto[ind - 1] ** 2 + ysto[ind - 1] ** 2)) + noiseSTD * ydW[ind]

    return xdet, ydet, xsto, ysto


import numpy as num
import matplotlib.pyplot as plt

xdet = {}
ydet = {}
xsto = {}
ysto = {}
xdet[0], ydet[0], xsto[0], ysto[0] = hopfstoch(-0.2, 0.2, num.linspace(0, 30, 1000))
xdet[1], ydet[1], xsto[1], ysto[1] = hopfstoch(0, 0.2, num.linspace(0, 30, 1000))
xdet[2], ydet[2], xsto[2], ysto[2] = hopfstoch(0.2, 0.2, num.linspace(0, 30, 1000))

plt.figure(1)
plt.plot(xdet[0], 'k')
plt.plot(xsto[0], 'r')
plt.legend(['Deterministic', 'Stochastic'])
plt.show()

plt.figure(2)
plt.plot(xdet[1], 'k')
plt.plot(xsto[1], 'r')
plt.legend(['Deterministic', 'Stochastic'])
plt.show()

plt.figure(3)
plt.plot(xdet[2], 'k')
plt.plot(xsto[2], 'r')
plt.legend(['Deterministic', 'Stochastic'])
plt.show()
