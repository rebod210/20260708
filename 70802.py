#任务一
import numpy as np
prices = np.array([100, 102, 105, 103, 107])
# 对数收益率公式 ln(Pt / Pt-1)
log_returns = np.log(prices[1:] / prices[:-1])
print("每日对数收益率：", log_returns)
#任务二
np.random.seed(42)
price_100 = np.random.normal(loc=100, scale=5, size=100)

def moving_avg_conv(data, window):
    kernel = np.ones(window) / window
    return np.convolve(data, kernel, mode="valid")

ma5 = moving_avg_conv(price_100, window=5)
ma20 = moving_avg_conv(price_100, window=20)
print(f"原始价格长度: {len(price_100)} | MA5长度: {len(ma5)} | MA20长度: {len(ma20)}")
#任务三
np.random.seed(42)
# shape=(股票数, 交易日) 1000×252
returns = np.random.normal(loc=0.001, scale=0.02, size=(1000, 252))

# 1. 年化波动率 = 日标准差 * sqrt(252)
daily_std = np.std(returns, axis=1)
annual_vol = daily_std * np.sqrt(252)
print("前5支股票年化波动率：", annual_vol[:5])

# 2. 股票相关系数矩阵 (1000×1000)
corr_matrix = np.corrcoef(returns)
print("相关矩阵形状：", corr_matrix.shape)