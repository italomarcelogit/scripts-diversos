from tabulate import tabulate
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# ML Algoritmos
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression, PoissonRegressor
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyRegressor

# ML selecao de dados de treino e teste e mae
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

warnings.filterwarnings('ignore')

# https://www.kaggle.com/rubenssjr/brasilian-houses-to-rent?select=houses_to_rent_v2.csv

df = pd.read_csv('datasets_casas-aluguel.csv')


def analisandoDataset(dataset, exibetudo=False, titulo='Analisando Dados'):
    print(titulo)
    if exibetudo:
        print('Head:\n', dataset.head(10))
        print('Describe:\n', dataset.describe())
        print('Dados Nulos:\n', dataset.isnull().sum())
        print('Head:\n', dataset.info())
        print('Resumo estatístico do valor do aluguel\n', dataset['rent amount (R$)'].describe())
        print('Resumo estatístico da variável cidade\n', dataset['city'].describe())

    print('Dados Aleatorios: \n', tabulate(dataset.sample(7), headers='keys', tablefmt='psql'))
    print('Shape\n', dataset.shape)


analisandoDataset(dataset=df, exibetudo=False, titulo='Analisando todo o dataset')

apto = df.query('floor != "-" ')

analisandoDataset(dataset=apto, exibetudo=False, titulo='Analisando dataset - Aptos de SP')

varTarget = 'rent amount (R$)'


def correlacao(dataset, variavelTarget, valorMinimo, exibe=False):
    corr = dataset.corr()
    if exibe:
        sns.heatmap(corr, annot=True, fmt='.2f', vmin=-1, vmax=1, cmap='RdBu_r')
        plt.title('Mapa de correlação')
        plt.show()

    correlacoes = corr[variavelTarget]
    print(f'Correlacao das variaveis com a variavel target {variavelTarget}\n {correlacoes}')
    features = []
    for i in range(0, len(correlacoes)):
        if correlacoes[i] > valorMinimo and correlacoes.index[i] != variavelTarget:
            features.append(correlacoes.index[i])
    return features


varFeatures = correlacao(apto, varTarget, valorMinimo=0.5, exibe=False)

print(f'\nTarget: {varTarget}\nFeatures:\n{varFeatures}')

regressores = [
    DecisionTreeRegressor(),
    RandomForestRegressor(),
    SVR(),
    LinearRegression(),
    GradientBoostingRegressor(),
    PoissonRegressor(),
    DummyRegressor(),
    LogisticRegression(),
    GaussianNB()
]


# escolher um algoritmo
def escolherModelo(dfEscolhida, algoritmos, varT, varF, exibeGrafico=False):
    print('\nEscolhendo o melhor algoritmo\n')

    X = dfEscolhida[varF]
    y = dfEscolhida[varT]

    Xtreino, Xteste, ytreino, yteste = train_test_split(X, y, train_size=0.3, random_state=42)

    mae = []
    reg = []

    for regressor in algoritmos:
        regressor.fit(Xtreino, ytreino)
        previsao = regressor.predict(Xteste)
        mae.append(round(mean_absolute_error(yteste, previsao),2))
        reg.append(regressor)

    meuMae = pd.DataFrame(columns=['Regressor', 'Mae'])
    meuMae['Regressor'] = reg
    meuMae['Mae'] = mae
    meuMae = meuMae.sort_values(by='Mae', ascending=True)

    print(tabulate(meuMae, headers='keys', tablefmt='psql'))
    if exibeGrafico:
        sns.boxplot(meuMae.values[0][0].predict(Xteste))
        plt.show()
    return meuMae.values[0][0]

melhorAlgoritmo = escolherModelo(apto, regressores, varTarget, varFeatures, exibeGrafico=False)


# prever o valor de imovel (apto), na cidade de sp, com 3 quartos e 1 banheiro

def previsao(dfEscolhido, mlAlgoritmo, varParams, valorParams, varTarget, desc='Previsão'):
    print(desc)
    x = dfEscolhido[varParams]
    y = dfEscolhido[varTarget]

    modelo = mlAlgoritmo
    modelo.fit(x, y)

    previsao = float(modelo.predict([valorParams]))

    print(f'Sumario:\n'
          f'Algoritmo: {mlAlgoritmo}\n'
          f'Total de imoveis analisados: {len(dfEscolhido)}\n'
          f'Características analisadas:')
    cond = ''
    for i in range(0, len(varParams)):
        print(f' - {varParams[i]}: {valorParams[i]}')
        cond += f' and `{varParams[i]}` == {valorParams[i]}'
    print(f'Valor previsto: R${previsao:.2f}\n'
          f'Valor médio: {dfEscolhido.query(cond[5:])[varTarget].mean():.2f}')


def removeOutliers(dfEscolhido, varTargt):
    print(f'Removendo outliers da variavel {varTarget}')
    print(f'Qtde de registros no dataset antigo: {len(dfEscolhido)}')
    dataset = dfEscolhido[varTarget]

    #criar quartis
    qtl1 = dataset.quantile(0.25)
    qtl3 = dataset.quantile(0.75)

    #calcular o IQR, interquantile range
    iqr = qtl3 - qtl1

    # gerar os limites
    baixo = qtl1 - 1.5 * iqr
    alto = qtl3 + 1.5 * iqr

    # remover os outliers
    novodf = pd.DataFrame()
    limites = dfEscolhido[varTarget].between(left=baixo, right=alto, inclusive=True)
    novodf = pd.concat([novodf, dfEscolhido[limites]])
    print(f'Qtde de registros no novo dataset: {len(novodf)}')
    return novodf


previsao(apto, melhorAlgoritmo, ['rooms'], [2], varTarget, desc='Previsão de Aptos')

semOutlier = removeOutliers(apto, varTarget)

previsao(semOutlier, melhorAlgoritmo, ['rooms'], [2], varTarget,
         desc='Previsão de Aptos - Sem Outliers')
