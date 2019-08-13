import matplotlib.pyplot as plt
# import numpy as np
import math;


sampleTime = 5
samples = 8000
f1 = 2
f2 = 50
f3 = 100
f4 = 100

y1 = []
y2 = []
y3 = []
y4 = []
y = []
x = []


for i in range (samples * sampleTime):
    y1.append( math.sin( 2 * math.pi * i * f1 / (samples)))
    y2.append( math.sin( 2 * math.pi * i * f2 / (samples)))
    y3.append( math.sin( 2 * math.pi * i * f3 / (samples)))
    y4.append( 0.4 * math.sin( 2 * math.pi * i * f4 / (samples)))
    x.append(i/samples)

for i in range(samples * sampleTime):
    y.append(y1[i])

plt.plot(x ,y)
plt.show()

