import pandas as pd
from pypfopt import expected_returns, EfficientSemivariance


def first_algorithm(close: pd.DataFrame, count: pd.Series) -> pd.Series:
    total = sum([c * r for c, r in zip(count, close.iloc[0])])
    weight = pd.Series([
        (c * r) / total
        for c, r in zip(count, close.iloc[0])
    ], index=close.columns, dtype=float)
    return weight

def portfolio_algorithm(close: pd.DataFrame, rate: float) -> pd.Series:
    mu = expected_returns.mean_historical_return(close)
    historical_returns = expected_returns.returns_from_prices(close)

    es = EfficientSemivariance(mu, historical_returns, verbose=True)
    es.efficient_return(rate)
    return pd.Series(es.clean_weights(), index=close.columns, dtype=float)
