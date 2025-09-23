import numpy as np
import matplotlib.pyplot as plt

n = 50

k = np.arange(n)
roots = np.exp(1j * 2 * np.pi * k / n)

real_part = roots.real
imag_part = roots.imag

plt.figure()
plt.plot(real_part, imag_part, 'o')
plt.title('Roots of $/lambda^{50} = 1$')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.axis('equal')
plt.grid(True)

plt.show()