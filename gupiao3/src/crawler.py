from typing import List
import pandas as pd
from src.datasources.akshare_client import AKShareClient
from src.datasources.tushare_client import TushareClient
from src.formatter import standardize_data
from src.utils import setup_logger

logger = setup_logger()


class StockCrawler:
    def __init__(self, config: dict):
        self.sources = config["data_sources"]
        self.tushare_token = config.get("tushare_token")

    def get_data(self, symbol: str, start: str, end: str) -> pd.DataFrame:
        """按优先级尝试多个数据源"""
        for source in self.sources:
            try:
                if source == "akshare":
                    client = AKShareClient()
                elif source == "tushare":
                    client = TushareClient(self.tushare_token)
                else:
                    continue

                raw_df = client.fetch_stock_data(symbol, start, end)
                std_df = standardize_data(raw_df, source)
                logger.info(f"数据源 {source} 获取成功")
                return std_df
            except Exception as e:
                logger.warning(f"数据源 {source} 失败: {str(e)}")
                continue
        raise Exception("所有数据源均不可用")
