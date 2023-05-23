
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading

data = pd.read_csv("flightSimulatorResults.csv")
t = data["Time"]
v = data['Velocity']
a = data['Acceleration']
alt = data["Altitude"]
thrust = data["Thrust"]

figure, axis = plt.subplots(2, 2, figsize=(10, 10))#makes figure and axis of 2 *2 and figure size of width and height in inches
figure.tight_layout()#spaces out the sub-plots

def vt(i):
    axis[0, 0].cla()#clears the plot of the previous data
    axis[0, 0].plot(t[:i], v[:i], 'r-')
    axis[0, 0].set_ylabel('Velocity')
    axis[0, 0].set_xlabel('Time')

def at(i):
    axis[0, 1].cla()
    axis[0, 1].plot(t[:i], a[:i], 'b-')
    axis[0, 1].set_ylabel('Acceleration')
    axis[0, 1].set_xlabel('Time')

def thrustt(i):
    axis[1, 0].cla()
    axis[1, 0].plot(t[:i], thrust[:i])
    axis[1, 0].set_xlabel('Time')
    axis[1, 0].set_ylabel('Thrust')

def altt(i):
    axis[1, 1].cla()
    axis[1, 1].plot(t[:i], alt[:i])
    axis[1, 1].set_xlabel('Time')
    axis[1, 1].set_ylabel('Altitude')

def threadani(i):
    t1 = threading.Thread(target=vt, args=(i,))
    t2 = threading.Thread(target=at, args=(i,))
    t3 = threading.Thread(target=thrustt, args=(i,))
    t4 = threading.Thread(target=altt, args=(i,))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
#frames = len(t) used to include all the data points; when frames = 20 - > graph terminated sooner
ani = FuncAnimation(figure, threadani, frames=len(t), interval=100)
plt.show()
