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
    # 實作練習：二元分類 — 乳癌資料集
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

    random_seed = 42
    xgboost_version = xgb.__version__
    print("xgboost version:", xgboost_version)
    return np, pd, plt, random_seed


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 混淆矩陣流程：從資料載入到資料劃分
    """)
    return


@app.cell
def _():
    # 從 scikit-learn 載入內建的乳癌資料集（Breast Cancer Wisconsin dataset）
    from sklearn.datasets import load_breast_cancer

    return (load_breast_cancer,)


@app.cell
def _(load_breast_cancer):
    cancer = load_breast_cancer()
    return (cancer,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - 將資料集儲存到變數 `cancer`，包含：
      - `cancer.data`：輸入特徵（每筆樣本有 30 個數值特徵）
      - `cancer.target`：0 表示良性，1 表示惡性
    """)
    return


@app.cell
def _(cancer):
    x = cancer.data
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    將輸入特徵存為變數 $x$（維度為 (樣本數, 特徵數)）
    """)
    return


@app.cell
def _(cancer):
    y = 1 - cancer.target
    return (y,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    為了讓模型更直觀判斷「是否為惡性」，這裡反轉標籤：使**惡性 = 1，良性 = 0**
    """)
    return


@app.cell
def _(x):
    x2 = x[:, :2]
    return (x2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - 為了視覺化簡單，我們只取前兩個特徵來建模。
    - `x[:, :2]` 表示取所有樣本的前 2 個欄位。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 分割資料（訓練 / 測試集）
    """)
    return


@app.cell
def _(random_seed, x2, y):
    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(
        x2, y, train_size=0.7, test_size=0.3, random_state=random_seed
    )
    return x_test, x_train, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `train_test_split`：將資料切分為「訓練集」與「測試集」。
    - `train_size=0.7`：70% 用來訓練模型。
    - `test_size=0.3`：30% 用來測試模型效果。
    - `random_state=random_seed`：保持隨機性一致，讓結果可重複。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 建立與訓練模型（邏輯迴歸）
    """)
    return


@app.cell
def _(random_seed, x_train, y_train):
    from xgboost import XGBClassifier

    algorithm = XGBClassifier(random_state=random_seed)
    algorithm.fit(x_train, y_train)
    return (algorithm,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - 導入並初始化邏輯 XGBoost
    - `random_state` 確保隨機初始化可重現。
    - 將訓練資料送進模型進行訓練（學習如何分類）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 預測與評估準確率
    """)
    return


@app.cell
def _(algorithm, x_test, y_test):
    y_pred = algorithm.predict(x_test)
    score = algorithm.score(x_test, y_test)
    print(f"score: {score:.4f}")
    return (y_pred,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - 使用訓練好的模型來預測測試資料，將結果存在 `y_pred`。
    - 用 `score()` 方法來計算模型正確率（accuracy）。
    - 使用 f-string 印出正確率，保留小數點後 4 位。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 混淆矩陣分析
    """)
    return


@app.cell
def _(y_pred, y_test):
    from sklearn.metrics import confusion_matrix

    matrix = confusion_matrix(y_test, y_pred)
    matrix
    return (matrix,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `confusion_matrix` 根據實際標籤 `y_test` 和預測結果 `y_pred` 計算矩陣，回傳如下格式：

    |                    | 預測=0（良性） | 預測=1（惡性） |
    | ------------------ | :------------: | :------------: |
    | **真實=0（良性）** |   TN（真正）   |   FP（假陽）   |
    | **真實=1（惡性）** |   FN（假陰）   |   TP（真陽）   |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 混淆矩陣美化顯示
    """)
    return


@app.cell
def _(matrix, mo, np, pd):
    def make_cm(matrix: np.ndarray, columns: list[str]) -> pd.DataFrame:
        n = len(columns)

        # 建立列索引與欄索引標籤
        act = ["正確答案數據"] * n
        pred = ["預測結果"] * n

        # 建立 DataFrame，讓混淆矩陣加上標籤
        cm = pd.DataFrame(matrix, columns=[pred, columns], index=[act, columns])
        return cm


    # 使用 make_cm 進行混淆矩陣標記
    cm = make_cm(matrix, ["良性", "惡性"])
    mo.plain(cm)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - 列：實際值（正確答案）
    - 欄：預測值（模型輸出）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 導入評估指標
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    「精準率（Precision）、召回率（Recall）、F1 分數」是分類任務中非常重要的評估指標，特別是在類別不平衡的情況下。
    """)
    return


@app.cell
def _():
    from sklearn.metrics import precision_recall_fscore_support

    return (precision_recall_fscore_support,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - 可以一次計算出精準率（precision）、召回率（recall）、F1 分數（f-score）和 support（樣本數）。
    - 適用於二元與多分類問題。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 計算三個指標
    """)
    return


@app.cell
def _(precision_recall_fscore_support, y_pred, y_test):
    precision, recall, fscore, _ = precision_recall_fscore_support(
        y_test, y_pred, average="binary"
    )
    return fscore, precision, recall


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `y_test`：實際的正確標籤（Ground Truth）
    - `y_pred`：模型預測的標籤
    - `average='binary'`：適用於「二元分類問題」，系統會以 1 為正類，0 為負類來計算。
    - 若是多類別任務，可使用：
      - `'macro'`：對所有類別計算指標的「簡單平均」
      - `'weighted'`：根據每個類別樣本數加權平均
      - `'micro'`：全體混合計算 TP/FP/FN

    **回傳值：**

    - `precision`（精準率）= TP / (TP + FP)
    - `recall`（召回率）= TP / (TP + FN)
    - `fscore`：精準率與召回率的調和平均。F1 = 2 × (precision × recall) / (precision + recall)
    - `_`：support（每個類別在 y*test 中的樣本數），此處用 `*` 忽略。
    """)
    return


