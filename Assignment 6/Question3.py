import numpy as np
import matplotlib.pyplot as plt

np.random.seed(987654321)
dataset = np.random.randn(60)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(np.cumsum(dataset), color='purple', linestyle='-.', linewidth=2)
axes[0, 0].set_title('Cumulative Sum')
axes[0, 0].set_xlabel('Data Points')
axes[0, 0].set_ylabel('Cumulative Sum')
axes[0, 0].grid(True, linestyle='dotted', alpha=0.7)

noise = np.random.randn(60) * 1.5  
axes[0, 1].scatter(dataset, dataset + noise, color='green', marker='x', alpha=0.7)
axes[0, 1].set_title('Scatter Plot with Noise')
axes[0, 1].set_xlabel('Dataset')
axes[0, 1].set_ylabel('Dataset + Noise')
axes[0, 1].grid(True, linestyle='dashed', alpha=0.5)

axes[1, 0].plot(dataset, color='red', linestyle='--', marker='o', markersize=4)
axes[1, 0].set_title('Line Plot')
axes[1, 0].set_xlabel('Data Points')
axes[1, 0].set_ylabel('Dataset Values')
axes[1, 0].grid(True, linestyle='solid', alpha=0.6)

axes[1, 1].scatter(np.arange(60), dataset, color='blue', marker='s', alpha=0.8)
axes[1, 1].set_title('Index vs Dataset Scatter')
axes[1, 1].set_xlabel('Index')
axes[1, 1].set_ylabel('Dataset Values')
axes[1, 1].grid(True, linestyle='dotted', alpha=0.7)

plt.tight_layout()
plt.show()
