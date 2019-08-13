import matplotlib.pyplot as plt
# import numpy as np
import math;
import numpy as np
import cmath;
from cmath import exp, pi

def fft(X, N):
    if N == 1: 
        return X
    else:
        even = fft(X[0::2], int(N//2)) # Call fft with all even elements
        odd  = fft(X[1::2], int(N//2)) # Call fft with all odd elements

        for k in range(int(N/2)):           
            t = exp(-2j*pi*k/N) * odd[k] 
            X[k] = even[k] + t
            X[k + int(N//2)] = even[k] - t
        return X


sampleTime = 1
samples = 1024 #16384 32768
sampleRate = samples * 20
f1 = 50 
f2 = 300
f3 = 400
f4 = 500

y1 = []
y2 = []
y3 = []
y4 = []
y = []
x = []


for i in range (samples):
    y1.append( math.sin( 2 * math.pi * i * f1 / (sampleRate)))
    y2.append( math.sin( 2 * math.pi * i * f2 / (sampleRate)))
    y3.append( math.sin( 2 * math.pi * i * f3 / (sampleRate)))
    y4.append( 0.4 * math.sin( 2 * math.pi * i * f4 / (sampleRate)))
    x.append(i/samples)

for i in range(samples):
    y.append(y1[i] + y2[i] + y3[i] + y4[i])

yfft = fft(y, samples)

power = np.abs(np.divide(yfft, samples/2))
p = power[0:int(samples/2)]

sampleT = samples/sampleRate
freqs = np.divide((np.arange(0, samples/2)), sampleT)

# print(p[400])
# print(p[480])

plt.plot(freqs, p)
plt.show()
plt.plot(p2)
plt.show()




