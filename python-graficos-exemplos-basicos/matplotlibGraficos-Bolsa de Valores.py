import numpy as np, pandas as pd, sys, matplotlib.pyplot as plt
from matplotlib import style


ts = pd.Series(np.random.randn(500), index=pd.date_range('1/1/2016', periods=500))
ts = ts.cumsum()
plt.show(plt.plot(ts))

df = pd.DataFrame(np.random.randn(500,4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure()
plt.legend(loc='best')
plt.show(plt.plot(df))




