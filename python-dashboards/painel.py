import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# plt.scatter(np.arange(50), np.random.randint(1,50,50))

# PLOT E SCATTER EM PARALELO
# fig = plt.figure()
# ax1 = fig.add_subplot(1,2,1)
# ax1.plot(np.random.randn(50), color='g')
# ax2 = fig.add_subplot(1,2,2)
# ax2.scatter(np.random.randn(50), np.random.randn(50), color='m')
# FIM - PLOT E SCATTER EM PARALELO

# PLOT E SCATTER EM PARALELO - 6 GRAFICOS
# _,ax = plt.subplots(2,3) # tem que colocar o _, antes da variavel
# ax[0,0].plot(np.random.randn(50), color='orange', linestyle='-')
# ax[0,1].plot(np.random.randn(50), color='green', linestyle='-')
# ax[0,2].plot(np.random.randn(50), color='red', linestyle='-')
# ax[1,0].plot(np.random.randn(50), color='yellow', linestyle='-')
# ax[1,1].plot(np.random.randn(50), color='blue', linestyle='-')
# ax[1,2].plot(np.random.randn(50), color='m', linestyle='-')
# FIM - PLOT E SCATTER EM PARALELO


# UTILIZANDO ESCALA PADRAO E LOGARITMICA

def axe1():
    #fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    global fig, axes
    x = np.arange(1,7)
    #axes[0].plot(x, y, x2, y2, color='g')
    #axes.set_color_cycle(['red', 'green', 'yellow'])
    axes[0, 0].clear()
    axes[0,0].plot(x, np.random.randint(250,500,6), color='r')
    axes[0,0].plot(x, np.random.randint(250,500,6), color='g')
    axes[0,0].set_title('tag Python - Default Scale')
    axes[0,0].grid(color='gray', alpha=0.3, linestyle='dashed', linewidth=0.5)
    #axes[1].plot(x, y, x2, y2)
    axes[0, 1].clear()
    axes[0,1].plot(x, np.random.randint(250,500,6), color='b')
    axes[0,1].plot(x, np.random.randint(250,500,6), color='y')
    axes[0,1].set_yscale('log')
    axes[0,1].set_title('tag Python - Log Scale (y)')
    axes[0,1].grid(color='gray', alpha=0.3, linestyle='dashed', linewidth=0.5)
    #axes[2].plot(x, y, x2, np.random.randint(10,220,6))
    axes[0, 2].clear()
    axes[0,2].plot(x, np.random.randint(250,500,6), color='pink')
    axes[0,2].plot(x, np.random.randint(250,500,6), color='deepskyblue')
    axes[0,2].set_yscale('log')
    axes[0,2].set_title('tag Java - Log Scale (y)')
    axes[0,2].grid(color='gray', alpha=0.3, linestyle='dashed', linewidth=0.5)


def axe2():
    #fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    global fig, axes
    x = np.arange(1,7)
    axes[1, 0].clear()
    axes[1,0].bar(x, np.random.randint(250,700,6), color='r')
    axes[1,0].bar(x, np.random.randint(250,700,6), color='g')
    axes[1,0].set_title('EVOLUTION')
    axes[1,0].grid(color='gray', alpha=0.3, linestyle='dashed', linewidth=0.5)
    axes[1, 1].clear()
    axes[1,1].barh(x, np.random.randint(250,700,6), color='b')
    axes[1,1].barh(x, np.random.randint(250,800,6), color='orange')
    axes[1,1].set_title('GROW UP TAGS')
    axes[1,1].grid(color='gray', alpha=0.3, linestyle='dashed', linewidth=0.5)
    #axes[2].plot(x, y, x2, np.random.randint(10,220,6))
    labels = 'python', 'java', 'php', 'SQL', 'others'
    sizes = [15, 30, 45, 10]
    a = np.random.randint(25,45)
    b = np.random.randint(15,25)
    c = np.random.randint(5,20)
    d = np.random.randint(1,100-a-b-c)
    e = 100 - a - b - c -d

    sizes = [a, b, c, d, e]
    explode = (0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    color = ['r','g','orange','b','pink']
    axes[1, 2].clear()
    axes[1,2].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, colors=color)
    axes[1,2].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    axes[1, 2].set_title('LANGUAGES NOTICED %')


def programa1(i):

    axe1()
    axe2()
    plt.pause(1)


if __name__ == '__main__':
    plt.style.use('dark_background')
    plt.rcParams.update({'font.size': 8})
    fig, axes = plt.subplots(2, 3, figsize=(12, 6))
    fig.suptitle('DASHBOARD Twitter Analytics [v1 - @italocosta_]', fontsize=16, color='y')
    refresh = FuncAnimation(plt.gcf(), programa1, interval=1000)
    plt.show()


