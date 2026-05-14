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
    # 分類模型 — 邏輯斯回歸（Logistic Regression）

    邏輯斯回歸是一種線性分類模型，會先計算特徵的線性組合，再用 sigmoid 函數把結果轉成 0 到 1 之間的機率。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型重點

    | 項目 | 說明 |
    |---|---|
    | 模型類型 | 損失函數型 |
    | 適合問題 | 二元分類、線性可分資料 |
    | 核心函數 | sigmoid |
    | 優點 | 簡單、速度快、容易解釋 |
    | 限制 | 對複雜非線性資料效果較差 |
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

    random_seed_lr = 42
    return np, plt, random_seed_lr


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sigmoid 函數

    $$\text{sigmoid}(x) = \frac{1}{1 + e^{-x}}$$

    sigmoid 會把任何實數壓到 0 到 1 之間，因此可以把模型輸出解讀成「屬於某一類的機率」。
    """)
    return


@app.cell
def _(np):
    def sigmoid_lr(x):
        return 1 / (1 + np.exp(-x))

    lr_curve_x = np.linspace(-5, 5, 101)
    lr_sigmoid_y = sigmoid_lr(lr_curve_x)
    return lr_curve_x, lr_sigmoid_y


@app.cell
def _(lr_curve_x, lr_sigmoid_y, plt):
    plt.plot(lr_curve_x, lr_sigmoid_y, label="sigmoid", c="b", lw=2)
    plt.axhline(0.5, color="gray", linestyle="--", lw=1)
    plt.legend()
    plt.grid()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 補充：常見 activation function

    Logistic Regression 主要用 sigmoid。神經網路則常看到 tanh 與 ReLU，這裡先一起比較。
    """)
    return


@app.cell
def _(lr_curve_x, np):
    def tanh_lr(x):
        return np.tanh(x)

    def relu_lr(x):
        return np.maximum(0, x)

    lr_tanh_y = tanh_lr(lr_curve_x)
    lr_relu_y = relu_lr(lr_curve_x)
    return lr_relu_y, lr_tanh_y


@app.cell
def _(lr_curve_x, lr_relu_y, lr_sigmoid_y, lr_tanh_y, plt):
    plt.plot(lr_curve_x, lr_sigmoid_y, label="sigmoid", lw=2)
    plt.plot(lr_curve_x, lr_tanh_y, label="tanh", lw=2)
    plt.plot(lr_curve_x, lr_relu_y, label="ReLU", lw=2)
    plt.legend()
    plt.grid()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | 函數 | 輸出範圍 | 中心點 | 常見用途 |
    |---|---|---|---|
    | sigmoid | 0 到 1 | 0.5 | 邏輯斯回歸、二元分類機率 |
    | tanh | -1 到 1 | 0 | 神經網路 hidden layer |
    | ReLU | 0 到無限大 | 無 | 深度學習常用 activation |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 建立人工分類資料

    使用三種二元分類資料觀察模型表現：

    - 線性可分資料
    - 新月形資料
    - 同心圓資料
    """)
    return


@app.cell
def _():
    from sklearn.datasets import make_circles, make_classification, make_moons
    from sklearn.model_selection import train_test_split

    return make_circles, make_classification, make_moons, train_test_split


@app.cell
def _(make_circles, make_classification, make_moons, random_seed_lr):
    lr_data_list = [
        make_classification(
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=random_seed_lr,
            n_clusters_per_class=1,
            n_samples=200,
            n_classes=2,
        ),
        make_moons(noise=0.05, random_state=random_seed_lr, n_samples=200),
        make_circles(noise=0.02, random_state=random_seed_lr, n_samples=200),
    ]
    return (lr_data_list,)


@app.cell
def _(np, plt, random_seed_lr, train_test_split):
    def plot_boundary_lr(ax, x, y, algorithm):
        from matplotlib.colors import ListedColormap

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.5, random_state=random_seed_lr
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

    def plot_boundaries_lr(algorithm, data_list):
        titles = ["線性分隔資料", "新月形資料", "圓形資料"]
        plt.figure(figsize=(15, 4))
        for index, (x, y) in enumerate(data_list):
            ax = plt.subplot(1, len(data_list), index + 1)
            ax.set_title(titles[index])
            plot_boundary_lr(ax, x, y, algorithm)
        plt.show()

    return (plot_boundaries_lr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Logistic Regression 決策邊界

    邏輯斯回歸的邊界本質上是線性的，所以在線性資料表現很好；在新月形與圓形資料中，會因為邊界不夠彈性而受限。
    """)
    return


@app.cell
def _(lr_data_list, plot_boundaries_lr, random_seed_lr):
    from sklearn.linear_model import LogisticRegression

    lr_model = LogisticRegression(random_state=random_seed_lr)
    plot_boundaries_lr(lr_model, lr_data_list)
    return


if __name__ == "__main__":
    app.run()
