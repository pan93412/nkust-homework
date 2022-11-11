'''Question 2

Licensed under AGPL-3.0-only.'''

from typing import List

# The electric pricing table.
summer_pt =     [2.10, 3.02, 4.39, 4.97, 5.63]
not_summer_pt = [2.10, 2.68, 3.61, 4.01, 4.50]

# The higher bound of the pricing range.
pricing_range = [120, 330, 500, 700, None]

def separate(price: int, ranges: List[int]) -> List[int]:
    """Separate the price to ranges.

    Logic
    =====

    * If the price is higher than the ``higher_bound``,
      we write (higher_bound - lower_bound). Why do we
      minus 'lower_bound'? On the next step, we will
      ``sum()`` the values, and not minusing ``lower_bound``
      may introduce the duplicated calculation.
    * Otherwise, we write ``(price - lower_bound)``, a.k.a.
      the difference of ``price`` and ``lower_bound``.

    For example, we can separate ``525`` to four ranges:

            [120, 330, 500, ~700]

    And the final calculation is:

            [120, 210, 170, 25] with a padded 0.
    """
    answer = [0] * len(ranges)

    for idx, higher_bound in enumerate(ranges):
        lower_bound = ranges[idx - 1] if idx > 0 else 0
        if price is not None and price > higher_bound:
            answer[idx] = higher_bound - lower_bound
        else:
            answer[idx] = price - lower_bound
            break  # stop calculation

    return answer

def get_price(separated_value: List[int], pricing_table: List[float]) -> float:
    # Vector
    answer_table = pricing_table.copy()

    for idx, eleval in enumerate(separated_value):
        answer_table[idx] *= eleval

    return sum(answer_table)

def main():
    how_much_used = int(input("請輸入電費度數："))
    separated_value = separate(how_much_used, pricing_range)

    summer_price = get_price(separated_value, summer_pt)
    not_summer_price = get_price(separated_value, not_summer_pt)

    print(f"""\
夏月: {summer_price:.2f} 元
非夏月: {not_summer_price:.2f} 元
""")


if __name__ == "__main__":
    main()
else:
    raise RuntimeError("Unexpected environment.")
