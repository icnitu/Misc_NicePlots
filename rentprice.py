import numpy as np
import matplotlib.pyplot as plt

rent = np.array([390, 405, 416, 422.5, 487.5, 540.2])
yr = 2019 + np.arange(6)

plt.figure(figsize=(6,4), constrained_layout=True)
plt.plot(yr, rent, marker='.')
plt.xlabel('year')
plt.ylabel('price')
plt.show()
