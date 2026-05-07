import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 大數據資料分析實作 — 分類模型演算法
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 介紹分類模型代表性演算法

    | 演算法名稱 | 實作方式 | 特徵 |
    |---|---|---|
    | 邏輯斯迴歸 | 損失函數型 | 將 sigmoid 函數的輸出值視為機率。分界線為直線。 |
    | 支援向量機 Kernel method | 損失函數型 | 利用 Kernel method 找出非直線的分界。 |
    | 神經網路 | 損失函數型 | 利用增加隱藏層找出非直線的分界。 |
    | 決策樹 | 決策樹型 | 以特定欄位值為基準，進行多次分組。 |
    | 隨機森林 | 決策樹型 | 利用訓練資料的子集合建立多棵決策樹，並取多數決的結果。 |
    | XGBoost | 決策樹型 | 將分類效果不佳的資料建立分類模型，以提高正確率。 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 損失函數（Loss Function）

    **簡單定義**：損失函數就是用來衡量「模型預測」與「實際答案」有多接近的一個數學公式。

    - 當模型預測得**很好**，損失值就很**小**。
    - 當模型預測得**很差**，損失值就很**大**。

    訓練模型的目標是：讓損失函數的值「**越小越好**」，也就是讓預測越來越**準確**。

    我們可以把機器學習的訓練過程想像成「打靶」：

    - 🎯 **真正的目標**：正確答案（例如類別 1）
    - 🎮 **模型預測**：你射出的箭（預測為 0.8 的機率）
    - 📏 **損失函數**：幫你量出這支箭離靶心有多遠
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 損失函數型演算法（Loss Function-based）

    **損失函數型（Lost function）** — 利用誤差最小化來建立分類模型。

    這類模型的核心目的是「**最小化預測錯誤**」，也就是透過**損失函數（Loss Function）**來衡量「預測值」與「真實值」的差距，並藉由訓練過程不斷調整模型參數，讓損失越來越小。

    | 演算法名稱 | 實作方式 | 特徵 |
    |---|---|---|
    | 邏輯斯迴歸 | 損失函數型 | 將 sigmoid 函數的輸出值視為機率。分界線為直線。 |
    | 支援向量機 Kernel method | 損失函數型 | 利用 Kernel method 找出非直線的分界。 |
    | 神經網路 | 損失函數型 | 利用增加隱藏層找出非直線的分界。 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 一、邏輯斯迴歸（Logistic Regression）

    **定義與原理：**
    - 一種**線性**模型，用來做**分類**（尤其是二元分類：是/否、真/假）。
    - 使用 **sigmoid** 函數將線性組合的結果轉為機率值（0 ~ 1），並以機率門檻進行分類。

    **應用場景：**
    - 信用卡詐騙偵測
    - 電子郵件是否為垃圾信
    - 客戶是否會流失（Churn analysis）

    **特色：**
    - 模型**簡單**，**速度快**，容易理解。
    - 適合**特徵彼此獨立**的情況。
    - 若特徵與結果間非線性關係，效果較差。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 二、支援向量機（Support Vector Machine, SVM）

    **定義與原理：**
    - 尋找一條**最佳超平面**，將資料分成兩類，並使分類邊界距離最近的資料點最遠（**最大化邊界**）。
    - 支援**非線性**分類，透過 **Kernel 核心**技巧將資料映射到高維空間進行分隔。

    **應用場景：**
    - 圖像辨識
    - 生物資訊（癌症細胞分類）
    - 文本分類（情感分析）

    **特色：**
    - 對**高維特徵**有效。
    - 支援線性與非線性分類。
    - 訓練速度較慢，**不適合大規模資料**。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 三、神經網路（Neural Network）

    **定義與原理：**
    - 模仿人腦**神經元**運作，透過「**輸入層 → 隱藏層 → 輸出層**」的方式進行資訊處理與分類。
    - 每層神經元計算加權總和後通過非線性激活函數，如 **sigmoid** 或 **ReLU**。

    **應用場景：**
    - 語音辨識、影像識別、自然語言處理（NLP）
    - 自動駕駛、金融風險評估

    **特色：**
    - 適合處理**非線性**、**複雜**問題。
    - 可學習**高階特徵**，但需大量資料與運算資源。
    - 較難解釋模型內部邏輯（黑盒）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 課堂實作範例操作流程
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    # 設定 NumPy 數字顯示格式：suppress=True 關閉科學記號，precision=4 只顯示小數點後 4 位
    np.set_printoptions(suppress=True, precision=4)

    # 設定 Pandas DataFrame 浮點數顯示格式為小數點後 4 位，讓表格數字對齊、易讀
    pd.options.display.float_format = "{:.4f}".format

    # 設定 matplotlib 圖表中所有文字（標題、軸標籤、刻度等）的預設字體大小為 14pt
    plt.rcParams["font.size"] = 14

    # 設定 matplotlib 圖表字體為 PingFang HK（蘋方-港），確保中文字能正確顯示
    plt.rcParams["font.family"] = "PingFang HK"

    # 設定 matplotlib 輸出畫質
    plt.rcParams["figure.dpi"] = 300
    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 實作：畫出 sigmoid 函數的圖形

    **sigmoid 函數**是機器學習中很常見的一個激活函數。

    $$\text{sigmoid}(x) = \frac{1}{1 + e^{-x}}$$

    **用途**：sigmoid 函數會把任何實數 x 映射到 **0 到 1 之間**，常用在：
    - **分類**問題中預測**機率**
    - **神經網路**的激活函數
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 1：定義 sigmoid 函數
    """)
    return


@app.cell
def _(np):
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    return (sigmoid,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `def` 是定義函數的關鍵字，這裡定義一個叫做 `sigmoid` 的函數，參數是 `x`。
    - `np.exp(-x)` 是指數函數 e 的 -x 次方。來自 NumPy 函式庫。
    - `return` 是回傳計算結果。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 2：產生輸入資料 x
    """)
    return


