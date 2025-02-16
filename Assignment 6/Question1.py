import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random

N = float(input("Enter a value for N: "))

t = np.linspace(-10, 10, 100)
z1 = N * t**2
z2 = N * np.sin(t)

plt.plot(t, z1, label='y = N * t^2', color='red', linestyle='-')
plt.plot(t, z2, label='y = N * sin(t)', color='blue', linestyle='--')

plt.legend()
plt.grid(True)
plt.title('Quadratic vs Sine')

plt.show()