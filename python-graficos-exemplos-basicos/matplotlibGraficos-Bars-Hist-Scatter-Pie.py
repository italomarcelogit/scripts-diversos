import numpy as np, pandas as pd
import matplotlib.pyplot as plt, matplotlib as mpl


x = np.arange(1,11)
y = np.random.randint(1,20,10)
w = np.arange(1,11)
z = np.random.randint(1,20,10)

# plt.bar(x,y, label='Barras', color='r')
# plt.bar(w,z, label='Barras', color='y')
# plt.legend()
# plt.show()

idades = np.random.randint(20,90,20)
#list comphreension
ids = [x for x in range(len(idades))]
# print(ids)
plt.bar(ids,idades)
plt.show()

bins = np.arange(0,140,10)
# print(bins)
plt.hist(idades,bins,histtype='stepfilled', rwidth=0.8)
plt.show()

plt.scatter(x,y,label='Scatter Plot pontos', color='r', marker='o', s=100)
plt.legend()
plt.show()

fatias = [7,3,5,6]
atividades = list('ABCD')
colunas = list('cmrk')
plt.pie(fatias, labels=atividades, colors=colunas, startangle=90, shadow=True)


plt.show()