@app.cell
def _(np):
    x = np.linspace(-5, 5, 101)
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `np.linspace` 是 NumPy 裡常用來產生等間距數值的陣列。
    - `-5 到 5`：代表 x 軸的範圍。
    - `101`：表示要產生 101 個點（剛好每 0.1 一個點）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 3：套用 sigmoid 函數產生對應 y 值
    """)
    return


@app.cell
def _(sigmoid, x):
    y = sigmoid(x)
    return (y,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - 把整個 x 陣列傳進 `sigmoid` 函數裡，每一個值都套用公式。
    - 回傳一個一樣長度的陣列 y，是對應的 sigmoid 值。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 4：畫出 sigmoid 曲線
    """)
    return


@app.cell
def _(plt, x, y):
    plt.plot(x, y, label="sigmoid function", c="b", lw=2)
    plt.legend()
    plt.grid()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `plt.plot()` 是畫線圖的函數。
        - `x, y` 是 X 軸與 Y 軸的資料。
        - `label='sigmoid function'`：給這條線一個名稱，待會圖例要用。
        - `c='b'`：線的顏色是藍色（blue）。
        - `lw=2`：線的寬度是 2。
    - `plt.legend()` 顯示圖例
        - 顯示之前用 `label` 設定的名稱。
        - 會自動幫你放在右上角（或自動選擇不擋到線的位置）。
    - `plt.grid()` 顯示背景的格線，幫助看數據的對應位置。
    - `plt.show()` 把圖形顯示出來，是畫圖的最後一步。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **完整流程總結：**
    1. 定義 sigmoid 函數。
    2. 建立從 -5 到 5 的等間距 x 資料。
    3. 計算對應的 y 值。
    4. 把 x 對 y 畫成一條線。
    5. 加上圖例、格線，美化圖形。
    6. 顯示圖表。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **使用時機**：當在做邏輯回歸或神經網路時，想了解 sigmoid 函數如何把「輸入值」轉換為「機率值」，以及為什麼它適合分類（例如 0 與 1）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 實作：畫出 tanh 函數（雙曲正切函數）

    **tanh 函數**是機器學習中另一個激活函數。

    $$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

    - 輸入為任意實數，輸出介於 **-1 和 1 之間**。
    - **用途**：在神經網路中作為激活函數，能強調輸入正負的差異，並保持平滑的非線性。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 1：定義 tanh 函數
    """)
    return


@app.cell
def _(np):
    def tanh(x):
        return np.tanh(x)

    return (tanh,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 2：建立 x 軸資料、計算 y 軸資料
    """)
    return


