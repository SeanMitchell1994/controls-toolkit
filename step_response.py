# step_response.py
# Computes the step response for a transfer function
# The script accepts integer and decimal input from the CLI

#import control
from scipy import signal
import matplotlib.pyplot as plt

# === Computes the step response ===
# Grabs input from the CLI and casts it as an float (same percision as a double)
# All input should be in the form [s^n + s^(n-1) + ... + s^0]
print("Enter the coefficients of the transfer function")
print("Enter the numerator: ", end='')
num = [float(x) for x in input().split()]

print("Enter the denominator: ", end='')
dem = [float(x) for x in input().split()]

sys = signal.TransferFunction(num, dem)
t, y = signal.step(sys)

# === Plotting ===
plt.plot(y,t)
plt.grid(True)
plt.xlabel('t')
plt.title('Step Response')
plt.show()
