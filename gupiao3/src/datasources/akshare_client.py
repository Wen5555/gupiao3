import akshare as ak
from .base_client import DataSourceClient
import pandas as pd

class AKShareClient(DataSourceClient):
    def fetch_stock_data(
        self, symbol: str, start_date: str, end_date: str
    ) -> pd.DataFrame:
        clean_symbol = self.format_symbol(symbol)
        df = ak.stock_zh_a_hist(
            symbol=clean_symbol,
            period="daily",
            start_date=start_date,
            end_date=end_date,
            adjust="qfq"
        )
        return df