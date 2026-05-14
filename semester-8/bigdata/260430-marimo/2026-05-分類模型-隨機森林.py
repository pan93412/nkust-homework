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
    # 分類模型 — 隨機森林（Random Forest）

    隨機森林由多棵決策樹組成。每棵樹會使用部分資料與部分特徵訓練，最後用多數決決定分類結果。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型重點

    | 項目 | 說明 |
    |---|---|
    | 模型類型 | 決策樹型、集成學習 |
    | 核心概念 | Bagging + 多棵樹多數決 |
    | 重要參數 | `n_estimators`、`max_depth`、`max_features` |
    | 優點 | 穩定、抗過擬合能力比單棵樹好 |
    | 限制 | 訓練成本較高，解釋性比單棵決策樹低 |
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    np.set_printoptions(suppress=True, precision=4)
    pd.options.display.float_format = "{:.4f}".format
    plt.rcParams["font.size"] = 14
    plt.rcParams["font.family"] = "PingFang HK"
    plt.rcParams["figure.dpi"] = 300

    rf_random_seed = 42
    return np, plt, rf_random_seed


@app.cell
def _():
    from sklearn.datasets import make_circles, make_classification, make_moons
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    return (
        RandomForestClassifier,
        make_circles,
        make_classification,
        make_moons,
        train_test_split,
    )


@app.cell
def _(make_circles, make_classification, make_moons, rf_random_seed):
    rf_data_list = [
        make_classification(
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=rf_random_seed,
            n_clusters_per_class=1,
            n_samples=200,
            n_classes=2,
        ),
        make_moons(noise=0.05, random_state=rf_random_seed, n_samples=200),
        make_circles(noise=0.02, random_state=rf_random_seed, n_samples=200),
    ]
    return (rf_data_list,)


@app.cell
def _(np, plt, rf_random_seed, train_test_split):
    def plot_boundary_rf(ax, x, y, algorithm):
        from matplotlib.colors import ListedColormap

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.5, random_state=rf_random_seed
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

    def plot_boundaries_rf(algorithm, data_list):
        titles = ["線性分隔資料", "新月形資料", "圓形資料"]
        plt.figure(figsize=(15, 4))
        for index, (x, y) in enumerate(data_list):
            ax = plt.subplot(1, len(data_list), index + 1)
            ax.set_title(titles[index])
            plot_boundary_rf(ax, x, y, algorithm)
        plt.show()

    return plot_boundaries_rf, plot_boundary_rf


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 基本 Random Forest

    `n_estimators` 是森林中樹的數量。預設值通常已經可用，但資料越複雜時，增加樹的數量可以讓結果更穩定。
    """)
    return


@app.cell
def _(
    RandomForestClassifier,
    plot_boundaries_rf,
    rf_data_list,
    rf_random_seed,
):
    rf_default_model = RandomForestClassifier(random_state=rf_random_seed)
    plot_boundaries_rf(rf_default_model, rf_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 調整 n_estimators

    | n_estimators | 特性 |
    |---|---|
    | 5 | 訓練快，但結果較不穩定 |
    | 20 | 小型資料基本可用 |
    | 100 | 實務常用預設 |
    | 500 | 更穩定，但訓練較慢 |
    """)
    return


@app.cell
def _(
    RandomForestClassifier,
    plot_boundaries_rf,
    rf_data_list,
    rf_random_seed,
):
    for rf_tree_count in [5, 20, 100, 500]:
        print(f"n_estimators = {rf_tree_count}")
        rf_estimators_model = RandomForestClassifier(
            n_estimators=rf_tree_count,
            random_state=rf_random_seed,
        )
        plot_boundaries_rf(rf_estimators_model, rf_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 調整 max_depth

    `max_depth` 限制每棵樹的最大深度，可以用來控制模型複雜度。
    """)
    return


@app.cell
def _(
    RandomForestClassifier,
    plot_boundaries_rf,
    rf_data_list,
    rf_random_seed,
):
    for rf_depth in [2, 5, 10, None]:
        print(f"max_depth = {rf_depth}")
        rf_depth_model = RandomForestClassifier(
            max_depth=rf_depth,
            random_state=rf_random_seed,
        )
        plot_boundaries_rf(rf_depth_model, rf_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## GridSearchCV 自動找參數

    這裡示範用第一組資料搜尋 `n_estimators` 與 `max_depth` 的較佳組合。
    """)
    return


@app.cell
def _(
    RandomForestClassifier,
    plot_boundary_rf,
    plt,
    rf_data_list,
    rf_random_seed,
    train_test_split,
):
    from sklearn.model_selection import GridSearchCV

    rf_grid_x, rf_grid_y = rf_data_list[0]
    rf_x_train, rf_x_test, rf_y_train, rf_y_test = train_test_split(
        rf_grid_x, rf_grid_y, test_size=0.3, random_state=rf_random_seed
    )
    rf_param_grid = {
        "n_estimators": [10, 50, 100],
        "max_depth": [3, 5, 10, None],
    }
    rf_grid_model = RandomForestClassifier(random_state=rf_random_seed)
    rf_grid_search = GridSearchCV(rf_grid_model, rf_param_grid, cv=5)
    rf_grid_search.fit(rf_x_train, rf_y_train)

    print("最佳參數組合：", rf_grid_search.best_params_)
    print("最佳交叉驗證準確率：", rf_grid_search.best_score_)
    print("測試集準確率：", rf_grid_search.score(rf_x_test, rf_y_test))

    plt.figure(figsize=(6, 4))
    rf_grid_ax = plt.subplot(1, 1, 1)
    plot_boundary_rf(rf_grid_ax, rf_grid_x, rf_grid_y, rf_grid_search.best_estimator_)
    plt.title("Random Forest GridSearchCV")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
