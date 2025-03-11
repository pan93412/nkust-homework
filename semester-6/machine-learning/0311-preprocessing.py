# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "anthropic==0.49.0",
#     "marimo",
#     "matplotlib==3.10.1",
#     "numpy==2.2.3",
#     "pandas==2.2.3",
#     "plotly==6.0.0",
#     "polars[pandas]==1.24.0",
#     "scikit-learn==1.6.1",
#     "scipy==1.15.2",
#     "seaborn==0.13.2",
#     "ucimlrepo==0.0.7",
# ]
# ///

import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Homework 1: Preprocessing data""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Import data from UCI machine learning repository""")
    return


@app.cell
def _():
    from ucimlrepo import fetch_ucirepo
    import pandas as pd

    # fetch dataset
    mushroom = fetch_ucirepo(id=73)

    # data (as pandas dataframes)
    assert mushroom.data is not None
    assert isinstance(mushroom.data.features, pd.DataFrame)
    assert isinstance(mushroom.data.targets, pd.DataFrame)
    return fetch_ucirepo, mushroom, pd


@app.cell
def _(mushroom):
    X = mushroom.data.features
    y = mushroom.data.targets
    return X, y


@app.cell
def _(mo):
    mo.md("""## 缺失值處理 - missing values""")
    return


@app.cell
def _(X):
    # Check missing values

    X.isnull().sum()
    return


@app.cell
def _(y):
    y.isnull().sum()
    return


@app.cell
def _(mo):
    mo.md(r"""很明顯 stalk-root 有一個缺失值。查看缺失值相對於所有值的比例。""")
    return


@app.cell
def _(X):
    # 查看缺失值相對於所有值的比例
    X.isnull().sum().sum()/ X.shape[0]
    return


@app.cell
def _(mo):
    mo.md(r"""居然有 30%！要不就刪除這一個 column 好了 …""")
    return


@app.cell
def _(X):
    # drop 'stalk-root' column
    Xc = X.drop(columns=['stalk-root'])

    Xc.isnull().sum()
    return (Xc,)


@app.cell
def _(mo):
    mo.md(r"""Awesome!""")
    return


@app.cell
def _():
    ## 針對資料進行敘述統計
    return


@app.cell
def _():
    import plotly.express as px
    return (px,)


@app.cell
def _():
    ### 資料基本資訊
    return


@app.cell
def _(X):
    print("資料集大小：\t", X.shape)
    print("特徵數量：\t", X.shape[1])
    print("樣本數量：\t", X.shape[0])
    return


@app.cell
def _(mo):
    mo.md("""### 這份資料集中，有多少是有毒，有多少是無毒的？""")
    return


@app.cell
def _(px, y):
    px.histogram(y, x="poisonous", color="poisonous", title="Number of poisonous and edible mushrooms")
    return


@app.cell
def _(mo):
    mo.md("""### 各特徵的唯一值數量及其項目""")
    return


@app.cell
def _(Xc, pd):
    # 各特徵的唯一值數量及其項目
    for _col in Xc.columns:
        print(f"\n{_col}: {Xc[_col].nunique()} 個唯一值")
        print(Xc[_col].value_counts())

    # 建立一個包含每個特徵的唯一值數量和項目的DataFrame
    features_info = []
    for _col in Xc.columns:
        _unique_values = Xc[_col].unique().tolist()
        features_info.append({
            'feature': _col,
            'unique_count': Xc[_col].nunique(),
            'values': _unique_values
        })

    features_info_df = pd.DataFrame(features_info)
    features_info_df
    return features_info, features_info_df


@app.cell
def _(mo):
    mo.md("""### 各特徵的值分佈""")
    return


@app.cell
def _(Xc, mo, px):
    for _col in Xc.columns:
        _value_counts = Xc[_col].value_counts()
        mo.output.append(px.bar(_value_counts, title=f"{_col} value counts"))
    return


@app.cell
def _(mo):
    mo.md("""### Heatmap of Features""")
    return


@app.cell
def _(Xc):
    import plotly.express as px

    # Assuming Xc is a DataFrame
    fig = px.imshow(Xc, 
                    labels=dict(x="Columns", y="Rows", color="Values"),
                    color_continuous_scale="Viridis")

    fig.update_layout(
        title="Pivot Map of Xc",
        xaxis_title="Columns",
        yaxis_title="Rows"
    )

    fig.show()
    return fig, px


@app.cell
def _(Xc, mo, pd, y):
    def _():
        for col in Xc.columns[:5]:
            cross_tab = pd.crosstab(Xc[col], y['poisonous'], normalize='index') * 100
            mo.output.append(f"\n{col} 與毒性的關係 (百分比):")
            mo.output.append(cross_tab.round(2))


    _()
    return


@app.cell
def _(mo):
    mo.md(r"""## Label 分類數值""")
    return


@app.cell
def _(mo):
    mo.md(r"""### 針對 Binary 資料使用 label encoder""")
    return


@app.cell
def _(Xc, features_info_df):
    from sklearn.preprocessing import LabelEncoder

    Xc_encoded_part1 = Xc.copy()

    binary_features = features_info_df[features_info_df["unique_count"] <= 2]

    le = LabelEncoder()
    for col in binary_features["feature"]:
        Xc_encoded_part1[col] = le.fit_transform(Xc_encoded_part1[col])

    Xc_encoded_part1
    return LabelEncoder, Xc_encoded_part1, binary_features, col, le


@app.cell
def _():
    ### 針對 Non-binary 資料使用 one-hot encoder
    return


