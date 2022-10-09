from dataclasses import dataclass


@dataclass()
class Tax:
    yr: int
    income: float
    business: float
    stock: float


tax_list = [
    Tax(2017, 98.34, 90.20, 104.79),
    Tax(2016, 83.00, 110.50, 82.45),
    Tax(2015, 98.00, 79.32, 102.00)
]

print(f"年度  所得稅  營業稅  證交稅")
for tax in tax_list:
    # 考慮到一個中文字佔 2 個數字字元，
    # 因此這裡的 align specifier 是有根據
    # 中英欄位進行調整的。
    print((
        f"{tax.yr}  "
        f"{tax.income:>6.2f}  "
        f"{tax.business:>6.2f}  "
        f"{tax.stock:>6.2f}"
    ))
