import matplotlib.pyplot as pt
import numpy as np
import time

x = np.linspace(0, 10, 100)
y = np.cos(x)

pt.ion()
figure, ax = pt.subplots(figsize=(8, 6))
line1, = ax.plot(x, y)

pt.title("Live plot for sin(x)", fontsize=18)
pt.xlabel("(x)", fontsize=10)
pt.ylabel("sin(x)", fontsize=10)

for p in range(1000):
    updated_y = np.cos(x-0.05*p)
    line1.set_xdata(x)
    line1.set_ydata(updated_y)
    figure.canvas.draw()
    figure.canvas.flush_events()
    # time.sleep(0.001)
