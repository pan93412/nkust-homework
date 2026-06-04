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
    ## 模型評估

    當完成分類模型的建立後，**模型評估**是非常關鍵的步驟，可幫助我們了解模型的**預測效能**與**實際表現**。

    ### 不同類型任務的評估指標差異

    | 類型 | 常用指標 |
    |------|----------|
    | **分類問題** | 準確率、混淆矩陣、Precision、Recall、F1-score、ROC、PR |
    | **迴歸問題** | MSE、RMSE、MAE、R²（決定係數） |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型評估 — 分類問題

    分類問題的三個常用模型評估指標：

    - **準確率**（Accuracy）
    - **混淆矩陣**（Confusion Matrix）
    - **分類報告**（Classification Report）
      - Precision（精確率）
      - Recall（召回率）
      - F1-score
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 準確率（Accuracy）

    **定義：** 準確率是最簡單也最直觀的評估指標，表示模型**預測正確的比例**。

    **計算公式：**

    $$
    \text{Accuracy} = \frac{\text{正確預測的樣本數}}{\text{總樣本數}} = \frac{TP + TN}{TP + TN + FP + FN}
    $$

    - **TP**（True Positive）：實際是正，預測也為正
    - **TN**（True Negative）：實際是負，預測也為負
    - **FP**（False Positive）：實際是負，卻預測為正（**誤報**）
    - **FN**（False Negative）：實際是正，卻預測為負（**漏報**）

    **解釋：** 高準確率代表大部分預測正確，但不一定代表模型好（在不平衡資料集上可能誤導）。

    **適用情況：**
    - 當各分類樣本數量大致相同，準確率是可靠的指標。
    - 在資料「不平衡」（例如：90% 是 A 類別，10% 是 B）時不適用。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 混淆矩陣（Confusion Matrix）

    **定義：** 混淆矩陣是一種用來衡量**模型預測結果**的表格工具，呈現模型預測與實際分類的對照關係，即能夠具體了解**模型在各類別上的預測表現**。

    #### 二元分類範例

    |  | 實際 Positive | 實際 Negative |
    |--|:---:|:---:|
    | **預測 Positive** | TP | FP |
    | **預測 Negative** | FN | TN |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 混淆矩陣詳細說明

    |  | 實際為正類（1） | 實際為負類（0） |
    |--|:---:|:---:|
    | **預測為正類（1）** | TP（真正） | FP（假正） |
    | **預測為負類（0）** | FN（假負） | TN（真負） |

    - **TP**（True Positive）：實際是正類，模型也預測為正 → 預測正確
    - **TN**（True Negative）：實際是負類，模型也預測為負 → 預測正確
    - **FP**（False Positive）：實際是負類，但模型預測為正 → **誤報**
    - **FN**（False Negative）：實際是正類，但模型預測為負 → **漏報**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 分類報告（Classification Report）

    **定義：** 分類報告提供每個類別的四個指標。

    | 指標名稱 | 說明 |
    |----------|------|
    | **Precision**（精確率） | 預測為正類中，有多少是真的正類 |
    | **Recall**（召回率） | 真實正類中，有多少被正確預測 |
    | **F1-score** | Precision 與 Recall 的加權平均 |
    | **Support** | 該類別的真實樣本數 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 精確率 Precision

    $$
    \text{Precision} = \frac{TP}{TP + FP}
    $$

    **說明：**
    - 意思是「你預測為正類的資料中，有幾個是真的」
    - 若 FP 很多，Precision 就會低
    - **高精確率**：表示模型預測為正的樣本中，絕大多數都是對的。
    - 適用於「**不想誤判**」的場景，如：癌症篩檢（別隨便說人有病）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 召回率 Recall

    $$
    \text{Recall} = \frac{TP}{TP + FN}
    $$

    **說明：**
    - 意思是「所有真的正類中，有多少被模型正確預測」
    - 若 FN 很多，Recall 就會低
    - **高召回率**：表示模型能抓到幾乎所有真正的正類。
    - 適用於「**不能漏判**」的場景，如：垃圾郵件過濾、毒品快篩
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### F1 分數（F1-score）

    $$
    \text{F1-score} = 2 \times \frac{Precision \times Recall}{Precision + Recall}
    $$

    **說明：**
    - Precision 與 Recall 的加權調和平均值，綜合考量 **Precision 和 Recall 的平衡性**
    - 非常適合處理**不平衡資料**
    - 若 Precision 或 Recall 有一個非常低，F1 也會低
    - 適用於「**需要精確與完整兼顧**」的情境（**不想誤報也不想漏報**）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 實務評估指引

    | 建議指標 | 重點用途 | 應用時機 | 解釋 |
    |----------|----------|----------|------|
    | **Accuracy** | 整體準確率 | 類別分布均衡時可用 | 直觀簡單 |
    | **Recall**（召回率） | 實際正類被找出的比例 | 不想漏報時。應用於垃圾郵件偵測（防漏判） | 寧可誤報，不要漏報 |
    | **Precision**（精確率） | 預測為正時，對的機率有多高 | 不想誤報時。應用於醫療診斷（防誤報） | 寧可漏報，不要誤判 |
    | **F1-score** | 精確率與召回率的平衡 | Precision/Recall 落差大時。應用於整體考量 | 平衡 Precision 與 Recall |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 模型評估 – 迴歸問題
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ROC 曲線（Receiver Operating Characteristic）

    **主要應用於：** 二元分類問題

    **定義：** ROC 曲線是以：
    - **X 軸**：False Positive Rate（FPR）

    $$
    FPR = \frac{FP}{FP + TN}
    $$

    - **Y 軸**：True Positive Rate（Recall / TPR）

    $$
    TPR = \frac{TP}{TP + FN}
    $$

    - 畫出一條隨著閾值變化的曲線，衡量模型在不同預測閾值下的分類能力。

    #### AUC（Area Under Curve）

    - 曲線下的面積，數值在 **0.5 ～ 1.0** 之間
    - 越接近 **1** 表示**分類性能越好**
    - **0.5** 表示亂猜，沒有預測能力

    **適用情境：**
    - 類別不平衡時更能反映模型整體分類能力
    - 適合想了解模型「**整體預測分數表現**」的情境
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### PR 曲線（Precision-Recall Curve）

    **主要應用於：** **資料不平衡**的**二元分類**問題

    **定義：**
    - **X 軸**：Recall（召回率）
    - **Y 軸**：Precision（精確率）

    **特點：**
    - 比 ROC 更適合**正類極少數**、**不平衡資料**的問題
    - 可以觀察當你希望模型多找出正類時，會犧牲多少精確率

    #### PR-AUC
    - 與 ROC-AUC 相似，指**曲線下的面積**
    - 曲線越**靠近右上角**，表示**模型越好**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### R² 分數（決定係數 / R-squared）

    **主要應用於：** 迴歸問題

    **定義：** R² 衡量的是模型「**對資料變異量的解釋能力**」，即模型對資料解釋能力的比例，取值範圍：0, 1（理論可為負）。

    $$
    R^2 = 1 - \frac{RSS}{TSS}
    $$

    - **RSS**（Residual Sum of Squares）：殘差平方和，即預測誤差平方和
    - **TSS**（Total Sum of Squares）：總平方和，即實際資料的總變異

    **解讀方式：**
    - **R² = 1**：完美預測
    - **R² = 0**：模型毫無解釋能力
    - **R² < 0**：模型甚至比隨機亂猜還差
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### MSE（Mean Squared Error）

    **定義：** 平均平方誤差，**越小越好**

    $$
    \text{MSE} = \frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2
    $$

    - **用途**：對離群值敏感，懲罰大誤差
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### RMSE（Root Mean Squared Error）

    **定義：** MSE 的平方根，單位與原始目標變數相同

    $$
    \text{RMSE} = \sqrt{MSE}
    $$

    - **用途**：直觀衡量預測值與實際值的偏差程度
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### MAE（Mean Absolute Error）

    **定義：** 平均絕對誤差，不平方，因此對**離群值不敏感**

    $$
    \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
    $$

    - **用途**：比 RMSE 更穩健（對 outliers 的影響較小）
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 何時選哪一種指標

    | 問題特性 | 適合使用的指標 |
    |----------|----------------|
    | 類別平衡，模型整體準確 | Accuracy、F1-score |
    | 類別不平衡（如詐騙檢測） | Precision-Recall、PR-AUC |
    | 想了解整體預測能力 | ROC-AUC |
    | 預測數值（迴歸問題） | MSE、RMSE、MAE、R² |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 總結
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 「大數據資料分析」完整流程八大步驟

    ```
      (1) 載入資料   → (2) 確認資料 → (3) 預處理資料 → (4) 分割資料
    → (5) 選擇演算法 → (6) 訓練     → (7) 預估      → (8) 評估
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (1) 載入資料（Load Data）

    - **目標**：將資料來源（CSV、資料庫、API、JSON、網頁等）匯入程式中。
    - **常用工具**：`pandas.read_csv()`、SQL、爬蟲、資料庫連線等。
    - **重點**：
      - 確保資料來源可靠、格式正確。
      - 檢查編碼問題、遺漏值或異常值。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (2) 確認資料（Understand Data）

    - **目標**：初步理解資料結構、欄位意義與資料型態。
    - **常用工具**：`df.head()`、`df.info()`、`df.describe()`、`df.plot()` 等。
    - **重點**：
      - 了解各欄資料分布與單位。
      - 判斷目標變數（Label）與特徵（Features）。
      - 判別問題類型：分類、迴歸、群聚等。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (3) 預處理資料（Preprocess Data）

    - **目標**：將資料清理並轉換為機器學習可接受的格式。
    - **處理方式**：
      - 缺失值處理（補值、刪除）
      - 類別資料轉換（One-hot Encoding、Label Encoding）
      - 數值正規化（Normalization/Standardization）
      - 特徵選擇與轉換（PCA、特徵工程）
    - **重點**：
      - 資料乾淨是模型學習的基礎。
      - 對類別型、時間型、文字型資料特別注意。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (4) 分割資料（Split Data）

    - **目標**：將資料分為訓練集與測試集，以便訓練與驗證模型效能。
    - **常用方式**：`train_test_split()`（例如 80% 訓練 / 20% 測試）
    - **重點**：
      - 保證測試資料在訓練時不被洩漏。
      - 可以加入驗證集（Validation Set）或使用交叉驗證（Cross-Validation）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (5) 選擇演算法（Select Algorithm）

    根據問題類型選擇對應的 AI 演算法：

    | 問題類型     | 常用演算法                                            |
    | ------------ | ----------------------------------------------------- |
    | 分類         | Logistic Regression, SVM, Random Forest, XGBoost, CNN |
    | 迴歸         | Linear Regression, XGBoost Regressor, SVR             |
    | 時間序列預測 | ARIMA, LSTM                                           |
    | 關聯分析     | Apriori, FP-Growth                                    |
    | 分群         | K-Means, DBSCAN                                       |

    - **重點**：問題決定演算法；可比較多種演算法挑選效果最佳者。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (6) 訓練模型（Train Model）

    - **目標**：使用訓練集讓演算法學習輸入資料與目標資料的關係。
    - **範例語法**：`model.fit(X_train, y_train)`
    - **重點**：
      - 訓練過程會調整模型參數。
      - 可以使用「超參數調整」（Hyperparameter Tuning）提升效果（如 GridSearchCV）。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (7) 預估（Predict）

    - **目標**：讓訓練好的模型針對新資料做出預測。
    - **範例語法**：`model.predict(X_test)`
    - **重點**：
      - 確保輸入的資料格式與訓練時一致。
      - 可以套用在即時預測、推薦系統、商業應用中。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### (8) 評估模型（Evaluate Model）

    - **目標**：使用測試集評估模型的預測效果。
    - **常用指標**：

    | 任務類型 | 評估指標                             |
    | -------- | ------------------------------------ |
    | 分類     | Accuracy, Precision, Recall, F1, AUC |
    | 迴歸     | MSE, RMSE, MAE, R² Score             |
    | 分群     | Silhouette Score, Calinski-Harabasz  |

    - **重點**：
      - 選擇正確的評估指標依據任務。
      - 可視覺化混淆矩陣、ROC 曲線、預測 vs 實際圖。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 機器學習在大數據分析的應用與意義

    | 流程步驟          | 大數據應用重點                                             | 實際意義                                       |
    | ----------------- | ---------------------------------------------------------- | ---------------------------------------------- |
    | **1. 載入資料**   | 整合多源資料（IoT、社群媒體、感測器、ERP、網頁點擊）       | 支援數百 GB 至 TB 級資料存取，奠定資料治理基礎 |
    | **2. 確認資料**   | 快速掃描數據分布與異常、資料類型統計                       | 幫助了解資料的維度與品質、確認目標與特徵欄位   |
    | **3. 預處理資料** | 分散式清洗（如 Spark）、特徵工程自動化（如 Feature Store） | 提升資料一致性、準確性，是 AI 成敗的關鍵       |
    | **4. 分割資料**   | 進行大規模交叉驗證或即時切分（Real-time Splitting）        | 確保模型不過擬合，同時可處理線上學習或滾動預測 |
    | **5. 選擇演算法** | 根據任務與資料類型自動推薦最佳模型（AutoML, HPO）          | 提升模型開發效率與可擴展性                     |
    | **6. 模型訓練**   | 使用 GPU 或分散式架構訓練大型模型（如深度學習、XGBoost）   | 快速處理大量特徵與樣本，支持企業級應用         |
    | **7. 預估/推論**  | 即時預測（Real-time Inference）、批次推論（Batch Scoring） | 將模型成果轉為實際決策支援工具                 |
    | **8. 模型評估**   | 結合視覺化儀表板、持續監控模型表現（MLOps）                | 持續追蹤模型品質、實現可解釋性與信任度         |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 大數據與機器學習整合的核心意義

    | 重點面向                              | 說明                                           |
    | ------------------------------------- | ---------------------------------------------- |
    | **規模與速度**（Scale & Speed）       | 可處理海量資料，支援即時分析與預測             |
    | **自動化決策**（AI-driven Decisions） | 將模型嵌入業務流程中，提供預測性洞察           |
    | **模型可解釋性**（Explainability）    | 尤其在醫療、金融等領域，確保模型透明可信       |
    | **商業價值最大化**                    | 從資料中找出模式，改善流程、預測趨勢、降低風險 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 各領域的大數據 + 機器學習應用實例

    | 領域           | 應用場景                   | 解決問題               | 使用演算法                                         |
    | -------------- | -------------------------- | ---------------------- | -------------------------------------------------- |
    | **零售**       | 顧客購物行為預測、動態定價 | 增加銷售、減少庫存成本 | 分群（K-Means）、分類（RF、XGBoost）               |
    | **金融**       | 信用風險評估、詐欺偵測     | 降低壞帳與損失風險     | 分類（SVM、XGBoost）、異常檢測（Isolation Forest） |
    | **醫療**       | 疾病預測、醫療影像辨識     | 提高診斷準確度與效率   | CNN、分類、強化學習                                |
    | **製造**       | 預測性維護、良率分析       | 減少停機時間、提升品質 | 時間序列分析、分類、分群                           |
    | **智慧城市**   | 交通流量預測、能源管理     | 提升城市效率與永續發展 | LSTM、回歸、即時預測                               |
    | **物流供應鏈** | 需求預測、最佳路徑規劃     | 優化配送與存貨管理     | 時間序列、強化學習、回歸模型                       |
    | **教育科技**   | 學習成效預測、個人化推薦   | 提升學習效果與資源配置 | 分類、回歸、推薦系統                               |
    | **社群媒體**   | 情緒分析、熱門貼文預測     | 掌握趨勢與行銷策略     | NLP 模型（BERT）、分群、分類
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 應用 AI 解決不同問題的方式

    | 應用領域             | 問題類型 | 使用方法與說明                     |
    | -------------------- | -------- | ---------------------------------- |
    | **醫療診斷**         | 分類     | 預測是否患病（癌症判別、病症分型） |
    | **房價預測**         | 迴歸     | 根據面積、地段等預測房價           |
    | **銷售預測**         | 時間序列 | 根據歷史銷售資料預測未來銷售量     |
    | **市場分析**         | 分群     | 將顧客群分成不同類型（顧客細分）   |
    | **電商推薦**         | 關聯分析 | 根據消費者購物行為推薦其他商品     |
    | **客服問答系統**     | 自然語言 | 使用 NLP 模型進行語意理解與回覆    |
    | **智慧工廠品質檢測** | 分類     | 影像辨識缺陷產品                   |
    | **智慧交通預測**     | 時間序列 | 根據天氣與流量預測車流量           |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### AI × 大數據 = 資料價值的實現

    「機器學習 + 大數據技術」能夠：

    - 將資料轉為**可行動的決策依據**
    - 將 AI 從「理論研究」推向「商業實戰」
    - 協助企業與組織在競爭中贏得先機
    """)
    return


if __name__ == "__main__":
    app.run()
