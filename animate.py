import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

steps = 50
nodes = 100
positions = []
solutions = []

for i in range(steps):
   positions.append(np.random.rand(2, nodes))
   solutions.append(np.random.random(nodes))

fig, ax = plt.subplots()
marker_size = 50

def animate(i):
   fig.clear()
   ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(0, 1), ylim=(0, 1))
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   s = ax.scatter(positions[i][0], positions[i][1], s=marker_size, c=solutions[i], cmap="RdBu_r", marker="o", edgecolor='black')

plt.grid(b=None)
ani = animation.FuncAnimation(fig, animate, interval=100, frames=range(steps))

ani.save('animation.gif', writer='pillow')