'''Question 1

Licensed under AGPL-3.0-only.'''

def bmi_calc(weight: float, height: float) -> float:
    return weight / (height**2)

def cals_calc(weight: float, height: float, activity: str) -> float:
    bmi = bmi_calc(weight, height)

    # Too fat: [24, 27) U [27, 30) U [30, 35) U [35,] -> [24, ]
    # Medium: [18.5, 24)
    # Too thin: (,18.5)
    if activity == "1":
        return 25 * weight   if bmi >= 24 else \
               30 * weight   if 24 > bmi >= 18.5 else \
               35 * weight # if 18.5 > bmi
    elif activity == "2":
        return 30 * weight   if bmi >= 24 else \
               35 * weight   if 24 > bmi >= 18.5 else \
               40 * weight # if 18.5 > bmi
    elif activity == "3":
        return 35 * weight   if bmi >= 24 else \
               40 * weight   if 24 > bmi >= 18.5 else \
               45 * weight # if 18.5 > bmi
    else:
        raise ValueError(f"Unexpected activity value ({activity})")

def main():
    activity = input("輸入每天活動量 (1: 輕度, 2: 中度, 3: 重度): ")
    height = float(input("輸入身高 (公尺): "))
    weight = float(input("輸入體重 (公斤): "))

    print(f"BMI 為 {bmi_calc(weight, height):.2f}")
    print(f"每日所需的熱量 {cals_calc(weight, height, activity):.2f}")

if __name__ == "__main__":
    main()
else:
    raise RuntimeError("Unexpected environment.")
