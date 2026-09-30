import simulation
import matplotlib.pyplot as plt
state = (1, 0, 0, 1, 0, 0)
state = simulation.gravAccel(state)
states = simulation.Verlet(state, tf=80, ti=0, nSteps=800)
x = []
y = []
for state in states:
    x.append(state[0])
    y.append(state[1])
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3,3)
ax.set_aspect("equal", adjustable = "box")
ax.plot(x,y)
plt.show()
