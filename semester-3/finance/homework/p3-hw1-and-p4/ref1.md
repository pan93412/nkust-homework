如果你有 N 個資產及其對應權重，並且你要計算整個投資組合的風險（變異數），你需要資產的方差和資產間的協方差。計算公式可以推廣為：

\[ Var(\sum_{i=1}^{N}W_i R_i) = \sum_{i=1}^{N} (W_i^2 Var(R_i)) + \sum_{i=1}^{N}\sum_{j \neq i, j=1}^{N} (W_i W_j Cov(R_i, R_j)) \]

這裏，\( Var(R_i) \) 是資產 i 的方差，\( Cov(R_i, R_j) \) 是資產 i 和資產 j 的協方差。

以下是一個簡單的 Python 函數示例，它使用 NumPy 庫來計算給定方差和協方差矩陣的投資組合變異數：

```python
import numpy as np

# 假設 weights 為資產權重的 NumPy 數組
# variances 為資產方差的 NumPy 數組
# covariance_matrix 為資產協方差矩陣的 NumPy 2D 數組

def calculate_portfolio_variance(weights, variances, covariance_matrix):
    # 確保權重和方差矩陣的長度匹配
    assert len(weights) == len(variances) == covariance_matrix.shape[0] == covariance_matrix.shape[1]

    # 計算加權方差
    weighted_variances = weights**2 * variances

    # 計算雙重總和以獲取加權協方差的和
    weighted_covariances_sum = 0
    for i in range(len(weights)):
        for j in range(len(weights)):
            if i != j:
                weighted_covariances_sum += weights[i] * weights[j] * covariance_matrix[i, j]

    # 投資組合的總變異數是加權方差和加權協方差的和
    total_variance = np.sum(weighted_variances) + weighted_covariances_sum
    return total_variance

# 範例使用：
# weights = np.array([...])  # 資產權重列表
# variances = np.array([...])  # 資產方差列表
# covariance_matrix = np.array([...])  # 資產協方差矩陣

# portfolio_variance = calculate_portfolio_variance(weights, variances, covariance_matrix)
# print(portfolio_variance)
```

請注意，此函數假設你已經有協方差矩陣和個別資產的方差。在實際應用中，這些數據通常是通過歷史價格數據計算獲得的。要實現這一點，你可能需要使用財經數據庫的數據，例如 Yahoo 財經或 Google 股票數據，然後使用像 NumPy 這樣的數學函數庫或者像 pandas 與 pandas_datareader 這樣的數據處理庫進行數據加工和計算。
