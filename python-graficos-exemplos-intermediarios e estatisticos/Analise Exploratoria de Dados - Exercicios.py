import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorsys
import warnings
from sklearn.datasets import load_iris



def exercicio():
    iris = load_iris()
    #print(iris.describe)
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df2 = df.copy()
    df2['target'] = iris.target
    target = pd.DataFrame()
    target['target'] = iris.target
    df2['especie'] = df2['target'].apply(lambda a: iris.target_names[a])
    features = pd.DataFrame({'features': iris.feature_names})
    print(features)
    df2.groupby('especie')[df2.columns].mean()
    print(df2.transpose)
    print(df2.info)
    print(df2.describe())
    print(df2.isnull().sum())
    for i in iris.feature_names:
        print(i, ': ', df2[i].count(), '\n')

    # Crie um Histograma de sepal length
    exclude = ['Id', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target']
    df2.loc[:, df.columns.difference(exclude)].hist()
    plt.figure(figsize=(15, 10))


    # Crie um Gráficos de Dispersão (scatter Plot) da variável sepal length versus número da linha,
    # colorido por marcadores da variável target
    plt.figure(figsize=(12, 8), dpi=80)
    plt.scatter(range(len(df2)), df2['petal width (cm)'], c=df2['target'])
    plt.xlabel('Número da Linha', fontsize=8)
    plt.ylabel('Sepal length (cm)', fontsize=8)
    plt.title('Gráfico de Dispersão dos Atributos, colorido por marcadores da classe alvo', fontsize=8)

    # Crie um Scatter Plot de 2 Features (atributos)
    plt.figure(figsize=(12, 8), dpi=80)
    plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'], c=df2['target'])
    plt.xlabel('petal length (cm)', fontsize=8)
    plt.ylabel('petal width (cm)', fontsize=8)

    # Crie um Scatter Matrix das Features (atributos)
    attributes = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    pd.plotting.scatter_matrix(df2[attributes], figsize=(16, 12))

    # Crie um Histograma de todas as features
    df2.hist(figsize=(12, 12))
    plt.show()


if __name__ == '__main__':
    exercicio()
