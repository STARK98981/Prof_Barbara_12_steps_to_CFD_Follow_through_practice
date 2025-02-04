# Diffusion equation using Central Differencing

import numpy as np
import matplotlib.pyplot as plt

nx = 41
dx = 2/(nx-1)
nu = 0.3
nt = 20
CFL = 0.2
dt = CFL * dx**2 / nu

u = np.ones(nx)
u[int(0.5/dx):int(1/dx+1)] = 2 # set values of u =2 between 0.5 and 1

un = np.ones(nx)

for n in range(nt):
    un = u.copy()
    for i in range(1,nx-1):
        u[i] = un[i] + (nu*dt/dx**2)*(un[i+1]- 2*un[i] + un[i-1])

plt.plot(np.linspace(0,2,nx), u, label='u(x)')  # Add a label for the legend
plt.xlabel('x')  # Label for the x-axis
plt.ylabel('u')  # Label for the y-axis
plt.title('Linear Convection-Diffusion')  # Title of the plot
plt.grid(True)  # Enable the grid
plt.legend()  # Show the legend
plt.show()  # Display the plot

