import numpy as np
import timeit
#任务一
np.random.seed(42)
# 生成矩阵
A = np.random.rand(1000, 2000)
B = np.random.rand(2000, 3000)

# 定义4种运算函数
def f_dot():
    return np.dot(A, B)

def f_at():
    return A @ B

def f_matmul():
    return np.matmul(A, B)

# %timeit 等价Python代码计时
t_dot = timeit.timeit(f_dot, number=3)
t_at = timeit.timeit(f_at, number=3)
t_matmul = timeit.timeit(f_matmul, number=3)

print("=== 矩阵乘法耗时（3次平均）===")
print(f"np.dot:    {t_dot/3:.2f} s")
print(f"@运算符:   {t_at/3:.2f} s")
print(f"np.matmul: {t_matmul/3:.2f} s")
#任务二
# 创建C序、F序数组
arr_c = np.random.rand(1000, 1000)  # 默认C order 行优先
arr_f = np.array(arr_c, order="F")  # 转为Fortran列优先

# 行求和计时
t_c_row = timeit.timeit(lambda: arr_c.sum(axis=1), number=20)
t_f_row = timeit.timeit(lambda: arr_f.sum(axis=1), number=20)

# 列求和计时
t_c_col = timeit.timeit(lambda: arr_c.sum(axis=0), number=20)
t_f_col = timeit.timeit(lambda: arr_f.sum(axis=0), number=20)

print("\n=== 内存布局求和速度 ===")
print(f"C序 行求和: {t_c_row:.3f}s | F序 行求和: {t_f_row:.3f}s")
print(f"C序 列求和: {t_c_col:.3f}s | F序 列求和: {t_f_col:.3f}s")
#任务三
A = np.random.rand(1000, 1000)
# 方案1：普通写法，产生3块临时数组
res1 = A**2 + 2*A + 1

# 方案2：链式ufunc，减少临时分配
res2 = np.add(np.multiply(A, A), np.multiply(2, A), out=np.empty_like(A))
np.add(res2, 1, out=res2)

print("\n表达式结果误差：", np.max(np.abs(res1 - res2)))