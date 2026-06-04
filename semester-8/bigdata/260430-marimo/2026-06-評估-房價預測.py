import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 實作練習：房價預測

    1. 資料讀取與預覽
    2. 資料前處理
    3. 切分訓練與測試資料
    4. 建立回歸模型（以線性回歸為例）
    5. 模型訓練
    6. 模型預測
    7. 模型評估（MSE、RMSE、MAE、R²）
    8. 結果視覺化與解釋
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import xgboost as xgb

    plt.rcParams["font.family"] = "Heiti TC"
    plt.rcParams["figure.dpi"] = 300

    np.set_printoptions(suppress=True, precision=4)
    pd.options.display.float_format = "{:.4f}".format
    # 顯示資料框中的所有項目
    pd.set_option("display.max_columns", None)

    xgboost_version = xgb.__version__
    print("xgboost version:", xgboost_version)
    return np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 實作案例：使用加州房價資料集
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1. 載入資料與預覽
    """)
    return


@app.cell
def _(pd):
    from sklearn.datasets import fetch_california_housing

    # 載入加州房價資料集
    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="HouseValue")
    return X, y


@app.cell
def _(X):
    X.head()  # 特徵資料（例如：人口、房間數、收入等）
    return


@app.cell
def _(y):
    y.head()  # 目標變數（房價，以千美元為單位）
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. 資料切分
    """)
    return


@app.cell
def _(X, y):
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_test, X_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    將資料分成訓練集 80% 和測試集 20%。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. 建立與訓練模型
    """)
    return


@app.cell
def _(X_train, y_train):
    from sklearn.linear_model import LinearRegression

    # 建立線性回歸模型
    model = LinearRegression()
    model.fit(X_train, y_train)
    return (model,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4. 預測與模型評估
    """)
    return


@app.cell
def _(X_test, model, np, y_test):
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    # 模型預測
    y_pred = model.predict(X_test)

    # 評估指標計算
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"MSE:  {mse:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"MAE:  {mae:.3f}")
    print(f"R²:   {r2:.3f}")
    return (y_pred,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #
    ### 模型結果視覺化
    """)
    return


@app.cell
def _(plt, y_pred, y_test):
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2)
    plt.xlabel("實際房價")
    plt.ylabel("預測房價")
    plt.title("預測 vs 實際")
    plt.grid(True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    若點多數集中在紅色虛線（理想預測）附近，代表預測效果佳。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 迴歸問題 — 指標應用說明

    | 指標     | 效果           | 適用情境               |
    | -------- | -------------- | ---------------------- |
    | **MSE**  | 對誤差懲罰大   | 偏好準確率但容忍離群值 |
    | **RMSE** | 與原始單位相符 | 對於直觀呈現效果佳     |
    | **MAE**  | 對離群值不敏感 | 預測較穩健             |
    | **R²**   | 模型解釋能力   | 判斷整體模型品質       |
    """)
    return


if __name__ == "__main__":
    app.run()
