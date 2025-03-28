import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    讀取 Excel 檔案並清理欄位名稱。

    Args:
        file_path (str): 檔案路徑。

    Returns:
        pd.DataFrame: 清理過的資料表。
    """
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()

    return df


def calculate_ratios(merged_data: pd.DataFrame) -> pd.DataFrame:
    """
    計算各項財務比率。

    Args:
        merged_data (pd.DataFrame): 合併後的資料表。

    Returns:
        pd.DataFrame: 含有各項比率的資料表。
    """
    # 計算變現力比率
    merged_data["流動比率"] = merged_data["流動資產"] / merged_data["流動負債"]
    merged_data["速動比率"] = (
        merged_data["流動資產"] - merged_data["存貨"] - merged_data["預付投資款"]
    ) / merged_data["流動負債"]

    # 計算負債管理比率
    merged_data["負債比率"] = merged_data["負債總額"] / merged_data["資產總額"]
    merged_data["利息保障倍數"] = merged_data["稅前息前淨利"] / merged_data["財務成本"]

    # 資產管理比率
    merged_data["存貨周轉率"] = merged_data["營業成本"] / merged_data["存貨"]
    merged_data["存貨周轉天數"] = 365 / merged_data["存貨周轉率"]
    merged_data["應收帳款周轉率"] = (
        merged_data["營業收入淨額"] / merged_data["應收帳款及票據"]
    )
    merged_data["平均收現期間"] = 365 / merged_data["應收帳款周轉率"]
    merged_data["應付帳款周轉率"] = (
        merged_data["營業成本"] / merged_data["應付帳款及票據"]
    )
    merged_data["應付帳款遞延支付期間"] = 365 / merged_data["應付帳款周轉率"]
    merged_data["總資產周轉率"] = merged_data["營業收入淨額"] / merged_data["資產總額"]

    # 獲利能力比率
    merged_data["純益率"] = (
        # 歸屬母公司淨利（損）：合併報表方之科目，指母公司股東所擁有之普通股東權益應分配之合併總損益。
        merged_data["歸屬母公司淨利（損）"] / merged_data["營業收入淨額"]
    )
    merged_data["股東權益報酬率 (ROE)"] = (
        # 母公司股東權益合計：係指合併股東權益中非屬少數股權之金額，其主要組成項目為股本、資本公積、
        # 保留盈餘（或累積虧損）及股東權益其他項目項目之金額減去庫藏股票面值。
        merged_data["歸屬母公司淨利（損）"] / merged_data["母公司股東權益合計"]
    )
    merged_data["總資產報酬率 (ROA)"] = (
        merged_data["歸屬母公司淨利（損）"] / merged_data["資產總額"]
    )

    # 市場價值比率
    merged_data["本益比"] = (
        merged_data["最高價(元)_年"] / merged_data["歸屬母公司淨利（損）"]
    )
    merged_data["股利殖利率"] = (
        merged_data["支付現金股利－CFF"] / merged_data["最高價(元)_年"]
    )
    merged_data["市價對帳面價值比"] = merged_data["最高價(元)_年"] / (
        merged_data["資產總額"] - merged_data["負債總額"]
    )

    return merged_data


def save_trend_plot(
    data: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    ylabel: str,
    trend_type: str,
):
    os.makedirs("charts", exist_ok=True)
    plt.figure(figsize=(10, 6))
    x = np.arange(len(data[x_column]))
    y = data[y_column]
    plt.plot(data[x_column], y, marker="o", linestyle="-", label=ylabel)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(data[x_column], p(x), "r--", label="趨勢線", linewidth=2)
    plt.title(f"{title} - {trend_type}")
    plt.xlabel("年/月")
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"charts/{ylabel}.png", dpi=300)
    plt.close()


def main() -> None:
    # set chinese font - pingfang hk
    plt.rcParams["font.family"] = "PingFang HK"

    # 讀取資料
    cash_flow = load_and_clean_data("data/現金流量表.xlsx")
    balance_sheet = load_and_clean_data("data/資產負債表.xlsx")
    income_statement = load_and_clean_data("data/綜合損益表.xlsx")
    stock_price = load_and_clean_data("data/調整股價.xlsx")

    # 合併資料
    merged_data = pd.merge(balance_sheet, income_statement, on="年/月", how="inner")
    merged_data = pd.merge(merged_data, cash_flow, on="年/月", how="inner")
    merged_data = pd.merge(
        merged_data, stock_price, left_on="年/月", right_on="年月", how="inner"
    )

    # 計算指標
    result_data = calculate_ratios(merged_data)

    # result by "年/月", ascending=True
    result_data = result_data.sort_values(by="年/月", ascending=True)

    result_data.to_excel("charts/raw_data.xlsx", index=False)

    # 所有指標列表
    indicators = [
        ("流動比率", "流動比率", "愈高愈好"),
        ("速動比率", "速動比率", "愈高愈好"),
        ("負債比率", "負債比率", "愈低愈好"),
        ("利息保障倍數", "利息保障倍數", "愈高愈好"),
        ("存貨周轉率", "存貨周轉率", "愈高愈好"),
        ("存貨周轉天數", "存貨周轉天數", "愈低愈好"),
        ("應收帳款周轉率", "應收帳款周轉率", "愈高愈好"),
        ("平均收現期間", "平均收現期間", "愈低愈好"),
        ("應付帳款周轉率", "應付帳款周轉率", "愈低愈好"),
        ("應付帳款遞延支付期間", "應付帳款遞延支付期間", "愈高愈好"),
        ("總資產周轉率", "總資產周轉率", "愈高愈好"),
        ("純益率", "純益率", "愈高愈好"),
        ("股東權益報酬率 (ROE)", "股東權益報酬率 (ROE)", "愈高愈好"),
        ("總資產報酬率 (ROA)", "總資產報酬率 (ROA)", "愈高愈好"),
        ("本益比", "本益比", "愈低愈好"),
        ("股利殖利率", "股利殖利率", "愈高愈好"),
        ("市價對帳面價值比", "市價對帳面價值比", "愈高愈好"),
    ]

    # 繪製所有指標的圖表
    for y_column, title, trend_type in indicators:
        save_trend_plot(result_data, "年/月", y_column, title, title, trend_type)

    print("所有圖表已成功儲存於 charts 資料夾中。")


if __name__ == "__main__":
    main()
