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
    # 分類模型 — 神經網路（MLPClassifier）

    神經網路透過輸入層、隱藏層與輸出層逐層轉換資料。每一層都會做加權計算，再通過 activation function，讓模型能學習非線性分類邊界。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型重點

    | 項目 | 說明 |
    |---|---|
    | 模型類型 | 損失函數型 |
    | scikit-learn 類別 | `MLPClassifier` |
    | 重要參數 | `hidden_layer_sizes`、`activation`、`max_iter` |
    | 優點 | 可處理複雜非線性資料 |
    | 限制 | 需要較多資料與運算資源，解釋性較低 |
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

    nn_random_seed = 42
    return nn_random_seed, np, plt


@app.cell
def _():
    from sklearn.datasets import make_circles, make_classification, make_moons
    from sklearn.model_selection import train_test_split
    from sklearn.neural_network import MLPClassifier

    return (
        MLPClassifier,
        make_circles,
        make_classification,
        make_moons,
        train_test_split,
    )


@app.cell
def _(make_circles, make_classification, make_moons, nn_random_seed):
    nn_data_list = [
        make_classification(
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=nn_random_seed,
            n_clusters_per_class=1,
            n_samples=200,
            n_classes=2,
        ),
        make_moons(noise=0.05, random_state=nn_random_seed, n_samples=200),
        make_circles(noise=0.02, random_state=nn_random_seed, n_samples=200),
    ]
    return (nn_data_list,)


@app.cell
def _(nn_random_seed, np, plt, train_test_split):
    def plot_boundary_nn(ax, x, y, algorithm):
        from matplotlib.colors import ListedColormap

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.5, random_state=nn_random_seed
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

    def plot_boundaries_nn(algorithm, data_list):
        titles = ["線性分隔資料", "新月形資料", "圓形資料"]
        plt.figure(figsize=(15, 4))
        for index, (x, y) in enumerate(data_list):
            ax = plt.subplot(1, len(data_list), index + 1)
            ax.set_title(titles[index])
            plot_boundary_nn(ax, x, y, algorithm)
        plt.show()

    return (plot_boundaries_nn,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Activation function

    | 函數 | 說明 |
    |---|---|
    | `relu` | 預設值，深度學習常用，對正值保留、負值變 0 |
    | `tanh` | 輸出介於 -1 到 1 |
    | `logistic` | sigmoid，輸出介於 0 到 1 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 預設神經網路

    `hidden_layer_sizes=(100,)` 表示只有一層隱藏層，裡面有 100 個神經元。
    """)
    return


@app.cell
def _(MLPClassifier, nn_data_list, nn_random_seed, plot_boundaries_nn):
    nn_default_model = MLPClassifier(random_state=nn_random_seed, max_iter=2048)
    plot_boundaries_nn(nn_default_model, nn_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 自訂隱藏層結構

    `hidden_layer_sizes=(100, 100)` 表示有兩層隱藏層，每層各 100 個神經元。層數增加後，模型可以學到更複雜的非線性關係，但也更需要注意過擬合與訓練時間。
    """)
    return


@app.cell
def _(MLPClassifier, nn_data_list, nn_random_seed, plot_boundaries_nn):
    nn_two_layer_model = MLPClassifier(
        hidden_layer_sizes=(100, 100),
        max_iter=2048,
        random_state=nn_random_seed,
    )
    plot_boundaries_nn(nn_two_layer_model, nn_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 小結

    - 神經網路對新月形、圓形資料通常比單純線性模型更有彈性。
    - 隱藏層越多、神經元越多，模型能力越強，但也越容易 overfit。
    - 實務上需要搭配驗證集、交叉驗證或 early stopping 觀察泛化能力。
    """)
    return


if __name__ == "__main__":
    app.run()
