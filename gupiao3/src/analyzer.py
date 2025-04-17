import pandas as pd
import matplotlib.pyplot as plt


def analyze_data(df: pd.DataFrame, symbol: str) -> None:
    """基础数据分析与可视化"""
    # 计算关键指标
    df["日期"] = pd.to_datetime(df["日期"])
    df.set_index("日期", inplace=True)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题
    # 绘制价格走势
    plt.figure(figsize=(12, 6))
    df["收盘"].plot(title=f"{symbol} 历史收盘价走势")
    plt.xlabel("日期")
    plt.ylabel("价格（后复权）")
    plt.savefig(f"data/{symbol}_price_trend.png")
    plt.close()