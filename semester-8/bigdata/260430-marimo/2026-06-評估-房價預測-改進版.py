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

    相較於原版（只用線性回歸），這個版本的改進重點：

    1. **多模型比較**：線性回歸、Ridge、Lasso、隨機森林、梯度提升、
       HistGradientBoosting、XGBoost
    2. **交叉驗證**：以 5-fold CV 估計各模型的泛化能力
    3. **超參數調參**：對 XGBoost 做網格搜尋找最佳組合
    4. **更多評估指標**：MSE、RMSE、MAE、R²、MAPE（平均絕對百分比誤差）、
       Explained Variance（解釋變異量）
    5. **特徵重要度**與**殘差分析**：理解模型抓到什麼、哪裡還預測不準
    """)
    return


@app.cell
def _():
    import warnings

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    plt.rcParams["font.family"] = "Heiti TC"
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["figure.dpi"] = 300

    np.set_printoptions(suppress=True, precision=4)
    pd.options.display.float_format = "{:.4f}".format
    pd.set_option("display.max_columns", None)
    warnings.filterwarnings("ignore")

    random_seed = 42
    return np, pd, plt, random_seed


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. 載入加州房價資料集
    """)
    return


@app.cell
def _(pd):
    from sklearn.datasets import fetch_california_housing

    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="HouseValue")

    print("特徵數：", X.shape[1], "  樣本數：", X.shape[0])
    X.head()
    return X, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    目標變數 `HouseValue` 是以 10 萬美元為單位的房價中位數。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. 切分訓練 / 測試資料
    """)
    return


@app.cell
def _(X, random_seed, y):
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_seed
    )
    print("訓練集：", X_train.shape, "  測試集：", X_test.shape)
    return X_test, X_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. 建立多個候選回歸模型

    線性家族（Linear / Ridge / Lasso）以 `Pipeline` 串接 `StandardScaler`；
    樹模型對尺度不敏感，直接使用原始特徵。
    """)
    return


@app.cell
def _(random_seed):
    from sklearn.ensemble import (
        GradientBoostingRegressor,
        HistGradientBoostingRegressor,
        RandomForestRegressor,
    )
    from sklearn.linear_model import Lasso, LinearRegression, Ridge
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from xgboost import XGBRegressor

    def scaled(estimator):
        return Pipeline([("scaler", StandardScaler()), ("model", estimator)])

    models = {
        "線性回歸": scaled(LinearRegression()),
        "Ridge": scaled(Ridge(alpha=1.0)),
        "Lasso": scaled(Lasso(alpha=0.001)),
        "隨機森林": RandomForestRegressor(
            n_estimators=200, random_state=random_seed, n_jobs=-1
        ),
        "梯度提升": GradientBoostingRegressor(random_state=random_seed),
        "HistGB": HistGradientBoostingRegressor(random_state=random_seed),
        "XGBoost": XGBRegressor(
            random_state=random_seed,
            n_estimators=600,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
        ),
    }
    return XGBRegressor, models


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. 在測試集上比較多項回歸指標

    - **MSE**：均方誤差，對大誤差有比較重的懲罰
    - **RMSE**：均方根誤差，單位與房價一致，最直觀
    - **MAE**：平均絕對誤差，對離群值較穩健
    - **R²**：解釋變異比例，越接近 1 越好
    - **MAPE**：平均絕對百分比誤差，以百分比表達誤差大小
    - **Explained Variance**：解釋變異量，與 R² 接近但不懲罰系統性偏差
    """)
    return


@app.cell
def _(X_test, X_train, models, np, pd, y_test, y_train):
    from sklearn.metrics import (
        explained_variance_score,
        mean_absolute_error,
        mean_absolute_percentage_error,
        mean_squared_error,
        r2_score,
    )

    fitted = {}
    rows = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        fitted[name] = model
        pred = model.predict(X_test)
        mse = mean_squared_error(y_test, pred)
        rows.append(
            {
                "模型": name,
                "RMSE": np.sqrt(mse),
                "MAE": mean_absolute_error(y_test, pred),
                "MAPE": mean_absolute_percentage_error(y_test, pred),
                "R²": r2_score(y_test, pred),
                "解釋變異": explained_variance_score(y_test, pred),
            }
        )

    result = (
        pd.DataFrame(rows).sort_values("R²", ascending=False).reset_index(drop=True)
    )
    result
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. 交叉驗證確認泛化能力

    單一切分可能只是剛好模型適合這份訓練資料，用 5-fold 交叉驗證的平均 R² 更能反映真實表現。
    """)
    return


