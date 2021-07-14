import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style
import sys

style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


def animate(interval):
	# graph_data = open(sys.argv[1], 'r').read()
	# lines = graph_data.split('\n')
	xs = []
	ys = []
	for line in sys.argv[1]:
		sys.argv[1].split('\n')
		if len(line) > 1:
			x, y = line.split()
			xs.append(x)
			ys.append(int(y))
	ax.clear()
	ax.barh(xs, ys)
	ax.set_xlabel('number of #', fontsize=12)
	ax.plot()


anime = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
