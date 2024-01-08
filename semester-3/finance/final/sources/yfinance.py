from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
import yfinance as yf

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

class YahooFinanceFetcher:
    def __init__(self):
        session = CachedLimiterSession(
            limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
            bucket_class=MemoryQueueBucket,
            backend=SQLiteCache("yfinance.cache"),
        )
        session.headers['User-agent'] = 'n.finance/1.0'

        self.session = session

    def get_tickers(self, stocks: list[str]) -> yf.Tickers:
        tickers = yf.Tickers(stocks, session=self.session)
        return tickers
