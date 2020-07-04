import pandas as pd
import numpy as np
from tabulate import tabulate
import datetime

# creating aleatory sales dataset
def dsSales(nreg=500):
    alpha = list('abcdefghijklmnopqrstuvwxyz'.upper())
    #creating lists
    produto = []
    catproduto = []
    qtde = []
    valores = []
    descontos = []
    totais = []
    lojas = []
    clientes = []
    sexo = []
    ec = []
    id = []
    datas = []
    startdate = datetime.date(2019, 1, 1)
    meses = []
    vendedores = []
    # inputs aleatory in lists
    for i in np.arange(1,nreg+1):
        id.append(i)
        produto.append(''.join(np.random.choice(alpha, 1)))
        catproduto.append(''.join(np.random.choice(alpha[0:3], 2)))
        vendedores.append(''.join(np.random.choice(alpha[3:5], 5)))
        qtd = np.random.randint(1,10,1)[0]
        qtde.append(qtd)
        valor = np.random.randint(150,300,1)[0]
        valores.append(valor)
        total = qtd * valor
        desc = np.random.randint(0,5,1)[0]/100
        descontos.append(desc)
        totais.append(total - (total * desc))
        lojas.append(''.join(np.random.choice(alpha[5:7], 4)))
        clientes.append(''.join(np.random.choice(alpha, 6)) + ' ' + ''.join(np.random.choice(alpha, 8)))
        sexo.append(''.join(np.random.choice(['m', 'f', 'a', '-'], 1, p=[0.4, 0.4, 0.1, 0.1])))
        ec.append(''.join(np.random.choice(['c', 's', 'd', '-'], 1)))
        date = startdate + datetime.timedelta(int(np.random.randint(1, 365, 1)[0]))
        datas.append(pd.Timestamp(date))
        meses.append(pd.Timestamp(date).month)

    # building Sales Pandas DataFrame
    tabela = pd.DataFrame()
    tabela['ID'] = id
    tabela['PRODUTO'] = produto
    tabela['CATEGORIA PRODUTO'] = catproduto
    tabela['QTDE'] = qtde
    tabela['VALOR'] = valores
    tabela['DESCONTO'] = descontos
    tabela['TOTAL'] = totais
    tabela['LOJA'] = lojas
    tabela['VENDEDOR'] = vendedores
    tabela['CLIENTE'] = clientes
    tabela['SEXO'] = sexo
    tabela['ESTADO CIVIL'] = ec
    tabela['DATA'] = datas
    tabela['PERIODO'] = tabela.DATA.dt.to_period('M')
    tabela['MES'] = meses
    return tabela

dados = dsSales(150000)
print(tabulate(dados, headers='keys', tablefmt='psql'))
print(dados.isnull().sum())
dados.to_csv ('dataset_vendas_random.csv', index = False, header=True)
# print(dados['SEXO'].describe(), dados['CATEGORIA PRODUTO'].describe(), dados['LOJA'])