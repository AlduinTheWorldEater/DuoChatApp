from misc import *
import matplotlib.animation as anm

fig, axs = graph_create_plot(3)

anim = anm.FuncAnimation(fig, graphing.graph_plot)

plt.show()
