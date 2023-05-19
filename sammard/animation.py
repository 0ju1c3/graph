import pandas as pd
#from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
plt.style.use('ggplot')#print(plt.style.available); different built-in-styles

def animate(i):
    data = pd.read_csv('flightSimulatorResults.csv')#data is being read and loaded into memory on each frame of the animation
    t = data['Time']
    v = data['Velocity']
    a = data['Acceleration']
    plt.subplot(221)
    plt.plot(t,v,'r-')
    plt.ylabel('velocity')
    plt.xlabel('time')
    plt.subplot(222)
    plt.plot(t,a,'b-')
    plt.ylabel('acceleration')
    plt.xlabel('time')
    plt.subplot(223)
    thrust = data['Thrust']
    plt.plot(t,thrust)
    plt.xlabel('Time')
    plt.ylabel('Thrust')
    alt = data['Altitude']
    plt.subplot(224)
    plt.plot(t,alt)
    plt.xlabel('Time')
    plt.ylabel('Altitude')
ani = FuncAnimation(plt.gcf(),animate,interval = 1000, frames = 10, repeat = False)
writer = FFMpegWriter(fps=20)
#ani.save('flight_animation.mp4',writer=writer)
plt.tight_layout()
plt.show()
exit()