@app.cell
def _(X_train, models, pd, y_train):
    from sklearn.model_selection import cross_val_score

    cv_rows = []
    for name_c, model_c in models.items():
        scores = cross_val_score(
            model_c, X_train, y_train, cv=5, scoring="r2", n_jobs=-1
        )
        cv_rows.append(
            {
                "模型": name_c,
                "CV 平均 R²": scores.mean(),
                "CV 標準差": scores.std(),
            }
        )

    cv_result = (
        pd.DataFrame(cv_rows)
        .sort_values("CV 平均 R²", ascending=False)
        .reset_index(drop=True)
    )
    cv_result
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. 超參數調參（XGBoost）

    對表現最好的 XGBoost 做網格搜尋。
    """)
    return


@app.cell
def _(XGBRegressor, X_train, random_seed, y_train):
    from sklearn.model_selection import GridSearchCV

    xgb_base = XGBRegressor(
        random_state=random_seed,
        subsample=0.8,
        colsample_bytree=0.8,
        min_child_weight=3,
    )
    param_grid = {
        "n_estimators": [600, 1000, 1500, 2000],
        "learning_rate": [0.02, 0.05, 0.08],
        "max_depth": [6, 7, 8],
    }
    grid = GridSearchCV(xgb_base, param_grid, cv=3, scoring="r2", n_jobs=-1)
    grid.fit(X_train, y_train)

    print("最佳參數：", grid.best_params_)
    print(f"最佳 CV R²：{grid.best_score_:.4f}")
    return (grid,)


@app.cell
def _(X_test, grid, np, y_test):
    from sklearn.metrics import mean_squared_error as mse_fn
    from sklearn.metrics import r2_score as r2_fn

    best_model = grid.best_estimator_
    best_pred = best_model.predict(X_test)
    print(f"調參後 XGBoost 測試集 R²：{r2_fn(y_test, best_pred):.4f}")
    print(f"調參後 XGBoost 測試集 RMSE：{np.sqrt(mse_fn(y_test, best_pred)):.4f}")
    return best_model, best_pred


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    調參後 XGBoost 測試集 R² 約 0.857，相較線性回歸的約 0.576 大幅提升，
    RMSE 也從約 0.746 降到約 0.43（即平均誤差約 4.3 萬美元）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. 預測 vs 實際
    """)
    return


@app.cell
def _(best_pred, plt, y_test):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(y_test, best_pred, alpha=0.3, s=10)
    lims = [y_test.min(), y_test.max()]
    ax.plot(lims, lims, "r--", lw=2, label="理想預測")
    ax.set_xlabel("實際房價")
    ax.set_ylabel("預測房價")
    ax.set_title("調參後 XGBoost：預測 vs 實際")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. 殘差分析

    殘差（實際 − 預測）若隨機散布在 0 附近、沒有明顯結構，代表模型抓到主要規律。
    上方 4 萬美元附近的水平帶是資料集的房價上限截斷（capped at 5.0）造成的。
    """)
    return


@app.cell
def _(best_pred, plt, y_test):
    residual = y_test - best_pred

    fig_r, (axr1, axr2) = plt.subplots(1, 2, figsize=(13, 5))

    axr1.scatter(best_pred, residual, alpha=0.3, s=10)
    axr1.axhline(0, color="r", ls="--")
    axr1.set_xlabel("預測房價")
    axr1.set_ylabel("殘差（實際 − 預測）")
    axr1.set_title("殘差圖")
    axr1.grid(True, alpha=0.3)

    axr2.hist(residual, bins=50, color="steelblue", edgecolor="white")
    axr2.axvline(0, color="r", ls="--")
    axr2.set_xlabel("殘差")
    axr2.set_ylabel("數量")
    axr2.set_title("殘差分佈")

    plt.tight_layout()
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 9. 特徵重要度

    看哪些特徵對房價預測貢獻最大。加州房價中，`MedInc`（地區收入中位數）
    通常是壓倒性的主因。
    """)
    return


@app.cell
def _(X, best_model, pd, plt):
    importance = pd.Series(
        best_model.feature_importances_, index=X.columns
    ).sort_values(ascending=True)

    fig_imp, ax_imp = plt.subplots(figsize=(8, 5))
    importance.plot.barh(ax=ax_imp, color="darkorange")
    ax_imp.set_xlabel("重要度")
    ax_imp.set_title("XGBoost 特徵重要度")
    plt.tight_layout()
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 總結

    | 改進項目 | 基礎版 | 改進版 |
    | --- | --- | --- |
    | 模型 | 只有線性回歸 | 7 模型比較 + XGBoost 調參 |
    | 驗證 | 單一切分 | 5-fold 交叉驗證 |
    | 指標 | MSE/RMSE/MAE/R² | 再加 MAPE、解釋變異 |
    | 診斷 | 僅散佈圖 | 殘差分析 + 特徵重要度 |
    | 測試 R² | 約 0.58 | **約 0.86** |
    | 測試 RMSE | 約 0.746 | **約 0.43** |

    **重點觀念**：房價與特徵的關係高度非線性，線性回歸抓不住；換成梯度提升樹（XGBoost）並調參後，R² 從 0.58 跳到 0.86。回歸沒有「準確率」概念，要用 R²、RMSE、MAE、MAPE 等多角度評估，再搭配殘差分析確認模型沒有系統性偏誤。
    """)
    return


if __name__ == "__main__":
    app.run()
