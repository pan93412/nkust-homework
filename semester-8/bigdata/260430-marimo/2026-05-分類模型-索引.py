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
    # 大數據資料分析實作 — 分類模型索引

    這份 notebook 是拆分後的索引頁。原本的 `2026-05-07.py` 保留不動；下面每一份 notebook 都可以獨立開啟，並且各自重複定義需要的套件、資料集與繪圖函式。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Notebook 清單

    | Notebook | 主題 | 內容 |
    |---|---|---|
    | `2026-05-分類模型-邏輯斯回歸.py` | Logistic Regression | sigmoid、tanh、ReLU、線性分類邊界 |
    | `2026-05-分類模型-SVM.py` | Support Vector Machine | kernel、C、gamma、GridSearchCV |
    | `2026-05-分類模型-神經網路.py` | MLPClassifier | 隱藏層、activation、非線性分類 |
    | `2026-05-分類模型-決策樹.py` | Decision Tree | Iris 範例、樹深度、決策邊界 |
    | `2026-05-分類模型-隨機森林.py` | Random Forest | bagging、n_estimators、max_depth、GridSearchCV |
    | `2026-05-分類模型-XGBoost.py` | XGBoost | boosting、重要參數、可選執行範例 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型分類方式

    | 類型 | 模型 | 核心想法 |
    |---|---|---|
    | 損失函數型 | Logistic Regression | 用 sigmoid 把線性輸出轉成機率，透過損失函數調整參數 |
    | 損失函數型 | SVM | 找到最大化 margin 的分類邊界，kernel 可處理非線性 |
    | 損失函數型 | Neural Network | 透過隱藏層與 activation function 學習複雜非線性 |
    | 決策樹型 | Decision Tree | 用一連串條件切分資料 |
    | 決策樹型 | Random Forest | 建立多棵樹後多數決，降低單棵樹過擬合 |
    | 決策樹型 | XGBoost | 一棵接一棵修正前面模型的錯誤 |
    """)
    return


if __name__ == "__main__":
    app.run()
