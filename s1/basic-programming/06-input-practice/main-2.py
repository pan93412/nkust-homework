from dataclasses import field, dataclass
from typing import Callable, Iterator


@dataclass()
class Tax:
    yr: int
    taxes: list[float] = field(default_factory=list)


class TaxManager:
    def __init__(self, subjects_order: list[str], data_getter: Callable[[str], float]):
        """初始化 TaxManager。

        Args:
            subjects_order (list[str]): 稅務科目的順序。
            data_getter (Callable[[str], float]): 資料來源的取得。傳入之 str 為提示訊息。
        """
        self.subjects_order = subjects_order
        self.data_source_getter = data_getter

    def record(self, tax: Tax) -> None:
        """將資料根據 ``subjects_order`` 順序
        錄入 ``tax`` 的 ``taxes`` 屬性。

        Args:
            tax (Tax): 要錄入的稅務結構體。
        """
        for subject in self.subjects_order:
            tax.taxes.append(self.data_source_getter(f"請輸入 {tax.yr} 年的{subject}："))

    def record_all(self, taxes: list[Tax]) -> Iterator[None]:
        """將資料錄入 ``taxes`` 中的所有 ``Tax``。

        見 ``record()``。

        Args:
            taxes (list[Tax]): 所有要錄入的稅務結構體。

        Yields:
            None: 回傳順序為錄入順序。
        """
        return map(self.record, taxes)


class TaxFormatter:
    subjects_order: list[str]

    def __init__(self, subjects_order: list[str]):
        """初始化 TaxFormatter。

        Args:
            subjects_order (list[str]): 科目順序。
        """
        self.subjects_order = subjects_order

    def format(self, taxes: list[Tax]) -> str:
        """將稅務資料格式化成字串。

        Args:
            taxes (list[Tax]): 稅務資料。
        """
        output_buffer: list[list[str]] = [["年度"] + self.subjects_order]

        for tax in taxes:
            tax_buffer: list[str] = [str(tax.yr)]

            for tax in tax.taxes:
                tax_buffer.append(f"{tax:>6.2f}")

            output_buffer.append(tax_buffer)

        return "\n".join(map(lambda to_tab_buf: "  ".join(to_tab_buf), output_buffer))


subjects_order = ["所得稅", "營業稅", "證交稅"]
taxes = list(map(Tax, [2017, 2016, 2015]))

recorder = TaxManager(subjects_order, lambda p: float(input(p)))
list(recorder.record_all(taxes))

printer = TaxFormatter(subjects_order)
result = printer.format(taxes)

print(result)
