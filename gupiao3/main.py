from src.crawler import fetch_stock_data, save_to_csv
from src.analyzer import analyze_data

if __name__ == "__main__":
    symbol = "000001"     #获取的股票代码
    stock_data = fetch_stock_data(symbol, start_year=2010)

    if stock_data is not None:
        # 保存原始数据
        save_to_csv(stock_data, f"{symbol}_historical")

        # 执行可视化分析，保存结果
        analyze_data(stock_data, symbol)
        print("数据处理完成！结果已保存至 data 目录")