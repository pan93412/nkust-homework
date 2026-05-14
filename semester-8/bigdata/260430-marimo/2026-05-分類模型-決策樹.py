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
    # 分類模型 — 決策樹（Decision Tree）

    決策樹用一連串「如果...則...」的條件切分資料。每個節點是一個判斷條件，每個葉節點代表最後的分類結果。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型重點

    | 項目 | 說明 |
    |---|---|
    | 模型類型 | 決策樹型 |
    | 核心概念 | 透過條件式分割建立樹狀分類規則 |
    | 重要參數 | `max_depth`、`min_samples_split`、`criterion` |
    | 優點 | 直觀、容易視覺化、不需要特徵標準化 |
    | 限制 | 容易過擬合，對資料雜訊敏感 |
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

    tree_random_seed = 42
    return np, plt, tree_random_seed


@app.cell
def _():
    from sklearn import tree
    from sklearn.datasets import load_iris, make_circles, make_classification, make_moons
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier

    return (
        DecisionTreeClassifier,
        load_iris,
        make_circles,
        make_classification,
        make_moons,
        train_test_split,
        tree,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Iris 資料集範例

    Iris 資料集共有 150 筆資料、3 種花類別。這裡使用 scikit-learn 內建資料集，避免需要外部下載。
    """)
    return


@app.cell
def _(load_iris):
    iris_raw = load_iris(as_frame=True)
    iris_df = iris_raw.frame
    iris_df["species_name"] = iris_df["target"].map(
        dict(enumerate(iris_raw.target_names))
    )
    iris_df.head()
    return (iris_raw,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 建立決策樹模型

    先用完整 Iris 資料訓練一棵決策樹，再用 `plot_tree` 直接畫出樹狀規則。
    """)
    return


@app.cell
def _(DecisionTreeClassifier, iris_raw, tree_random_seed):
    iris_x = iris_raw.data
    iris_y = iris_raw.target
    iris_tree_model = DecisionTreeClassifier(random_state=tree_random_seed)
    iris_tree_model.fit(iris_x, iris_y)
    return (iris_tree_model,)


@app.cell
def _(iris_raw, iris_tree_model, plt, tree):
    plt.figure(figsize=(16, 8))
    tree.plot_tree(
        iris_tree_model,
        feature_names=iris_raw.feature_names,
        class_names=list(iris_raw.target_names),
        filled=True,
        rounded=True,
        impurity=False,
    )
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 人工資料決策邊界

    下面使用和 2026-05-07 相同概念的三種人工資料，觀察決策樹在不同資料分布上的分類邊界。
    """)
    return


@app.cell
def _(make_circles, make_classification, make_moons, tree_random_seed):
    tree_data_list = [
        make_classification(
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=tree_random_seed,
            n_clusters_per_class=1,
            n_samples=200,
            n_classes=2,
        ),
        make_moons(noise=0.05, random_state=tree_random_seed, n_samples=200),
        make_circles(noise=0.02, random_state=tree_random_seed, n_samples=200),
    ]
    return (tree_data_list,)


@app.cell
def _(np, plt, train_test_split, tree_random_seed):
    def plot_boundary_tree(ax, x, y, algorithm):
        from matplotlib.colors import ListedColormap

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.5, random_state=tree_random_seed
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

    def plot_boundaries_tree(algorithm, data_list):
        titles = ["線性分隔資料", "新月形資料", "圓形資料"]
        plt.figure(figsize=(15, 4))
        for index, (x, y) in enumerate(data_list):
            ax = plt.subplot(1, len(data_list), index + 1)
            ax.set_title(titles[index])
            plot_boundary_tree(ax, x, y, algorithm)
        plt.show()

    return (plot_boundaries_tree,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 預設深度

    預設情況下決策樹會持續切分到符合停止條件為止，因此邊界可能非常細碎，也比較容易 overfit。
    """)
    return


@app.cell
def _(
    DecisionTreeClassifier,
    plot_boundaries_tree,
    tree_data_list,
    tree_random_seed,
):
    tree_default_model = DecisionTreeClassifier(random_state=tree_random_seed)
    plot_boundaries_tree(tree_default_model, tree_data_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 限制樹深度

    `max_depth=3` 會限制樹最多切到 3 層，通常可以降低過擬合風險，但如果限制太嚴格，也可能造成 underfit。
    """)
    return


@app.cell
def _(
    DecisionTreeClassifier,
    plot_boundaries_tree,
    tree_data_list,
    tree_random_seed,
):
    tree_depth3_model = DecisionTreeClassifier(max_depth=3, random_state=tree_random_seed)
    plot_boundaries_tree(tree_depth3_model, tree_data_list)
    return


if __name__ == "__main__":
    app.run()
