import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fftshift
import math

# harmonics = []
# for i in range(0, 4):
#     print(f'Введите {i + 1} гармонику')
#     ele = input()
#     harmonics.append(ele)
# print(harmonics)
N = 4000
t = 1.0 / 10000
A = np.array([1, 1, 0.3, 1])  # Массив амплитуд
LOGIC_LEVEL = 0.6
FREQ_LEVEL = 300
F = np.array([1.310, 1.7, 3, 4]) * 1000
W = F * 2 * np.pi
P = np.array([np.pi / 3, np.pi / 2, 0, np.pi / 4]) * 0
T = np.linspace(0.0, N * t, N, False)
U = A[0] * np.sin(T * W[0] + P[0]) + A[1] * np.sin(T * W[1] + P[1]) + A[2] * np.sin(T * W[2] + P[2]) + A[3] * np.sin(
    T * W[3] + P[3])
UF = fft(U)
fourier_amplitudes = 2.0 / N * np.abs(UF[0:N // 2])
harmonics_amplitudes = np.sort(fourier_amplitudes)[-4:]
print(harmonics_amplitudes)

buffer = []
for i in range(0, 4):
    if harmonics_amplitudes[i] < LOGIC_LEVEL:
        continue
    buffer.append(harmonics_amplitudes[i])
harmonics_amplitudes = buffer
print(harmonics_amplitudes)
harmonics_phases = []
# for i in range(0, 4):
#     j, = np.where(np.isclose(fourier_amplitudes, harmonics_amplitudes[i]))
#     phase = np.angle(UF[j]) + np.pi / 2  # Относительно косинуса
#     harmonics_phases.append(phase)
print("Фазы гармоник", harmonics_phases)
harmonics_freq = []
harmonics_char = []
TF = fftfreq(N, t)[:N // 2]
for i in range(0, TF.size):
    print (TF[i])

for i in range(0, len(harmonics_amplitudes)):
    index = list(fourier_amplitudes).index(harmonics_amplitudes[i])
    harmonics_char.append([])
    harmonics_char[i].append(harmonics_amplitudes[i])
    harmonics_char[i].append(TF[index])
    harmonics_freq.append(TF[index])
    np.delete(TF, index)
T_max = 1 / min(harmonics_freq)
harmonics_t = []
for i in range(0, len(harmonics_freq)):
    harmonics_t.append(1 / harmonics_freq[i])
print("Периоды синусоид", harmonics_t)
time = np.linspace(0.0, T_max, 5000, False)
harmonics = []
print("Массив частот", harmonics_freq)
print("Массив амплитуд", harmonics_amplitudes)
print("Характеристики амплитуд", harmonics_char)
for i in range(0, len(harmonics_amplitudes)):
    harmonic = harmonics_amplitudes[i] * np.sin(
        time * 2 * math.pi * harmonics_freq[i])
    harmonics.append(harmonic)
figure1, ax1 = plt.subplots(2)
ax1[0].plot(T, U)
ax1[0].grid()
ax1[0].set_title('U(t)')
ax1[1].plot(TF, fourier_amplitudes)
ax1[1].set_title('U(f)')
ax1[1].grid()
figure2, ax2 = plt.subplots(4)
harmonics_code = [0, 0, 0, 0]
for i in range(0, len(harmonics_amplitudes)):
    ax2[i].plot(time, harmonics[i])
for freq in harmonics_freq:
    if freq >= 4000 - FREQ_LEVEL and freq <= 4000 + FREQ_LEVEL:
        harmonics_code[3] = 1
    if freq >= 3000 - FREQ_LEVEL and freq <= 3000 + FREQ_LEVEL:
        harmonics_code[2] = 1
    if freq >= 2000 - FREQ_LEVEL and freq <= 2000 + FREQ_LEVEL:
        harmonics_code[1] = 1
    if freq >= 1000 - FREQ_LEVEL and freq <= 1000 + FREQ_LEVEL:
        harmonics_code[0] = 1
print(harmonics_code)
plt.show()