@app.cell
def _(Xc_encoded_part1, features_info_df, pd):
    onehot_features = features_info_df[features_info_df["unique_count"] > 2]

    Xc_encoded = pd.get_dummies(Xc_encoded_part1, columns=onehot_features["feature"], dtype='int64')

    Xc_encoded
    return Xc_encoded, onehot_features


@app.cell
def _(mo):
    mo.md(r"""## 切割資料集與訓練集""")
    return


@app.cell
def _(Xc_encoded, y):
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(Xc_encoded, y, test_size=0.2, random_state=42, stratify=y)

    X_train, X_test, y_train, y_test
    return X_test, X_train, train_test_split, y_test, y_train


@app.cell
def _(mo):
    mo.md(r"""### 資料分布""")
    return


@app.cell
def _(mo, px, y_test, y_train):
    mo.output.append(px.histogram(y_train, x="poisonous", color="poisonous", title="Number of poisonous and edible mushrooms in y_train"))
    mo.output.append(px.histogram(y_test, x="poisonous", color="poisonous", title="Number of poisonous and edible mushrooms in y_test"))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## 縮放特徵

        分別使用 StandardSca≤rStandardScaler 和 M∈MaxSca≤rMinMaxScaler 進行測試。
        """
    )
    return


@app.cell
def _(X_test, X_train):
    from sklearn.preprocessing import StandardScaler

    ss_scaler = StandardScaler()
    ss_scaler.set_output(transform="pandas")
    X_train_ss_scaled = ss_scaler.fit_transform(X_train)
    X_test_ss_scaled = ss_scaler.transform(X_test)

    X_train_ss_scaled, X_test_ss_scaled
    return StandardScaler, X_test_ss_scaled, X_train_ss_scaled, ss_scaler


@app.cell
def _(X_test, X_train):
    from sklearn.preprocessing import MinMaxScaler

    mm_scaler = MinMaxScaler()
    mm_scaler.set_output(transform="pandas")
    X_train_mm_scaled = mm_scaler.fit_transform(X_train)
    X_test_mm_scaled = mm_scaler.transform(X_test)

    X_train_mm_scaled, X_test_mm_scaled
    return MinMaxScaler, X_test_mm_scaled, X_train_mm_scaled, mm_scaler


@app.cell
def _():
    ## Experiments: Check the Random Forest accuracy with different scaling methods
    return


@app.cell
def _(
    X_test,
    X_test_mm_scaled,
    X_test_ss_scaled,
    X_train,
    X_train_mm_scaled,
    X_train_ss_scaled,
    y_test,
    y_train,
):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    import matplotlib.pyplot as plt
    import numpy as np

    # Convert target to 1D array for sklearn
    y_train_values = y_train['poisonous'].values
    y_test_values = y_test['poisonous'].values

    # Create and train models with different scaling methods
    # 1. No scaling
    rf_no_scaling = RandomForestClassifier(random_state=42)
    rf_no_scaling.fit(X_train, y_train_values)
    y_pred_no_scaling = rf_no_scaling.predict(X_test)
    accuracy_no_scaling = accuracy_score(y_test_values, y_pred_no_scaling)

    # 2. StandardScaler
    rf_ss = RandomForestClassifier(random_state=42)
    rf_ss.fit(X_train_ss_scaled, y_train_values)
    y_pred_ss = rf_ss.predict(X_test_ss_scaled)
    accuracy_ss = accuracy_score(y_test_values, y_pred_ss)

    # 3. MinMaxScaler
    rf_mm = RandomForestClassifier(random_state=42)
    rf_mm.fit(X_train_mm_scaled, y_train_values)
    y_pred_mm = rf_mm.predict(X_test_mm_scaled)
    accuracy_mm = accuracy_score(y_test_values, y_pred_mm)

    # Print results
    print("Random Forest with No Scaling:")
    print(f"Accuracy: {accuracy_no_scaling:.4f}")
    print(classification_report(y_test_values, y_pred_no_scaling))

    print("\nRandom Forest with StandardScaler:")
    print(f"Accuracy: {accuracy_ss:.4f}")
    print(classification_report(y_test_values, y_pred_ss))

    print("\nRandom Forest with MinMaxScaler:")
    print(f"Accuracy: {accuracy_mm:.4f}")
    print(classification_report(y_test_values, y_pred_mm))

    # Compare accuracies with a bar plot
    scaling_methods = ['No Scaling', 'StandardScaler', 'MinMaxScaler']
    accuracies = [accuracy_no_scaling, accuracy_ss, accuracy_mm]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(scaling_methods, accuracies, color=['blue', 'green', 'orange'])
    plt.ylim(0.9, 1.01)  # Adjust y-axis to better see differences
    plt.title('Random Forest Accuracy with Different Scaling Methods')
    plt.ylabel('Accuracy')

    # Add accuracy values on top of bars
    for bar, acc in zip(bars, accuracies):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001, 
                 f'{acc:.4f}', ha='center', va='bottom')

    plt.gca()
    return (
        RandomForestClassifier,
        acc,
        accuracies,
        accuracy_mm,
        accuracy_no_scaling,
        accuracy_score,
        accuracy_ss,
        bar,
        bars,
        classification_report,
        confusion_matrix,
        np,
        plt,
        rf_mm,
        rf_no_scaling,
        rf_ss,
        scaling_methods,
        y_pred_mm,
        y_pred_no_scaling,
        y_pred_ss,
        y_test_values,
        y_train_values,
    )


if __name__ == "__main__":
    app.run()