@app.cell
def _(np, tanh, x):
    tanh_x = np.linspace(-5, 5, 101)
    tanh_y = tanh(x)
    return tanh_x, tanh_y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 3：畫出 tanh 圖形
    """)
    return


@app.cell
def _(plt, tanh_x, tanh_y):
    plt.plot(tanh_x, tanh_y, label="tanh function", c="green", lw=2)
    plt.legend()
    plt.grid()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### sigmoid 和 tanh 比較

    | 函數 | 範圍 | 中心點 | 對稱性 |
    |---|---|---|---|
    | sigmoid | (0, 1) | 0.5 | 非對稱 |
    | tanh | (-1, 1) | 0 | 原點對稱 |

    > **tanh** 通常在訓練神經網路中比 sigmoid **表現更好**一些，因為它的輸出平均值是 0，更容易幫助**梯度下降收斂**。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 實作：畫出 ReLU 函數

    **ReLU（Rectified Linear Unit）**：神經網路中非常重要的激活函數，也是目前在深度學習中最常用的激活函數之一。

    $$\text{ReLU}(x) = \max(0, x)$$

    **用途**：讓神經網路中只保留**正值訊號**，負值直接「砍掉」。這樣可以加速學習並**解決梯度消失**問題。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 1：定義 ReLU 函數
    """)
    return


@app.cell
def _(np):
    def relu(x):
        return np.maximum(0, x)

    return (relu,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `np.maximum(0, x)`：會比較 0 和 x 兩個值，選出「**較大的那個**」。
    - 如果 x 是負的，回傳 0；如果 x 是正的，回傳 x 自己。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 2：建立 x 軸資料、計算 y 軸資料
    """)
    return


@app.cell(hide_code=True)
def _(np, relu, x):
    relu_x = np.linspace(-5, 5, 101)
    relu_y = relu(x)

    relu_y
    return relu_x, relu_y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Step 3：畫出 ReLU 圖形
    """)
    return


@app.cell
def _(plt, relu_x, relu_y):
    plt.plot(relu_x, relu_y, label="ReLU function", c="orange", lw=2)
    plt.legend()
    plt.grid()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 三種激活函數差異比較

    | 函數 | 輸出範圍 | 對稱性 | 是否非線性 | 缺點 |
    |---|---|---|---|---|
    | **Sigmoid** | 0 ~ 1 | 非對稱 | ✅ | 可能造成梯度消失（飽和區） |
    | **Tanh** | -1 ~ 1 | 原點對稱 | ✅ | 飽和區仍可能導致梯度消失 |
    | **ReLU** | 0 ~ ∞ | 非對稱 | ✅ | 對負數輸入為 0（可能導致「死神經元」） |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 實作步驟：支援向量機（SVM）模型

    **SVM 定義與原理：**
    - 尋找一條**最佳超平面**，將資料分成兩類，並使分類邊界距離最近的資料點最遠（**最大化邊界**）。
    - 支援**非線性**分類，透過 **Kernel 核心**技巧將資料映射到**高維空間**進行分隔。

    **SVC（支援向量分類器）**：用來找出可以區分資料的「**最佳邊界**」。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Step 1：引入支援向量機演算法類別
    """)
    return


@app.cell
def _():
    from sklearn.svm import SVC

    random_seed = 42
    return SVC, random_seed


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Step 2：建立分類器，指定使用的「核心函數」
    """)
    return


@app.cell
def _(SVC, random_seed):
    svc_algorithm = SVC(kernel="rbf", random_state=random_seed)
    return (svc_algorithm,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | 參數 | 說明 |
    |---|---|
    | `kernel='rbf'` | 使用 RBF（高斯徑向基底）核心函數，是最常用的非線性分類方式 |
    | `random_state=random_seed` | 設定隨機種子，確保實驗可重現（前面有設定 `random_seed = 123`） |

    > SVC 支援多種 kernel：**linear**（線性）、**poly**（多項式）、**rbf**（高斯）、**sigmoid**，選擇不同 kernel 可以對應不同資料型態。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Step 3：列印出演算法的參數設定
    """)
    return


@app.cell
def _(svc_algorithm):
    svc_algorithm
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Step 4：呼叫畫圖函數，顯示分類結果
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 定義圖形邊界
    """)
    return


