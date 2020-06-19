import pandas as pd
import numpy as np
import datetime

# creating aleatory sales dataset
def dsSales(nreg=500):
    alpha = ('abcdefghijklmnopqrstuvwxyz'.upper())
    #creating lists
    produto = []
    catproduto = []
    qtde = []
    valores = []
    descontos = []
    totais = []
    lojas = []
    clientes = []
    id = []
    datas = []
    startdate = datetime.date(2019, 1, 1)
    meses = []
    vendedores = []
    # inputs aleatory in lists
    for i in np.arange(1,nreg+1):
        id.append(i)
        produto.append(alpha[np.random.randint(0, len(alpha)-1, 1)[0]])
        catproduto.append(alpha[np.random.randint(0,10)][0])
        vendedores.append(alpha[np.random.randint(13, len(alpha) - 1, 1)[0]])
        qtd = np.random.randint(1,10,1)[0]
        qtde.append(qtd)
        valor = np.random.randint(150,300,1)[0]
        valores.append(valor)
        total = qtd * valor
        desc = np.random.randint(0,5,1)[0]/100
        descontos.append(desc)
        totais.append(total - (total * desc))
        lojas.append(alpha[np.random.randint(0,len(alpha)-1,1)[0]])
        clientes.append(alpha[np.random.randint(0,len(alpha)-1,1)[0]])
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
    tabela['DATA'] = datas
    tabela['PERIODO'] = tabela.DATA.dt.to_period('M')
    tabela['MES'] = meses
    return tabela



# carregando dados
vendas = dsSales(1000) # Sales Table with (N) rows - year 2019 - aleatory data created
print(vendas.describe())
# below top products
top = vendas.groupby('PRODUTO').sum().sort_values(by='QTDE', ascending=False)
top5produtos = top.head(5)
#print(top5produtos)
# below sales by month - source 2019 - aleatory data created
totalVendasPorMes = vendas.groupby('MES').TOTAL.sum().head(12) # Sales month by month - jan to dec 2019
#print(totalVendasPorMes)
# CONTAINERS DATA
KPI1 = vendas.QTDE.sum() # Total Sales 2019 - units
KPI2 = int(vendas.TOTAL.sum()) # Total Sales 2019 - cash

KPI31 = top5produtos.index[0] # Product top 1 - name - 2019
KPI32 = top5produtos.QTDE[0] # Product top 1 - units - 2019

KPI41 = top.index[len(top)-1] # Product top 1 - name - 2019
KPI42 = top.QTDE[len(top)-1] # Product top 1 - units - 2019
#print(KPI1, KPI2, KPI31, KPI32, KPI41, KPI42)
#data graphOne - bar -
xg1 = top5produtos.index # return product names
yg1 = top5produtos.QTDE # return product units
#print(xg1, yg1)
#data graphTwo
xg2 = totalVendasPorMes.index # return months 2019 jan to dec
yg2 = totalVendasPorMes.values # return values cash month by month jan to dec
#print(totalVendasPorMes, xg2, yg2)

# data to best sales person
topVendores = vendas.groupby('VENDEDOR').sum().sort_values(by='TOTAL', ascending=False).head(1)
nomeV = topVendores.index[0]
vendedor = vendas.query(f"VENDEDOR == '{nomeV}'")
pmv = vendedor.groupby('PRODUTO').sum().sort_values(by='QTDE', ascending=False).head(1)
pmvStr = f'Produto mais vendido: {pmv.index[0]} - {pmv.QTDE[0]} units'
mf = vendedor.groupby('MES').sum().sort_values(by='TOTAL', ascending=False).head(1)
mfStr = f'Maior faturamento: US${mf.TOTAL.values}. Ref.: {mf.index[0]}/2019 '
tvpmpv = vendedor.groupby('MES').TOTAL.sum().head(12)
xg3 = tvpmpv.index
yg3 = tvpmpv.values