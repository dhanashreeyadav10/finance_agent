
# import numpy as np
# from sklearn.linear_model import LinearRegression

# def forecast_series(series, days=10):
#     y = series.values
#     X = np.arange(len(y)).reshape(-1, 1)
#     model = LinearRegression().fit(X, y)
#     future_X = np.arange(len(y), len(y) + days).reshape(-1, 1)
#     return model.predict(future_X)

import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_series(series, days=10):
    series = series.dropna()
    if len(series) < 2:
        return []

    y = series.values
    X = np.arange(len(y)).reshape(-1, 1)

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(y), len(y) + days).reshape(-1, 1)
    return model.predict(future_X)
