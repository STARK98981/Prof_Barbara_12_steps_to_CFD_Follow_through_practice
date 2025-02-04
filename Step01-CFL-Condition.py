# This code is to understand CFL condition while implementing linear convection in 1D using FDM
import numpy as np
import matplotlib.pyplot as plt

def linearconv(nx):
    dx = 2/(nx-1)
    nt = 20
    dt = 0.025
    c  = 1

    u = np.ones(nx)
    u[int(0.5/dx):int(1/dx+1)] = 2 # set values of u =2 between 0.5 and 1

    un = np.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c*dt/dx*(un[i]-un[i-1])
    
    plt.plot(np.linspace(0,2,nx), u, label='u(x)')  # Add a label for the legend
    plt.xlabel('x')  # Label for the x-axis
    plt.ylabel('u')  # Label for the y-axis
    plt.title('Linear Convection')  # Title of the plot
    plt.grid(True)  # Enable the grid
    plt.legend()  # Show the legend
    plt.show()  # Display the plot


linearconv(41)