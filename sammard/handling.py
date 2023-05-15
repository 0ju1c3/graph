import matplotlib.pyplot as plt 
file = open('test.txt','r')
t = []
x = []
y = []
for line in file:

    count = 0
    for element in line[1:-1]:
        if element not in ',[]':
            print(element)
            if count == 0:
                t.append(float(element))    
                count += 1
            elif count == 1:
                x.append(float(element))
                count += 1
            elif count == 2:
                y.append(float(element))

           # lst.append(float(element))
plt.subplot(221)#.subploot(nrows,ncolumns,plot_number)first <= third <= second;212
plt.plot(x,t,'r-',label='x-t graph',)
plt.xlabel("x-axis")
plt.ylabel("t-axis")
plt.legend()
#second plot
plt.subplot(222)#creates a 2-row, 1-column and this is the 2nd subplot
plt.plot(x,y,'b-',label='x-y graph')#213
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
#third plot
plt.subplot(223)
plt.plot(t,y,'o-',label='t-y graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
#fourth plot
fourth = []
for i in range(0,len(x)):
    fourth.append(x[i] - y[i])
plt.subplot(224)
plt.plot(fourth,y,label='x-yvs t graph')
plt.xlabel('x-y')
plt.ylabel('t')
plt.legend()
plt.show()
#3d plot
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(x,y,t)
plt.show()
