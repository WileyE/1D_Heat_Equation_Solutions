#Solving 1D heat equation
# Problem u_t = Du_xx - bu_x +cu +S(x,t)

#boundary conditions
#         u(A,t) = f(t)
#         u(B,t) = g(t)

#Initial Conditions
#         u(x,0) = h(x)

#imports
import numpy as np
import matplotlib.pyplot as plt

#Define initial condition
def h(x):
    return np.exp(-((x*8)**2))

#Define Left Boundry Condition as a function of t
def f(t):
    return 0.4

#Define Right Boundry Condition as a function of t
def g(t):
    return 0.4

#Define external source as a function of x and t
def s(x,t):
    return 0.0


A = -1.0 #Left Boundry

B = 1.0 #Right Boundary

D = 0.05 #Diffusivity

c = 0.0 #internal source

beta = 0.0 #Convection

dx = .001 #Spatial step

dt = .00001 #Time Step

rt = (D*dt)/(dx**2.0) #Discretization coefficient

Tmax = 1 #Max time

imax = int((B-A)/dx) #Last spatial step

nmax = int(Tmax/dt + .1) #Last time step

counter = 0 #Iterator for saving plots


#Setup Arrays
x = np.linspace(A,B,imax)
t = np.linspace(0,Tmax,nmax)
u = np.zeros((imax,2))

#Set first solution vector to initial conditions
for i in range(0,imax):
    u[i][0] = h(x[i])

#plot initial conditions
n = 0
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,u[:,n], color = 'r')
ax.set_xlim([-1,1])
ax.set_ylim([0,1.05])
ax.set_xlabel('x')
ax.set_ylabel('u(x,t)')
ax.set_title('Heat Diffusion on a Thin Rod')
fig.savefig('0.png', bbox_inches='tight')


# Main loop
for n in range(1, nmax):
    u[0][1] = f(t[n])
    for i in range(1, imax - 1):
        u_xx = u[i - 1][0] - 2.0 * u[i][0] + u[i + 1][0]
        u_x = u[i + 1][0] - u[i - 1][0]
        u_ = u[i][0]
        source = s(x[i], t[n])
        u[i][1] = u[i][0] + rt * u_xx - ((beta * dt) / (2.0 * dx)) * u_x + c * u_ + source
    u[imax - 1][1] = g(t[n])

    # move solution column u[i][1] to known column u[i][0]
    for i in range(0, imax):
        u[i][0] = u[i][1]

    counter = n
    

    if counter % 10000 == 0 or counter == nmax-1:
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.plot(x,u[:,0], color = 'r')
        ax.set_xlim([-1,1])
        ax.set_ylim([0,1.05])
        ax.set_xlabel('x')
        ax.set_ylabel('u(x,t)')
        ax.set_title('Heat Diffusion on a Thin Rod timestep = '+ str(n))
        fig.savefig(str(n) + '.png', bbox_inches='tight')
        
    else:
        continue