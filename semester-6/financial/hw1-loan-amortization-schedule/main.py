from datetime import datetime
from calculate import calculate_loan_amortization
from structure import LoanConfig


if __name__ == "__main__":
    # 範例使用
    config = LoanConfig(
        principal=7_000_000,
        periods=240,
        annual_rate=0.03,
        start_date=datetime(2024, 4, 1)
    )

    print(repr(config))
    
    df = calculate_loan_amortization(config)
    df.write_excel("loan_amortization.xlsx")
