from dataclasses import field, dataclass
from typing import Callable, Iterator


@dataclass()
class Tax:
    yr: int
    taxes: list[float] = field(default_factory=list)


class TaxManager:
    def __init__(self, subjects_order: list[str], data_getter: Callable[[str], float]):
        self.subjects_order = subjects_order
        self.data_source_getter = data_getter

    def record(self, user: Tax) -> None:
        for subject in self.subjects_order:
            user.taxes.append(self.data_source_getter(f"請輸入 {user.yr} 年的{subject}："))

    def record_all(self, users: list[Tax]) -> Iterator[None]:
        return map(self.record, users)


class TaxPrinter:
    subjects_order: list[str]

    def __init__(self, subjects_order: list[str]):
        self.subjects_order = subjects_order

    def format(self, taxes: list[Tax]) -> str:
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

printer = TaxPrinter(subjects_order)
result = printer.format(taxes)

print(result)
