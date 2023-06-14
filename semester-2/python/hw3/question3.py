"""
(Used to be an) One-line solution to Question 3
"""

import numpy as np

def add(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return np.add(A, B, dtype=int)

print(
    "\n".join(  # "{c1}\n{c2}\n{c3}"
        map(
            lambda col: " ".join(map(str, col)),  # "{e1} {e2} {e3}"
            add(  # add two matrics, basically = M_1 + M_2
                *(
                    np.array(
                        #     ------------------------- 3 columns (ideally)
                        [input().split(maxsplit=3) for _ in range(3)],  # 3 rows
                        dtype=int,  # integer only. no float.
                    )
                    for _ in range(2)  # we read two matrics
                ),
            ),
        )
    )
)
