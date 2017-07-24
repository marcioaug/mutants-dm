from matplotlib import pyplot

pyplot.figure()

ax = pyplot.gca()

ax.quiver([0, 0, 0, 0], [0, 0, 0, 0], [2, 3, 1, 5], [1, 4, 3, 5], angles='xy', scale_units='xy', scale=1)
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])

pyplot.draw()
pyplot.show()