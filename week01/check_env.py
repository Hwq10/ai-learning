"""第 1 周：环境自检 + Numpy / Pandas / Matplotlib 上手"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # 无图形窗口也能出图
import matplotlib.pyplot as plt

print("Python:", sys.version.split()[0])

# 1. Numpy：数组运算
a = np.arange(1, 11)
print("numpy 版本:", np.__version__)
print("1~10 的平方:", a ** 2)

# 2. Pandas：表格操作
df = pd.DataFrame({"n": a, "平方": a ** 2})
print("pandas 版本:", pd.__version__)
print(df)

# 3. Matplotlib：画图并保存
plt.plot(a, a ** 2, marker="o")
plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
out = Path(__file__).parent / "y_x2.png"
plt.savefig(out, dpi=100)
print(f"图表已保存到 {out}")
