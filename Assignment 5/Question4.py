import numpy as np
import matplotlib.pyplot as plt

#(a)
x = np.linspace(-10,10,100)

y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x)+1)

plt.figure(figsize=(5, 3))
plt.plot(x, y1, label='Y = x²')
plt.title('Plot of Y = x²')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid()
plt.legend()
plt.show()

#(b)
plt.figure(figsize=(5,3))
plt.plot(x, y2, label = 'Y = sinx')
plt.title('Plot of Y = sinx')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid()
plt.legend()
plt.show()

#(c)
plt.figure(figsize=(5, 3))
plt.plot(x, y3, label='Y = e^x')
plt.title('Plot of Y = e^x')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid()
plt.legend()
plt.show()

#(d) 
plt.figure(figsize=(5, 3))
plt.plot(x, y4, label='Y = log(|x| + 1)')
plt.title('Plot of Y = log(|x| + 1)')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid()
plt.legend()
plt.show()