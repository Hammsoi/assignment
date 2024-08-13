import matplotlib.pyplot as plt
import numpy as np
import random as r

x = np.array(r.choices(range(10,20),k=100))


plt.plot(np.arange(len(x)),x, '-or')
plt.show()