@app.cell
def _():
    from sklearn.model_selection import train_test_split

    return (train_test_split,)


@app.cell
def _(np, plt, random_seed, train_test_split):
    def plot_boundary(ax, x, y, algorithm):
        # 將資料隨機分成一半訓練、一半測試
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.5, random_state=random_seed
        )

        # 設定顏色對應圖
        from matplotlib.colors import ListedColormap

        cmap1 = plt.cm.bwr  # 背景顏色（紅藍）
        cmap2 = ListedColormap(["#0000FF", "#000000"])  # 點顏色

        # 設定網格解析度（數值越小，邊界圖越細緻）
        h = 0.005

        # 訓練模型
        algorithm.fit(x_train, y_train)

        # 評估模型的準確率
        score_test = algorithm.score(x_test, y_test)
        score_train = algorithm.score(x_train, y_train)

        # 決策邊界繪圖範圍
        f1_min = x[:, 0].min() - 0.5
        f1_max = x[:, 0].max() + 0.5
        f2_min = x[:, 1].min() - 0.5
        f2_max = x[:, 1].max() + 0.5

        # 建立網格
        f1, f2 = np.meshgrid(np.arange(f1_min, f1_max, h), np.arange(f2_min, f2_max, h))

        # 預測網格上每個點的分類
        if hasattr(algorithm, "decision_function"):
            Z = algorithm.decision_function(np.c_[f1.ravel(), f2.ravel()])
            Z = Z.reshape(f1.shape)
            ax.contour(f1, f2, Z, levels=[0])
        else:
            Z = algorithm.predict_proba(np.c_[f1.ravel(), f2.ravel()])[:, 1]
            Z = Z.reshape(f1.shape)

        # 填色顯示分區（背景決策區域）
        ax.contourf(f1, f2, Z, cmap=cmap1, alpha=0.3)

        # 畫出訓練資料和測試資料
        ax.scatter(x_test[:, 0], x_test[:, 1], c=y_test, cmap=cmap2)
        ax.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=cmap2, marker="x")

        # 顯示訓練與測試的準確率
        text = f"測試:{score_test:.2f}  訓練: {score_train:.2f}"
        ax.text(
            f1.max() - 0.3,
            f2.min() + 0.3,
            text,
            horizontalalignment="right",
            fontsize=18,
        )

    return (plot_boundary,)


@app.cell
def _(plot_boundary, plt):
    def plot_boundaries(algorithm, DataList):
        """
        plot_boundaries 會：

        - 把資料分成訓練集與測試集。
        - 使用 SVM 模型來學習分類邊界。
        - 畫出分類區域、訓練點與測試點。
        - 顯示準確率（訓練 / 測試）。
        """
        N = len(DataList)

        plt.figure(figsize=(15, 4))
        for i, data in enumerate(DataList):
            X, y = data
            ax = plt.subplot(1, N, i + 1)
            plot_boundary(ax, X, y, algorithm)

        plt.show()

    return (plot_boundaries,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 生成相應圖形
    """)
    return


@app.cell
def _():
    from sklearn.datasets import make_circles, make_classification, make_moons

    return make_circles, make_classification, make_moons


@app.cell
def _(make_circles, make_classification, make_moons, random_seed):
    DataList = [
        # 線性分離
        make_classification(
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=random_seed,
            n_clusters_per_class=1,
            n_samples=200,
            n_classes=2,
        ),
        # 新月形
        make_moons(noise=0.05, random_state=random_seed, n_samples=200),
        # 圓形（無法進行線性分離）
        make_circles(noise=0.02, random_state=random_seed, n_samples=200),
    ]
    return (DataList,)


@app.cell
def _(DataList, plot_boundaries, svc_algorithm):
    plot_boundaries(svc_algorithm, DataList)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **結果畫面說明**：執行後會看到三張圖，分別對應：
    - 線性可分的資料
    - 新月型資料
    - 同心圓資料
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 比較四種 SVM Kernel
    """)
    return


