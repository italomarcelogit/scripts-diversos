import pylab as pl
import matplotlib.pyplot as plt

# x = pl.linspace(0,5,10)
# y = x ** 2
#
# fig = plt.figure()
#
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
#
# #figura1
# axes1.plot(x,y, 'r')
# axes1.set_xlabel('X')
# axes1.set_ylabel('Y')
# axes1.set_title('Title 1')
#
# #figura2
# axes2.plot(x,y, 'y')
# axes2.set_xlabel('X')
# axes2.set_ylabel('Y')
# axes2.set_title('Title 2')
#
# plt.show(axes1)
# plt.show(axes2)


### GRAFICOS EM PARALELO ####
x = [1,2,3,4]
y = [3,6,9,12]
x2 = [2,4,6,8,]
y2 = [3,1,9,4]

fig, axes = plt.subplots(nrows=2, ncols=1)
c = 0
for ax in axes:
    if c==0:
        ax.plot(x,y,'r')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Titulo 1')
    else:
        ax.plot(x2, y2, 'y')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Titulo 2')
    c += 1


plt.show(fig.tight_layout())