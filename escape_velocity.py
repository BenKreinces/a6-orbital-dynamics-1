import simulation
import matplotlib.pyplot as plt
import numpy as np

G = 1
M = 1
r0 = 1
vys = [1.2, 1.5]
ti = 0
tf = 80
nSteps = 10000
h = (tf - ti) / nSteps
allStates = []
for vy in vys:
    state = (1, 0, 0, vy, 0, 0)
    state = simulation.gravAccel(state)
    states = simulation.Verlet(state, tf, ti, nSteps)
    allStates.append(states)

fig, ax = plt.subplots()
theta = np.linspace(0, 2 * np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), "--", label="Reference Circle r=1")
ax.plot(0, 0, "o", label="Central mass")

for i , states in enumerate(allStates):
    x = []
    y = []
    for state in states:
        x.append(state[0])
        y.append(state[1])
    ax.plot(x, y, label = f'vy = {vys[i]}')
    
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()


for j, states in enumerate(allStates):
    t = []
    K = []
    U = []
    E = []

    for ii, state in enumerate(states):
        t.append(ti + ii * h)
        energies = simulation.energy(state)
        K.append(energies[0])
        U.append(energies[1])
        E.append(energies[2])

    plt.plot(t, K, label="K")
    plt.plot(t, U, label="U")
    plt.plot(t, E, label="E")
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.title(f'vy = {vys[i]}')
    plt.legend()
    plt.show()

    print(f'vy = {vys[i]}, initial total energy =, {E[0]}')

print(f"Escape velocity: {np.sqrt(2)}")
