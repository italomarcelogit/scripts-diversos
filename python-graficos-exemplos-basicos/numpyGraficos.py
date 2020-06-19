import numpy as np
import matplotlib.pyplot as plt


# plt.scatter(np.arange(50), np.random.randint(1,50,50))

# PLOT E SCATTER EM PARALELO
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.plot(np.random.randn(50), color='g')
ax2 = fig.add_subplot(1,2,2)
ax2.scatter(np.random.randn(50), np.random.randn(50), color='m')
# FIM - PLOT E SCATTER EM PARALELO

# PLOT E SCATTER EM PARALELO - 6 GRAFICOS
_,ax = plt.subplots(2,3) # tem que colocar o _, antes da variavel
ax[0,0].plot(np.random.randn(50), color='orange', linestyle='-')
ax[0,1].plot(np.random.randn(50), color='green', linestyle='-')
ax[0,2].plot(np.random.randn(50), color='red', linestyle='-')
ax[1,0].plot(np.random.randn(50), color='yellow', linestyle='-')
ax[1,1].plot(np.random.randn(50), color='blue', linestyle='-')
ax[1,2].plot(np.random.randn(50), color='m', linestyle='-')
# FIM - PLOT E SCATTER EM PARALELO


# UTILIZANDO ESCALA PADRAO E LOGARITMICA

fig, axes = plt.subplots(1,2,figsize=(12,6))
x = [0,1,2,3,4,5]
y = [1,3,6,10,15,20]
x2 = [0,1,2,3,4,5]
y2 = [5,10,26,50,80,130]
axes[0].plot(x,y,x2,y2)
axes[0].set_title('Escala Padrao')
axes[0].grid(True)
axes[1].plot(x,y,x2,y2)
axes[1].set_yscale('log')
axes[1].set_title('Escala Logaritmica (y)')
axes[1].grid(color='gray', alpha=0.3, linestyle='dashed', linewidth=0.5)

plt.show()