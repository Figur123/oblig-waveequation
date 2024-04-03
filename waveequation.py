import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

X_length = 1
y_length = 1
time_length = 300

x_divisions = 51
y_divisions = 51
time_divisions = 600

def initialfunction(x,y):
    return 2*np.e**(-20*(x-0.5)**2) * np.e**(-20*(y-0.5)**2)

x = np.linspace(0,X_length,x_divisions)
y = np.linspace(0,y_length,y_divisions)
t= np.linspace(0,time_length,time_divisions)

x,y,t = np.meshgrid(x,y,t)
u = np.zeros((x_divisions,y_divisions,time_divisions))
du = np.zeros((x_divisions,y_divisions))

u[:,:,0] = initialfunction(x[:,:,0],y[:,:,0])



for h in range(time_divisions-1):
    for i in range(1, y_divisions - 1):
        for j in range(1, x_divisions - 1):
            du[j,i] += ((u[j + 1, i, h] - 2 * u[j, i, h] + u[j - 1, i, h])/(time_length/time_divisions) + \
                       (u[j, i + 1, h] - 2 * u[j, i, h] + u[j, i - 1, h])/(time_length/time_divisions))*(time_length/time_divisions)
            #print(du[j,i])
            u[j,i,h+1] = u[j,i,h] + (du[j,i])*(time_length/time_divisions)
            


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for h in range(0,time_divisions):
    ax.clear()
    surf = ax.plot_surface(x[:, :, 0], y[:, :, 0], u[:, :, h].T, cmap=cm.coolwarm, vmin=-1, vmax=1 , linewidth=0, antialiased=False)

    ax.set_xlabel('X-akse')
    ax.set_ylabel('Y-akse')
    ax.set_zlabel('Amplitude')
    ax.set_zlim(0, 2)
    ax.zaxis.set_major_locator(LinearLocator(10))

    plt.pause(0.001)

plt.show()
