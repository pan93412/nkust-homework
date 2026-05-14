import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 分類模型 — XGBoost（Extreme Gradient Boosting）

    XGBoost 屬於梯度提升樹。它不是一次建立很多獨立的樹，而是一棵接一棵地訓練，每一棵新樹都試著修正前面模型的錯誤。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型重點

    | 項目 | 說明 |
    |---|---|
    | 模型類型 | 決策樹型、Boosting、集成學習 |
    | 核心概念 | 後面的樹修正前面模型的預測誤差 |
    | 重要參數 | `n_estimators`、`learning_rate`、`max_depth`、`subsample` |
    | 優點 | 效能強、準確率高、常用於競賽與實務 |
    | 限制 | 參數較多、調校成本較高 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 與 Random Forest 的差異

    | 項目 | Random Forest | XGBoost |
    |---|---|---|
    | 建樹方式 | 多棵樹大致彼此獨立 | 一棵接一棵修正錯誤 |
    | 集成方法 | Bagging | Boosting |
    | 主要目的 | 降低單棵樹變異 | 逐步降低預測誤差 |
    | 訓練特性 | 可平行化程度高 | 有先後順序，調參更重要 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 常見可調參數

    | 參數名稱 | 說明 |
    |---|---|
    | `n_estimators` | 要建立多少棵樹 |
    | `learning_rate` | 每次修正的步長，越小通常越穩但需要更多樹 |
    | `max_depth` | 每棵樹的最大深度，控制模型複雜度 |
    | `subsample` | 每棵樹訓練時抽樣的資料比例 |
    | `colsample_bytree` | 每棵樹使用的特徵比例 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 基本程式碼範例

    這份專案已經把 `xgboost` 加入 `pyproject.toml`。下面會把 import、資料切分、模型訓練與準確率計算拆成 marimo code cell。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Import 測試

    這個 cell 會實際 import `xgboost` 並顯示目前安裝版本。
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import xgboost as xgb
    from sklearn.datasets import make_circles, make_classification, make_moons
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import GridSearchCV, train_test_split

    np.set_printoptions(suppress=True, precision=4)
    pd.options.display.float_format = "{:.4f}".format
    plt.rcParams["font.size"] = 14
    plt.rcParams["font.family"] = "PingFang HK"
    plt.rcParams["figure.dpi"] = 300

    xgb_random_seed = 42
    xgboost_version = xgb.__version__
    print("xgboost version:", xgboost_version)
    return (
        GridSearchCV,
        accuracy_score,
        make_circles,
        make_classification,
        make_moons,
        np,
        plt,
        train_test_split,
        xgb,
        xgb_random_seed,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 產生分類資料集

    建立一組二元分類資料，並切成訓練集與測試集。
    """)
    return


@app.cell
def _(make_classification, train_test_split, xgb_random_seed):
    xgb_x, xgb_y = make_classification(
        n_samples=1000,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_classes=2,
        random_state=xgb_random_seed,
    )
    xgb_x_train, xgb_x_test, xgb_y_train, xgb_y_test = train_test_split(
        xgb_x,
        xgb_y,
        test_size=0.3,
        random_state=xgb_random_seed,
    )
    return xgb_x_test, xgb_x_train, xgb_y_test, xgb_y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 建立三種視覺化資料

    為了和前面幾章一致，這裡也建立三種二元分類資料，後面會用它們畫出 XGBoost 的決策邊界。
    """)
    return


@app.cell
def _(make_circles, make_classification, make_moons, xgb_random_seed):
    xgb_data_list = [
        make_classification(
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=xgb_random_seed,
            n_clusters_per_class=1,
            n_samples=200,
            n_classes=2,
        ),
        make_moons(noise=0.05, random_state=xgb_random_seed, n_samples=200),
        make_circles(noise=0.02, random_state=xgb_random_seed, n_samples=200),
    ]
    return (xgb_data_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 定義決策邊界繪圖函式

    `plot_boundaries_xgb` 會把同一個 XGBoost 模型套到三種資料上，並畫出訓練集、測試集與分類區域。
    """)
    return


@app.cell
def _(np, plt, train_test_split, xgb_random_seed):
    def plot_boundary_xgb(ax, x, y, algorithm):
        from matplotlib.colors import ListedColormap

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.5, random_state=xgb_random_seed
        )
        cmap_background = plt.cm.bwr
        cmap_points = ListedColormap(["#0000FF", "#000000"])
        h = 0.005

        algorithm.fit(x_train, y_train)
        score_test = algorithm.score(x_test, y_test)
        score_train = algorithm.score(x_train, y_train)

        f1_min, f1_max = x[:, 0].min() - 0.5, x[:, 0].max() + 0.5
        f2_min, f2_max = x[:, 1].min() - 0.5, x[:, 1].max() + 0.5
        f1, f2 = np.meshgrid(np.arange(f1_min, f1_max, h), np.arange(f2_min, f2_max, h))

        z = algorithm.predict_proba(np.c_[f1.ravel(), f2.ravel()])[:, 1]
        z = z.reshape(f1.shape)

        ax.contourf(f1, f2, z, cmap=cmap_background, alpha=0.3)
        ax.scatter(x_test[:, 0], x_test[:, 1], c=y_test, cmap=cmap_points)
        ax.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=cmap_points, marker="x")
        ax.text(
            f1.max() - 0.3,
            f2.min() + 0.3,
            f"測試:{score_test:.2f}  訓練:{score_train:.2f}",
            horizontalalignment="right",
            fontsize=14,
        )

    def plot_boundaries_xgb(algorithm, data_list):
        titles = ["線性分隔資料", "新月形資料", "圓形資料"]
        plt.figure(figsize=(15, 4))
        for _index, (_x, _y) in enumerate(data_list):
            _ax = plt.subplot(1, len(data_list), _index + 1)
            _ax.set_title(titles[_index])
            plot_boundary_xgb(_ax, _x, _y, algorithm)
        plt.show()

    return (plot_boundaries_xgb,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 訓練基本 XGBoost 模型

    先使用常見的起始參數建立模型，訓練後用測試集計算 accuracy。
    """)
    return


