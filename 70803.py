import numpy as np
import matplotlib.pyplot as plt

# 任务1 NumPy数组基础操作
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_3d = np.arange(24).reshape(2, 3, 4)

print(arr_1d[:3])
print(arr_2d[1, 2])
print(arr_2d[:2, :2])
print(arr_3d[0, :, 1])

reshape_arr = arr_1d.reshape(5, 1)
flat_arr = arr_2d.flatten()
trans_arr = arr_2d.T

def mat_add(a, b):
    if a.shape != b.shape:
        raise ValueError("维度不匹配")
    return a + b

def mat_mul(a, b):
    if a.shape[1] != b.shape[0]:
        raise ValueError("矩阵无法相乘")
    return np.dot(a, b)

def mat_t(a):
    return a.T

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(mat_add(A,B))
print(mat_mul(A,B))
print(mat_t(A))

rand_data = np.random.randn(100)
print(np.mean(rand_data), np.var(rand_data), np.std(rand_data), np.max(rand_data), np.min(rand_data))

# 任务2 金融数据分析
np.random.seed(42)
day_num = 200
price_a = np.cumsum(np.random.randn(day_num)) + 100
price_b = np.cumsum(np.random.randn(day_num)) + 95

def get_ret(price):
    return np.log(price[1:] / price[:-1])

def get_vol(ret, year=252):
    return np.std(ret) * np.sqrt(year)

ret_a = get_ret(price_a)
ret_b = get_ret(price_b)
vol_a = get_vol(ret_a)
vol_b = get_vol(ret_b)

def sma(series, win=20):
    return np.convolve(series, np.ones(win)/win, mode="valid")
ma20 = sma(price_a)

ret_mat = np.vstack([ret_a, ret_b])
cov_mat = np.cov(ret_mat)
weight = np.array([0.5, 0.5])
port_var = weight @ cov_mat @ weight
port_vol = np.sqrt(port_var * 252)

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(14,6))
plt.subplot(2,1,1)
plt.plot(price_a)
plt.plot(np.arange(19, day_num), ma20)
plt.subplot(2,1,2)
plt.plot(ret_a)
plt.plot(ret_b)
plt.tight_layout()
plt.show()