import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

y0 = [np.pi - 0.1, 0.0]

def step(y, t):
	theta, omega = y
	dtheta = omega
	domega = -0.1 * omega - 9.81 * np.sin(theta)
	return [dtheta, domega] 

y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0,30,100)
sol = odeint(step, y0, t)

plt.plot(sol[:, 0], 'b', label="Theta(t)")
plt.plot(sol[:, 1], 'g', label="Omega(t)")
plt.show()

