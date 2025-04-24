import tushare as ts
from .base_client import DataSourceClient
import pandas as pd

class TushareClient(DataSourceClient):
    def __init__(self, token: str):
        ts.set_token(token)
        self.pro = ts.pro_api()

    def fetch_stock_data(
        self, symbol: str, start_date: str, end_date: str
    ) -> pd.DataFrame:
        clean_symbol = self.format_symbol(symbol)
        df = self.pro.daily(
            ts_code=f"{clean_symbol}.SH",  # 假设默认沪市，可扩展深市判断
            start_date=start_date,
            end_date=end_date
        )
        return df