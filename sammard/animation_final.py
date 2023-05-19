import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
plt.style.use('ggplot')

# Read data from CSV
data = pd.read_csv('flightSimulatorResults.csv')
t = data['Time']
v = data['Velocity']
a = data['Acceleration']
thrust = data['Thrust']
alt = data['Altitude']

# Define the animate function
def animate(i):
    plt.subplot(221)
    plt.plot(t[:i], v[:i], 'r-')
    plt.ylabel('Velocity')
    plt.xlabel('Time')

    plt.subplot(222)
    plt.plot(t[:i], a[:i], 'b-')
    plt.ylabel('Acceleration')
    plt.xlabel('Time')

    plt.subplot(223)
    plt.plot(t[:i], thrust[:i])
    plt.xlabel('Time')
    plt.ylabel('Thrust')

    plt.subplot(224)
    plt.plot(t[:i], alt[:i])
    plt.xlabel('Time')
    plt.ylabel('Altitude')

# Create the animation
ani = FuncAnimation(plt.gcf(), animate, interval=1000, frames=20, repeat=False)

# Set up the writer for saving the animation as an MP4 file
writer = FFMpegWriter(fps=20)

# Save the animation as an MP4 file
#ani.save('flight_animation.mp4', writer=writer)

# Show the plot
plt.tight_layout()
plt.show()
