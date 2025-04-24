
from src.crawler import StockCrawler
from src.utils import load_config

config = load_config()
crawler = StockCrawler(config)

# 获取数据（自动切换源）
try:
    df = crawler.get_data("600519.SH", "20250101", "20250418")
    df.to_csv("data/000019.csv", index=False)
except Exception as e:
    print(f"数据获取失败: {e}")
