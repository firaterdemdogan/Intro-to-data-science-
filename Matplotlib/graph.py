import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,6)
y = np.arange(1,11,2)

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.2,0.3])

axes1.plot(y,x)
axes1.set_xlabel("Outer X")
axes1.set_ylabel("Outer Y")
axes1.set_title("Outer Graph")

axes2.plot(y,x)
axes1.set_xlabel("Inner X")
axes1.set_ylabel("Inner Y")
axes1.set_title("Inner Graph")
plt.show()
