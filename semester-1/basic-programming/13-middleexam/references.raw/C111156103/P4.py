'''Question 4

Licensed under AGPL-3.0-only.'''

from typing import Iterable

RI = float

# Strings
s_perfect   =   "心肺功能優異"
s_normal    =   "心肺功能一般"
s_notenough =   "心肺功能不足"
s_notgood   =   "心肺功能不良"
s_urgent    =   "立即就醫評估"

def get_ruffier_indicator(p_values: Iterable[float]) -> RI:
    """Get the ``RI`` value according to the ``p_values``.

    The ``p_values`` should include 3 values: [P1, P2, P3]."""

    return (sum(p_values) - 200) / 10

def get_status_from_ri(age: int, ri: RI) -> str:
    """
    Get human-readable status text from the RI value.

    Exception
    =========
    Raise ValueError when ``age`` is lower than 18.
    """
    if age < 18: raise ValueError("The age is out of the expected range.")
    elif 18 <= age < 40:
        return  s_perfect   if 0 <= ri <= 5 else \
                s_normal    if 5 < ri <= 10 else \
                s_notenough if 10 < ri <= 15 else \
                s_notgood   if 15 < ri <= 20 else \
                s_urgent
    else: # age <= 40
        return  s_perfect   if 0 <= ri <= 5 else \
                s_perfect   if 5 < ri <= 10 else \
                s_normal    if 10 < ri <= 15 else \
                s_notenough if 15 < ri <= 20 else \
                s_urgent

def main():
    age = int(input("輸入受試者年紀："))
    p_values = map(lambda idx: float(input(f"輸入 P{idx}：")), range(1, 4))

    ri = get_ruffier_indicator(p_values)

    print(f"RI 為 {ri}")
    print(get_status_from_ri(age, ri))

if __name__ == "__main__":
    main()
else:
    raise RuntimeError("Unexpected environment.")
