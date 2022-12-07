from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt


# Number of sample points
N = 10000
# sample spacing
T = 1.0 / 10000
x = np.linspace(0.0, N * T, N, endpoint=False)
y = 0*np.sin(1000 * 2.0 * np.pi * x) + np.sin(2000 * 2.0 * np.pi * x) + 1 * np.sin(3000* 2.0 * np.pi * x) + \
    np.sin(4000 * 2.0 * np.pi * x)

yf = fft(y)
xf = fftfreq(N, T)[:N // 2]
UF = 2.0 / N * np.abs(yf[0:N // 2])
a = 700
b= 1300
for i in range(4):
    if np.max(UF[a:b]) >= 0.8:
        print('1', end='')
    else:
        print('0', end='')
    a += 1000
    b += 1000
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.grid()
plt.show()