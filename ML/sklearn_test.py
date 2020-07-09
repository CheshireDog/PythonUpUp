# coding = utf-8

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
try:
    from scipy.special import comb
except:
     from scipy.misc import comb

# 生成伪随机数
rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
# plt.scatter(x, y)
# plt.show()
model = LinearRegression()
X = x[:, np.newaxis]
model.fit(X, y)
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)
plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()