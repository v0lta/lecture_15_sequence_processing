import matplotlib.pyplot as plt
import tikzplotlib as tikz
import numpy as np


x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.cos(x)

plt.plot(x,y)
tikz.save('cos.tex', standalone=True)

