"""
One-line solution to Question 2, with numpy
"""

import numpy as np

print(
    # the __str__() of an ndarray renders a matrix to `[1 2 3]`.
    # by removing the first and last character, we will get `1 2 3`,
    # which is exactly what we want.

    #    vvvvvvvv -- Only for fulfilling the exercise requirement.
    str((arr1 := np.array(input().split(), dtype=int) + (arr2 := np.array(input().split(), dtype=int)) & 1))[1:-1]
    #                                      +~~~~~~~~~                 +--------------------------------^^^
    #                                      |                          +->  Basically = (a + b) % 2.
    #                                      |                               When the final bit is 1, it is odd.
    #                                      |
    #                                      |
    #                                      +-- defining `dtype` as `int` can improve the perf.
    #
)
