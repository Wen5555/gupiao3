from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional

class DataSourceClient(ABC):
    @abstractmethod
    def fetch_stock_data(
        self,
        symbol: str,
        start_date: str,
        end_date: str
    ) -> Optional[pd.DataFrame]:
        """所有数据源必须实现此方法"""
        pass

    @staticmethod
    def format_symbol(symbol: str) -> str:
        """统一股票代码格式（如 600519.SH -> 600519）"""
        return symbol.split(".")[0] if "." in symbol else symbol