import matplotlib.pyplot as plt
import numpy as np
import MyModule

b = MyModule.dist(7,3)
print(b)

a = MyModule.dist2(4,5)
print(a)

x = np.linspace (0, 3, 20)
y = np.sin(x)
plt.plot(x, y,)
plt.plot(x, y, 'o')
plt.show()