@app.cell
def _(DataList, SVC, plot_boundaries, random_seed):
    # 比較四種 kernel 在三種資料集上的分類效果
    kernels = ["linear", "poly", "rbf", "sigmoid"]
    algs = (SVC(kernel=kernel, random_state=random_seed) for kernel in kernels)

    for alg in algs:
        plot_boundaries(alg, DataList)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | Kernel | 線性資料集效果 | 月亮型效果 | 圓形效果 |
    |---|---|---|---|
    | **linear** | 很好 👍 | 不理想 👎 | 不理想 👎 |
    | **poly** | 可能還行 👌 | 視階數而定 | 可用 👌 |
    | **rbf** | 非常靈活 👍 | 很好 👍 | 很好 👍 |
    | **sigmoid** | 效果不穩定 🤔 | 有時可用 | 常常不佳 👎 |

    結果圖為 4 列 × 3 欄，共 12 張子圖：每一列代表一種 kernel，每一欄代表一種資料型態。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### SVM 參數：C（懲罰參數）

    | 參數 | 說明 |
    |---|---|
    | **C** | 是 SVM 的懲罰參數，用來平衡「分類邊界的寬度」和「錯誤分類的容忍度」 |

    - **C 小** → 容忍錯誤較多，邊界較**平滑**（容易 underfit）
    - **C 大** → 容忍錯誤較少，模型更**嚴格**（容易 overfit）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 比較不同 C 值的效果
    """)
    return


@app.cell
def _(DataList, SVC, plot_boundary, plt, random_seed):
    def _():
        # 設定要比較的 C 值
        C_list = [0.01, 0.1, 1, 10, 100]

        # 設定畫布大小（5 種 C）
        plt.figure(figsize=(20, 12))

        # 每個 C 值建模並畫圖
        for i, C_val in enumerate(C_list):
            model = SVC(kernel="rbf", C=C_val, random_state=random_seed)

            for j, (X, y) in enumerate(DataList):
                ax = plt.subplot(len(C_list), len(DataList), i * len(DataList) + j + 1)
                plot_boundary(ax, X, y, model)

                if j == 0:
                    ax.set_ylabel(f"C = {C_val}", fontsize=14)
                if i == 0:
                    titles = ["線性分隔資料", "新月形資料", "圓形資料"]
                    ax.set_title(titles[j], fontsize=14)

        plt.tight_layout()
        plt.show()

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **結果觀察：**
    - C 很小（0.01）：分類邊界很平滑，但容易分類錯誤。
    - C 適中（1）：平衡表現，通常效果佳。
    - C 很大（100）：分類邊界變得非常彎曲，幾乎貼近所有訓練資料，容易 overfit。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### SVM 參數：gamma

    | 參數 | 說明 |
    |---|---|
    | **gamma** | 控制一個訓練樣本影響力的範圍 |

    - **小 gamma** → 影響範圍大 → 模型平滑、**泛化能力強**
    - **大 gamma** → 影響範圍小 → 模型更專注於個別點，**容易 overfit**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 比較不同 gamma 值的分類效果
    """)
    return


