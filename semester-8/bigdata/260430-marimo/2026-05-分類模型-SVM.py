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
    # 分類模型 — 支援向量機（SVM）

    SVM 會尋找能分開兩類資料的最佳邊界，並讓邊界與最近資料點之間的距離盡可能大。遇到非線性資料時，可以透過 kernel method 把資料映射到較高維度後再分類。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型重點

    | 項目 | 說明 |
    |---|---|
    | 模型類型 | 損失函數型 |
    | 核心概念 | 最大化分類邊界 margin |
    | 重要參數 | `kernel`、`C`、`gamma` |
    | 優點 | 對高維資料有效，可透過 kernel 處理非線性 |
    | 限制 | 大資料量時訓練較慢，參數需要調整 |
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

    svm_random_seed = 42
    return np, plt, svm_random_seed


@app.cell
def _():
    from sklearn.datasets import make_circles, make_classification, make_moons
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC

    return SVC, make_circles, make_classification, make_moons, train_test_split


@app.cell
def _(make_circles, make_classification, make_moons, svm_random_seed):
    svm_data_list = [
        make_classification(
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=svm_random_seed,
            n_clusters_per_class=1,
            n_samples=200,
            n_classes=2,
        ),
        make_moons(noise=0.05, random_state=svm_random_seed, n_samples=200),
        make_circles(noise=0.02, random_state=svm_random_seed, n_samples=200),
    ]
    return (svm_data_list,)


@app.cell
def _(np, plt, svm_random_seed, train_test_split):
    def plot_boundary_svm(ax, x, y, algorithm):
        from matplotlib.colors import ListedColormap

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.5, random_state=svm_random_seed
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

        z = algorithm.decision_function(np.c_[f1.ravel(), f2.ravel()])
        z = z.reshape(f1.shape)

        ax.contourf(f1, f2, z, cmap=cmap_background, alpha=0.3)
        ax.contour(f1, f2, z, levels=[0], colors="black", linewidths=1)
        ax.scatter(x_test[:, 0], x_test[:, 1], c=y_test, cmap=cmap_points)
        ax.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=cmap_points, marker="x")
        ax.text(
            f1.max() - 0.3,
            f2.min() + 0.3,
            f"測試:{score_test:.2f}  訓練:{score_train:.2f}",
            horizontalalignment="right",
            fontsize=14,
        )

    def plot_boundaries_svm(algorithm, data_list):
        titles = ["線性分隔資料", "新月形資料", "圓形資料"]
        plt.figure(figsize=(15, 4))
        for index, (x, y) in enumerate(data_list):
            ax = plt.subplot(1, len(data_list), index + 1)
            ax.set_title(titles[index])
            plot_boundary_svm(ax, x, y, algorithm)
        plt.show()

    return plot_boundaries_svm, plot_boundary_svm


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 基本 SVM：RBF Kernel

    `kernel="rbf"` 是常見的非線性分類 kernel，適合新月形、同心圓這類線性邊界不容易切開的資料。
    """)
    return


@app.cell
def _(SVC, plot_boundaries_svm, svm_data_list, svm_random_seed):
    svm_rbf_model = SVC(kernel="rbf", random_state=svm_random_seed)
    plot_boundaries_svm(svm_rbf_model, svm_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 比較 Kernel

    | Kernel | 適合狀況 |
    |---|---|
    | `linear` | 線性可分資料 |
    | `poly` | 多項式形狀的非線性資料 |
    | `rbf` | 常用、彈性高的非線性資料 |
    | `sigmoid` | 類似神經網路 activation，但分類效果較不穩定 |
    """)
    return


@app.cell
def _(SVC, plot_boundaries_svm, svm_data_list, svm_random_seed):
    for svm_kernel in ["linear", "poly", "rbf", "sigmoid"]:
        print(f"kernel = {svm_kernel}")
        svm_kernel_model = SVC(kernel=svm_kernel, random_state=svm_random_seed)
        plot_boundaries_svm(svm_kernel_model, svm_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 參數 C

    `C` 是懲罰參數，用來平衡「分類邊界寬度」與「錯誤分類容忍度」。

    - `C` 小：容忍錯誤較多，邊界較平滑，可能 underfit。
    - `C` 大：對錯誤更嚴格，邊界更貼近訓練資料，可能 overfit。
    """)
    return


@app.cell
def _(SVC, plot_boundary_svm, plt, svm_data_list, svm_random_seed):
    svm_c_list = [0.01, 0.1, 1, 10, 100]
    plt.figure(figsize=(20, 12))
    for _row_index, _c_value in enumerate(svm_c_list):
        _svm_c_model = SVC(kernel="rbf", C=_c_value, random_state=svm_random_seed)
        for _col_index, (_x, _y) in enumerate(svm_data_list):
            _ax = plt.subplot(len(svm_c_list), len(svm_data_list), _row_index * len(svm_data_list) + _col_index + 1)
            plot_boundary_svm(_ax, _x, _y, _svm_c_model)
            if _col_index == 0:
                _ax.set_ylabel(f"C = {_c_value}", fontsize=14)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 參數 gamma

    `gamma` 控制單一訓練樣本的影響範圍。

    - `gamma` 小：影響範圍大，邊界平滑。
    - `gamma` 大：影響範圍小，容易貼合個別資料點。
    """)
    return


@app.cell
def _(SVC, plot_boundary_svm, plt, svm_data_list, svm_random_seed):
    svm_gamma_list = [0.01, 0.1, 1, 10, 100]
    plt.figure(figsize=(20, 12))
    for _row_index, _gamma_value in enumerate(svm_gamma_list):
        _svm_gamma_model = SVC(kernel="rbf", C=1, gamma=_gamma_value, random_state=svm_random_seed)
        for _col_index, (_x, _y) in enumerate(svm_data_list):
            _ax = plt.subplot(len(svm_gamma_list), len(svm_data_list), _row_index * len(svm_data_list) + _col_index + 1)
            plot_boundary_svm(_ax, _x, _y, _svm_gamma_model)
            if _col_index == 0:
                _ax.set_ylabel(f"gamma = {_gamma_value}", fontsize=14)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## GridSearchCV 自動找參數

    使用交叉驗證測試多組 `C` 與 `gamma`，挑出平均表現最好的參數組合。
    """)
    return


@app.cell
def _(SVC, plot_boundary_svm, plt, svm_data_list, svm_random_seed):
    from sklearn.model_selection import GridSearchCV

    svm_grid_x, svm_grid_y = svm_data_list[1]
    svm_grid_model = SVC(kernel="rbf", random_state=svm_random_seed)
    svm_param_grid = {
        "C": [0.01, 0.1, 1, 10, 100],
        "gamma": [0.01, 0.1, 1, 10, 100],
    }
    svm_grid_search = GridSearchCV(svm_grid_model, svm_param_grid, cv=5, n_jobs=-1)
    svm_grid_search.fit(svm_grid_x, svm_grid_y)

    print("最佳參數組合：", svm_grid_search.best_params_)
    print("最佳交叉驗證分數：", svm_grid_search.best_score_)

    plt.figure(figsize=(6, 4))
    svm_grid_ax = plt.subplot(1, 1, 1)
    plot_boundary_svm(svm_grid_ax, svm_grid_x, svm_grid_y, svm_grid_search.best_estimator_)
    plt.title("最佳參數下的新月形分類效果")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
