import simulation
import matplotlib.pyplot as plt
import numpy as np

velocities = [0.8, 1.2]

fig, axes = plt.subplots(1, 2)

for j, velocity in enumerate(velocities):
    a = 1 / (2 - velocity**2)
    expectedPeriod = 2 * np.pi * a**1.5
    ti = 0
    tf = 10 * expectedPeriod
    nSteps = 10000
    h = (tf - ti) / nSteps

    state = (1, 0, 0, velocity, 0, 0)
    state = simulation.gravAccel(state)
    states = simulation.Verlet(state, tf, ti, nSteps)

    x = []
    y = []
    t = []
    r = []
    v = []
    K = []
    U = []
    E = []

    for i in range(len(states)):
        state = states[i]
        x.append(state[0])
        y.append(state[1])
        t.append(ti + i * h)
        r.append(simulation.radius(state))
        v.append(simulation.speed(state))
        energies = simulation.energy(state)
        K.append(energies[0])
        U.append(energies[1])
        E.append(energies[2])

    axes[j].plot(x, y, label="Orbit")
    axes[j].plot(0, 0, "o", label="Central mass")
    axes[j].plot(x[0], y[0], "o", label="Initial point")
    axes[j].set_aspect("equal", adjustable="box")
    axes[j].set_xlabel("x")
    axes[j].set_ylabel("y")
    axes[j].set_title(f"v0 = {velocity}")
    axes[j].legend()

    plt.plot(t, K, label="K")
    plt.plot(t, U, label="U")
    plt.plot(t, E, label="E")
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.title(f"v0 = {velocity}")
    plt.legend()
    plt.show()

    plt.plot(t, r)
    plt.xlabel("Time")
    plt.ylabel("r")
    plt.title(f"v0 = {velocity}")
    plt.show()

    plt.plot(r, v)
    plt.xlabel("r")
    plt.ylabel("Speed")
    plt.title(f"v0 = {velocity}")
    plt.show()

    apoTimes = []
    if velocity < 1:
        apoTimes.append(0)
    for i in range(1, len(r) - 1):
        if r[i - 1] < r[i] and r[i] > r[i + 1]:
            apoTimes.append(t[i])

    measuredPeriods = []
    for i in range(1, len(apoTimes)):
        measuredPeriods.append(apoTimes[i] - apoTimes[i - 1])

    measuredPeriod = np.mean(measuredPeriods)
    fractionalError = abs(measuredPeriod - expectedPeriod) / expectedPeriod

    print(f"v0 = {velocity}")
    print(f"Expected period: {expectedPeriod}")
    print(f"Measured period:{measuredPeriod}")
    print(f"Fractional error:{fractionalError}")
    print(f"Periapsis:{min(r)}")
    print(f"Apoapsis: {max(r)}")

plt.show()