import numpy as np
import matplotlib.pyplot as pl
import dynamic_graph.tutorial.inverted_pendulum as ip

# define inverted pendulum
a = ip.InvertedPendulum("IP")
a.cart_mass = 1.0
a.pendulum_mass = 1.0
a.pendulum_length = 1.0

# Set value of state signal
a.state = [0.0, 0.01, 0.0, 0.0]

timeStep = 0.01
timeSteps = []
values = []

# Loop over time and compute discretized state values
for x in xrange(10000) :
    t = x*timeStep
    timeSteps.append(t)
    values.append(a.state)
    a.incr(timeStep)

# Convert into numpy array
x = np.array(timeSteps)
y = np.array(values).transpose()

fig  = pl.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# plot configuration variables
ax1.plot(x,y[0])
ax1.plot(x,y[1])

# plot velocity variables
ax2.plot(x,y[2])
ax2.plot(x,y[3])

leg = ax1.legend(("x", "theta"))
leg = ax2.legend(("dx", "dtheta"))

pl.show()
