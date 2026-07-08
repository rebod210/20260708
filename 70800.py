
import numpy as np

print("="*40, "练习1", "="*40)
# 练习1
arr = np.random.randint(0, 10, size=(3, 4))
print("原始数组:\n", arr)
reshaped = arr.reshape(4, 3)
transposed = reshaped.T
print("重塑并转置:\n", transposed)
print("大于5的元素:", arr[arr > 5])

print("\n" + "="*40, "练习2", "="*40)
# 练习2
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("第2行第1~3列:", arr2[1, 0:3])
print("所有行第3列:", arr2[:, 2])
print("奇数行:", arr2[::2, :])

print("\n" + "="*40, "练习3", "="*40)
# 练习3
A = np.random.randint(1, 5, size=(2, 3))
B = np.random.randint(1, 5, size=(2, 3))
print("逐元素乘法:\n", A * B)
print("矩阵乘法:\n", A @ B.T)
arr3 = np.array([[1, 2], [3, 4]])
print("按行求和:", np.sum(arr3, axis=1))
print("按列求和:", np.sum(arr3, axis=0))
data = np.array([1.2, 3.5, 2.8])
print("均值:", np.mean(data))
print("标准差:", np.std(data))
print("四舍五入:", np.round(data))

print("\n" + "="*40, "练习4", "="*40)
# 练习4
arr4 = np.random.rand(10)
normalized = (arr4 - arr4.min()) / (arr4.max() - arr4.min()) * 100
print("归一化:\n", normalized)
print("累计和:", np.cumsum(arr4))
print("累计最大值:", np.maximum.accumulate(arr4))