from control import *
import matplotlib.pyplot as plt

# Computes the step response
num = [77.06, 275.9];
dem = [1, 11.4, 91.06, 275.9];
sys = TransferFunction(num, dem)
t, y = step(sys)

# Plotting
plt.plot(y,t)
plt.grid(True)
plt.xlabel('t')
plt.title('Step Response')
plt.show()
