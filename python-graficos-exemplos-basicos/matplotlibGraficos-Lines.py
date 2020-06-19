import numpy as np, pandas as pd
import matplotlib.pyplot as plt, matplotlib as mpl


# print(mpl.__version__)
plt.plot([1,2,3],[2,5,9])
plt.show()

x = np.arange(1,11)
y = np.random.randint(1,20,10)
# x = [1, 4, 5]
# y = [3, 7, 2]
plt.plot(x,y, label='Primeira Linha')
plt.plot(x,y,'o', label='Valor Linha')
plt.xlabel('XXX')
plt.ylabel('YYY')
plt.title('TIIIITULO')
plt.legend()
plt.show()