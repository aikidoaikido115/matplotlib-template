import matplotlib.pyplot as plt



plt.xlabel('time (s)')
plt.ylabel('LPG concentration (ppm)')

plt.axis([0,20,-20,320])


time = [1,5,10,15]

ppm_5 = [66.62,294.8,112.5,151.86]

ppm_10 = [0,10.29,122.84,50.5]

ppm_15_20 = [0,0,0,0]

marker = ['.','o','v','^','<','>']


plt.plot(time,ppm_5,marker = marker[1])

plt.plot(time,ppm_10,marker = marker[1])

plt.plot(time,ppm_15_20,marker = marker[1])

plt.savefig(r'.\new.jpg')
plt.show()