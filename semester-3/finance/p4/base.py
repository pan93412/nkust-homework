import pandas as pd

from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)
session.headers['User-agent'] = 'n.finance/1.0'

stocks = ['2330.TW', '2317.TW', '1216.TW']
tickers = yf.Tickers(stocks, session=session)

close = tickers.history(start='2013-12-31', end='2016-12-31', auto_adjust=False)["Close"]
returns = close.pct_change()
