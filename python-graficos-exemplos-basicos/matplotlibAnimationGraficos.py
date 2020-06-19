import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np, pandas as pd



def animate(i):
    global pos, DF, data, data2, DADOS


    xs = range(0,pos+1)
    ys = []
    ys2 = []
    line = 0



    while line<=pos:
        ys.append(data[line])
        ys2.append(data2[line])
        line += 1



    ax1.clear()





    VETOR = []

    print(f'Pos: {pos}')
    i = 0
    while i<=pos:
        VET = []
        for c,v in enumerate(DADOS[i]):
            VET.append(v)
        print(f'vetor: {VET}')
        VETOR.append(VET)
        print(f'VETORZAO: {VETOR}')
        i += 1





    print(f'YS: {ys}')
    print(f'YS2: {ys2}')

    ax1.plot(xs, ys, color='red', label='tag RED')
    ax1.plot(xs, ys, 'o', color='red')
    ax1.plot(xs, ys2, color='g', label='tag GREEN')
    ax1.plot(xs, ys2, 'o', color='g')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Live graph with matplotlib')


    if pos < len(data)-1:
        pos += 1
    else:
        pos = 0



plt.style.use('dark_background')
fig = plt.figure(figsize=(6, 8))
# creating a subplot
ax1 = fig.add_subplot(1, 1, 1)
pos = 0

DICTA = {'hora': [0, 1, 2, 3, 4, 5],
         'covid': np.random.randint(1, 100, 6),
         'bozo': np.random.randint(1, 200, 6),
         'teste': np.random.randint(1, 100, 6)
         }
DF = pd.DataFrame(DICTA)
DADOS = []
for INDEX, LINHA in DF.iterrows():
    MONTA = []
    for HEAD in DF.columns:
        if HEAD != 'hora':
            MONTA.append(LINHA[HEAD])
    DADOS.append(MONTA)
print(f'dados:\n{DADOS}')

data = DF['covid']
data2 = DF['teste']

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()