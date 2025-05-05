# SnowNLP 簡介

## 文字情緒分析

### 基於詞典的方法（Lexicon-based methods）

這類方法依賴預先定義的情緒詞典，透過比對文本中的詞語來判定情緒傾向。

- 特點
  - 不需大量標註資料。
  - 適合初期探索或小型資料集。
- 工具/詞典：
  - 中文：NTUSD（台灣大學情緒詞典）、HowNet、BosonNLP情緒詞典。
  - 英文：SentiWordNet、VADER（適合社群媒體語言）。
- 優缺點：
  - ✅ 解釋性高、易於實施。
  - ❌ 對語境與諷刺、否定詞處理較弱。

### 機器學習方法（Machine Learning-based methods）

這類方法依賴標註資料，使用傳統的分類演算法進行訓練。

- 常用模型
  - Naive Bayes
  - SVM（Support Vector Machine）
  - Logistic Regression
  - Random Forest
- 特點：
  - 需手動標註大量文本（正面/負面/中性）。
  - 依賴特徵抽取，如 TF-IDF、詞袋模型（Bag-of-Words, BoW）。
- 優缺點：
  - ✅ 效能佳，能捕捉更細緻的特徵。
  - ❌ 特徵工程繁瑣、需大量標註資料。

### 深度學習方法（Deep Learning-based methods）

這類方法使用深層神經網絡來自動學習特徵，對語意掌握較佳。

- 常見模型
  - RNN / LSTM / GRU（處理序列資料）
  - CNN（擷取局部語意特徵）
  - BERT / ERNIE（語境預訓練模型）
- 特點：
  - 可處理上下文語意、否定語句與隱喻。
  - 常搭配詞嵌入（Word Embedding），如 Word2Vec、GloVe、BERT embedding。
- 優缺點：
  - ✅ 效果優越，語境掌握能力強。
  - ❌ 訓練成本高、需大量資料與運算資源。

### 情緒多維度分析（Multidimensional sentiment analysis）

不僅辨識正負情緒，也進一步細分情緒種類。

- 情緒分類：
  - 快樂、憤怒、悲傷、恐懼、驚訝等（Plutchik 情緒輪）
- 實作方式：
  - 可透過多分類模型進行。

### 混合方法（Hybrid methods）

結合詞典與機器學習/深度學習，以彌補各自缺點。

## SnowNLP

- SnowNLP 是一種基於詞典法與機器學習混合技術的中文自然語言處理套件
- 它屬於偏向傳統機器學習方法，但內建了簡單的情緒分析模型與情緒詞典，可視為「輕量級機器學習 + 詞典法的工具」。
- 可以方便的處理中文文字內容

### 特點

| 項目 | 說明 |
|:-----|:------------|
| 📦 使用模型 | Naive Bayes 為主的機器學習模型 |
| 📚 訓練資料 | 內建中文情緒分類語料（可自訂重訓） |
| 💬 處理方式 | 對每段文本進行斷詞、特徵提取，並以模型預測正面（>0.5）或負面（<0.5）情緒 |
| ⚙ 可擴展性 | 支援自訂情緒語料以進行再訓練 |
| 💡 模型原理 | 採用 TF-IDF 特徵 + Naive Bayes 分類器 |

### 用法

```python
s = SnowNLP(句子)

# 情感分析
s.sentiments
# 分詞
s.words
# 分句
s.sentences
# 關鍵詞
s.keywords
# 提取文字摘要
s.summary
```