@app.cell
def _(
    accuracy_score,
    plot_boundaries_xgb,
    xgb,
    xgb_data_list,
    xgb_random_seed,
    xgb_x_test,
    xgb_x_train,
    xgb_y_test,
    xgb_y_train,
):
    xgb_basic_model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        random_state=xgb_random_seed,
    )
    xgb_basic_model.fit(xgb_x_train, xgb_y_train)
    xgb_basic_pred = xgb_basic_model.predict(xgb_x_test)
    xgb_basic_accuracy = accuracy_score(xgb_y_test, xgb_basic_pred)

    print(f"基本 XGBoost 模型準確率：{xgb_basic_accuracy:.4f}")
    plot_boundaries_xgb(xgb_basic_model, xgb_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 調整 n_estimators 的方向

    | n_estimators | 預期效果 |
    |---|---|
    | 5 | 樹太少，容易 underfit |
    | 50 | 基本可用 |
    | 100 | 常見起始值 |
    | 200 以上 | 可能更準，但也更容易耗時或 overfit |
    """)
    return


@app.cell
def _(
    accuracy_score,
    plot_boundaries_xgb,
    xgb,
    xgb_data_list,
    xgb_random_seed,
    xgb_x_test,
    xgb_x_train,
    xgb_y_test,
    xgb_y_train,
):
    xgb_estimators_results = []
    for _n_estimators in [5, 50, 100, 200]:
        _model = xgb.XGBClassifier(
            n_estimators=_n_estimators,
            max_depth=3,
            learning_rate=0.1,
            random_state=xgb_random_seed,
        )
        _model.fit(xgb_x_train, xgb_y_train)
        _pred = _model.predict(xgb_x_test)
        _accuracy = accuracy_score(xgb_y_test, _pred)
        xgb_estimators_results.append((_n_estimators, _accuracy))
        print(f"n_estimators={_n_estimators}: accuracy={_accuracy:.4f}")
        plot_boundaries_xgb(_model, xgb_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 調整 max_depth 的方向

    | max_depth | 預期效果 |
    |---|---|
    | 2 | 模型較簡單，可能 underfit |
    | 3 到 5 | 常見起始範圍 |
    | 10 | 模型很複雜，容易 overfit |
    """)
    return


@app.cell
def _(
    accuracy_score,
    plot_boundaries_xgb,
    xgb,
    xgb_data_list,
    xgb_random_seed,
    xgb_x_test,
    xgb_x_train,
    xgb_y_test,
    xgb_y_train,
):
    xgb_depth_results = []
    for _max_depth in [2, 3, 5, 10]:
        _model = xgb.XGBClassifier(
            n_estimators=100,
            max_depth=_max_depth,
            learning_rate=0.1,
            random_state=xgb_random_seed,
        )
        _model.fit(xgb_x_train, xgb_y_train)
        _pred = _model.predict(xgb_x_test)
        _accuracy = accuracy_score(xgb_y_test, _pred)
        xgb_depth_results.append((_max_depth, _accuracy))
        print(f"max_depth={_max_depth}: accuracy={_accuracy:.4f}")
        plot_boundaries_xgb(_model, xgb_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## GridSearchCV 範例

    使用 `GridSearchCV` 測試多組 `n_estimators`、`max_depth` 和 `learning_rate`，找出交叉驗證分數最高的組合。
    """)
    return


@app.cell
def _(
    GridSearchCV,
    plot_boundaries_xgb,
    xgb,
    xgb_data_list,
    xgb_random_seed,
    xgb_x_train,
    xgb_y_train,
):
    xgb_grid_model = xgb.XGBClassifier(random_state=xgb_random_seed)
    xgb_param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [3, 5, 7],
        "learning_rate": [0.03, 0.1, 0.3],
    }

    xgb_grid_search = GridSearchCV(
        estimator=xgb_grid_model,
        param_grid=xgb_param_grid,
        cv=5,
        scoring="accuracy",
        n_jobs=-1,
    )
    xgb_grid_search.fit(xgb_x_train, xgb_y_train)

    print("最佳參數：", xgb_grid_search.best_params_)
    print("最佳交叉驗證分數：", xgb_grid_search.best_score_)
    plot_boundaries_xgb(xgb_grid_search.best_estimator_, xgb_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 小結

    - XGBoost 是樹模型家族中常見的高效能 boosting 方法。
    - 它通常比單棵決策樹與一般 Random Forest 更需要調參。
    - 實務上常從 `n_estimators`、`learning_rate`、`max_depth` 開始搜尋。
    """)
    return


if __name__ == "__main__":
    app.run()
