import pandas as pd


def standardize_data(raw_df: pd.DataFrame, source: str) -> pd.DataFrame:
    """将不同数据源的字段统一为相同格式"""
    column_mapping = {
        "akshare": {
            "日期": "trade_date",
            "开盘": "open",
            "收盘": "close",
            "最高": "high",
            "最低": "low",
            "成交量": "vol"
        },
        "tushare": {
            "trade_date": "trade_date",
            "open": "open",
            "close": "close",
            "high": "high",
            "low": "low",
            "vol": "vol"
        }
    }

    # 字段重命名
    df = raw_df.rename(columns=column_mapping[source])

    # 确保日期格式统一
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    df = df[["trade_date", "open", "close", "high", "low", "vol"]]  # 固定列顺序
    return df.sort_values("trade_date")