@app.cell
def _(DataList, SVC, plot_boundary, plt, random_seed):
    def _():
        # 要測試的 gamma 值
        gamma_list = [0.01, 0.1, 1, 10, 100]

        # 畫布大小（5 個 gamma 值 × 3 資料集）
        plt.figure(figsize=(20, 12))

        # 每個 gamma 值建模並畫圖
        for i, gamma_val in enumerate(gamma_list):
            model = SVC(kernel="rbf", C=1, gamma=gamma_val, random_state=random_seed)

            for j, (X, y) in enumerate(DataList):
                ax = plt.subplot(
                    len(gamma_list), len(DataList), i * len(DataList) + j + 1
                )
                plot_boundary(ax, X, y, model)

                if j == 0:
                    ax.set_ylabel(f"γ = {gamma_val}", fontsize=14)
                if i == 0:
                    titles = ["線性分隔資料", "新月形資料", "圓形資料"]
                    ax.set_title(titles[j], fontsize=14)

        plt.tight_layout()
        plt.show()

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    | gamma 值 | 預期效果 |
    |---|---|
    | 0.01 | 分類邊界很平緩，有點 underfit |
    | 0.1 | 還不錯，適合簡單資料集 |
    | **1** | **通常平衡效果好** |
    | 10 | 分類邊界變彎曲，可能開始 overfit |
    | 100 | 過度貼合訓練資料，邊界複雜，容易 overfit |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### GridSearchCV — 自動找最佳參數

    **GridSearchCV（Grid Search with Cross Validation）**：將指定的所有參數組合都試一遍，透過**交叉驗證（cross-validation）**評估每種組合的效果，挑出效果最好的模型參數組合！
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 程式碼範例（針對「新月形資料」）
    """)
    return


@app.cell
def _(DataList, plot_boundary, plt, random_seed):
    def _():
        from sklearn.model_selection import GridSearchCV
        from sklearn.svm import SVC

        # 取新月資料集（非線性）
        X, y = DataList[1]

        # 定義 SVM 模型（rbf）
        svc = SVC(kernel="rbf", random_state=random_seed)

        # 定義要搜尋的參數組合
        param_grid = {
            "C": [0.01, 0.1, 1, 10, 100],
            "gamma": [0.01, 0.1, 1, 10, 100],
        }

        # 建立 GridSearchCV 物件（5-fold 交叉驗證）
        grid = GridSearchCV(
            estimator=svc, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1
        )

        # 執行搜尋
        grid.fit(X, y)

        # 印出最佳參數
        print("最佳參數組合：", grid.best_params_)
        print("最佳交叉驗證分數：", grid.best_score_)

        # 取出最佳模型並畫圖
        best_model = grid.best_estimator_

        plt.figure(figsize=(6, 4))
        ax = plt.subplot(1, 1, 1)
        plot_boundary(ax, X, y, best_model)
        plt.title("最佳參數下的分類效果")
        plt.show()

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **補充說明：**
    - 若把參數範圍調整得更細，例如 `np.logspace(-2, 2, 10)`，可試更連續的 C 或 gamma。
    - 如果資料量很大，`n_jobs=-1` 可加速運算（使用所有 CPU）。
    - `verbose=1` 可以顯示搜尋進度。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 實作步驟：神經網路（MLPClassifier）模型
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 第一次神經網路分類（使用預設設定）
    """)
    return


@app.cell(hide_code=True)
def _(random_seed):
    from sklearn.neural_network import MLPClassifier

    # 選擇演算法
    mlp_algorithm = MLPClassifier(random_state=random_seed, max_iter=2048)

    # 顯示演算法的參數
    mlp_algorithm
    return MLPClassifier, mlp_algorithm


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    預設值：
    - 隱藏層大小為 `(100,)`（表示只有一層有 100 個神經元）
    - 激活函數為 `'relu'`
    - 學習演算法為 `'adam'`
    """)
    return


@app.cell
def _(DataList, mlp_algorithm, plot_boundaries):
    # 呼叫顯示功能
    plot_boundaries(mlp_algorithm, DataList)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 第二次神經網路分類（自訂隱藏層結構）
    """)
    return


@app.cell
def _(MLPClassifier, random_seed):
    # 隱藏層節點數 = (100, 100)
    mlp_algorithm_with_hidden_layer = MLPClassifier(
        hidden_layer_sizes=(100, 100),
        max_iter=2048,
        random_state=random_seed,
    )

    mlp_algorithm_with_hidden_layer
    return (mlp_algorithm_with_hidden_layer,)


@app.cell
def _(DataList, mlp_algorithm_with_hidden_layer, plot_boundaries):
    # 呼叫顯示功能
    plot_boundaries(mlp_algorithm_with_hidden_layer, DataList)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `hidden_layer_sizes=(100, 100)` 表示模型會有**兩層隱藏層**，每層各 100 個神經元。
    - 改變隱藏層的結構，可以讓模型有更多的能力去**擬合複雜資料**（例如：非線性分布）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 補充說明：為何要用 MLPClassifier？

    **MLP** 是一種「**前饋神經網路**」，適合：
    - ✅ 處理**非線性分類**問題（像新月、同心圓）
    - ✅ **可以調整參數與層數**，以提升表現
    - ✅ 是深度學習的基本入門方法
    """)
    return


if __name__ == "__main__":
    app.run()
