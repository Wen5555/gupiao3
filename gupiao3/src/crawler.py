import akshare as ak
import pandas as pd
from typing import Optional

def fetch_stock_data(
    symbol: str,
    start_year: int = 2020,
    end_year: int = 2023,
    adjust: str = "hfq"
) -> Optional[pd.DataFrame]:
    """通过 AKShare 获取股票历史数据"""
    try:
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period="daily",
            start_date=f"{start_year}0101",
            end_date=f"{end_year}1231",
            adjust=adjust
        )
        return df
    except Exception as e:
        print(f"数据获取失败: {e}")
        return None

def save_to_csv(df: pd.DataFrame, filename: str) -> None:
    """保存数据到CSV文件"""
    df.to_csv(f"data/{filename}.csv", index=False)