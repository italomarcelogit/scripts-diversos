import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from tabulate import tabulate
import seaborn as sns, matplotlib.pyplot as plt
import warnings
# ML Algoritmos Regressores
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression, PoissonRegressor, SGDClassifier
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyRegressor

# ML classificators
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier

# ML selecao de dados de treino e teste
from sklearn.model_selection import train_test_split, cross_val_score
# calcular o menor erro medio absoluto entre 2 dados apresentados
from sklearn.metrics import mean_absolute_error
# confusion matrics
from sklearn.metrics import confusion_matrix
# metrics
from sklearn import metrics
#
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups

warnings.filterwarnings('ignore')
print('reading dataset')
base = pd.read_csv('labelsMusic2.csv')

print('setup X (feature) and y (target) variables')
X = base['letra']
y = base['cantorId']
# cantores = ['david-bowie', 'paul-mccartney', 'laura-pausini', 'evanescence', 'ac-dc']
nomes = base['cantorNome'].unique()

print(f'Cantores: {nomes}')


def eda(dataset, title='EDA'):
    print(f'=={title}==')
    print('INFO \n')
    print(tabulate(dataset.info(), headers='keys', tablefmt='psql'))
    print('\nHEAD \n', tabulate(dataset.head(), headers='keys', tablefmt='psql'))
    print('\nTAIL \n', tabulate(dataset.tail(), headers='keys', tablefmt='psql'))
    print('\nDESCRIBE \n', tabulate(dataset.describe(), headers='keys', tablefmt='psql'))
    print('\n5 SAMPLES \n', tabulate(dataset.sample(5), headers='keys', tablefmt='psql'))
    print('\nNULLS QTY \n', dataset.isnull().sum().sum())
    print('\nSHAPE \n', tabulate([dataset.shape], headers=['rows', 'cols'], tablefmt='psql'))


# eda(base)

print('converting words in lower size')
palavras = X.str.lower().str.split()
print('creating a dictionary')
dicionario = set()
for i in palavras:
    dicionario.update(i)
palavraEposicao = dict(zip(dicionario, range(len(dicionario))))

print('splitting train and test data')
Xtreino, Xteste, ytreino, yteste = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)
#
print('vetorizing Train Data')
txtvetorizado = TfidfVectorizer()
vetorXtreino = txtvetorizado.fit_transform(Xtreino)

# treinando
print('training')
modelo = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)
modelo.fit(vetorXtreino, ytreino)
#
print('vetorizing Test Data')
vetorXteste = txtvetorizado.transform(Xteste)
print('predicting')
previsao = modelo.predict(vetorXteste)
#
print('generating metrics')

print(metrics.classification_report(yteste.values, previsao, target_names=nomes))

print(modelo.classes_)

confusion_matrix = confusion_matrix(yteste.values, previsao)
print('Matriz da confusão\n')
# plt.matshow(confusion_matrix, cmap='RdBu_r')
# plt.title("Matriz de confusão")
# plt.colorbar()
# plt.ylabel("Classificações corretas")
# plt.xlabel("Classificações")
# plt.show()

print(nomes)
print('Matriz da confusão em pandas\n', pd.crosstab(yteste.values, previsao, rownames=['Real'], colnames=['Previsto'], margins=True))

novafrase = [
    "we used to say we live and let live",
    "Proyecto de vida en comúnlLo sé todo el abismo que ves",
    "Inch worm, inch worm. Measuring the marigolds"
]

novoVetor = txtvetorizado.transform(novafrase)

previsao = modelo.predict(novoVetor)
print('Previsões [predicts]')
for trecho, artista in zip(novafrase, previsao):
    print(f'{trecho}:  {nomes[artista]}')