@app.cell
def _(fscore, precision, recall):
    print(f"準確率: {precision:.4f}")
    print(f"召回率: {recall:.4f}")
    print(f"F1分數: {fscore:.4f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 使用情境簡介

    | 指標        | 適合關注的情境                                                         |
    | ----------- | ---------------------------------------------------------------------- |
    | **精準率**  | 當「錯把負類當成正類」的成本很高時，例如垃圾信分類、醫療診斷中的誤診。 |
    | **召回率**  | 當「漏判正類」的成本很高時，例如癌症檢測、金融詐欺預測。               |
    | **F1 分數** | 當你需要在精準率與召回率間做出綜合考量時。                             |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## PR 曲線（Precision-Recall Curve）

    PR 曲線是在不均衡分類問題（例如詐欺檢測）中非常實用的指標，它顯示模型在不同閾值下的準確率（precision）與召回率（recall）之間的關係。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 建立 PR 曲線資料
    """)
    return


@app.cell
def _(y_pred, y_test):
    # 導入 precision_recall_curve 函數
    from sklearn.metrics import precision_recall_curve

    # 獲取 precision、recall、以及對應的 threshold 閾值
    prc_precision, prc_recall, prc_thresholds = precision_recall_curve(
        y_test, y_pred
    )
    return prc_precision, prc_recall, prc_thresholds


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `y_test`：實際標籤（0 或 1）
    - `y_proba1`：預測為 1 的機率（即 `predict_proba` 中的第 1 欄）
    - 回傳三個陣列：
      - `precision`：各閾值下的準確率
      - `recall`：各閾值下的召回率
      - `thresholds`：不同的閾值
    """)
    return


@app.cell
def _(pd, prc_precision, prc_recall, prc_thresholds):
    # 將結果放入 DataFrame 中方便檢視
    df_pr = pd.DataFrame([prc_thresholds, prc_precision, prc_recall]).T
    df_pr.columns = ["臨界點", "準確率", "召回率"]
    df_pr
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 繪製 PR 曲線
    """)
    return


@app.cell
def _(plt, prc_precision, prc_recall):
    plt.figure(figsize=(6, 6))  # 設定圖形大小為 6x6 吋
    plt.fill_between(
        prc_recall, prc_precision, 0
    )  # 使用填滿的區域來表示曲線下的面積
    plt.xlim([0.0, 1.0])  # X 軸範圍限制為 0~1
    plt.ylim([0.0, 1.0])  # Y 軸範圍限制為 0~1
    plt.xlabel("召回率")  # 設定 X 軸標籤
    plt.ylabel("準確率")  # 設定 Y 軸標籤
    plt.title("PR曲線")  # 設定圖形標題
    plt.show()  # 顯示圖形
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### PR 曲線的 AUC（面積）
    """)
    return


@app.cell
def _(prc_precision, prc_recall):
    from sklearn.metrics import auc  # 匯入 AUC 計算工具

    pr_auc = auc(prc_recall, prc_precision)  # 計算 PR 曲線下面積
    print(f"PR 曲線下面積: {pr_auc:.4f}")  # 顯示結果（保留四位小數）
    return (auc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `auc(x, y)`：計算以 x 為橫軸、y 為縱軸下的曲線面積。
    - PR 曲線的面積越大，代表模型在不平衡資料上表現越穩定。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ROC 曲線（Receiver Operating Characteristic）

    ROC 曲線用來描述模型在不同閾值下的**真陽性率（TPR）**與**假陽性率（FPR）**，是最常見的二元分類評估工具。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 產生 ROC 曲線資料
    """)
    return


@app.cell
def _(y_pred, y_test):
    from sklearn.metrics import roc_curve

    fpr, tpr, thresholds = roc_curve(y_test, y_pred, drop_intermediate=False)
    return fpr, thresholds, tpr


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `fpr`：假陽性率（False Positive Rate）
    - `tpr`：真陽性率（True Positive Rate），也叫敏感度
    - `thresholds`：對應這些比率的閾值
    """)
    return


@app.cell
def _(fpr, pd, thresholds, tpr):
    df_roc = pd.DataFrame([thresholds, fpr, tpr]).T
    df_roc.columns = ["臨界點", "假陽性率", "敏感度"]

    df_roc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 繪製 ROC 曲線並計算 AUC
    """)
    return


@app.cell
def _(auc, fpr, plt, tpr):
    plt.figure(figsize=(6, 6))
    plt.plot([0, 1], [0, 1], "k--")
    plt.fill_between(fpr, tpr, 0)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel("假陽性率")
    plt.ylabel("敏感度")
    plt.title("ROC 曲線")
    plt.show()

    roc_auc = auc(fpr, tpr)
    print(f"ROC 曲線下面積：{roc_auc:.4f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - `auc(fpr, tpr)`：計算 ROC 曲線下面積（AUC）
    - AUC 越接近 1，模型表現越好；0.5 表示與隨機猜測差不多。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 總結：PR vs. ROC

    | 項目     |          PR 曲線           |     ROC 曲線     |
    | -------- | :------------------------: | :--------------: |
    | 橫軸     |      召回率（Recall）      | 假陽性率（FPR）  |
    | 縱軸     |    精準率（Precision）     | 真陽性率（TPR）  |
    | 適用場景 | 標籤不平衡（少量陽性樣本） | 標籤較均衡時使用 |
    | 衡量指標 |       AUC（PR-AUC）        |  AUC（ROC-AUC）  |
    | 越高越好 |             ✅             |        ✅        |
    """)
    return


if __name__ == "__main__":
    app.run()
