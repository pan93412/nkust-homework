# Q5 的數學邏輯解釋

**注意：加密和解密皆是以字元為單位 ('1' '2' '3' '4' '5' '6')**

令 $e$ 為加密函數

$$
e(r) = r \times 4 \mod 7
$$

用上面的式子用國小數學表示，就是：

$$
4r \div 7 = n \cdots c
$$

則解密函數 ($e'$) 為

$$
e'(c, n) = \frac {7 \times n + c}{4}
$$

考慮到題目只給我們只有 $c$，$n$ 必須暴力求出。

已知 $0 \leqslant r \leqslant 9$，因此 $n$ 的條件是：

$$
\begin{array}{ccccc}
    0 & \leqslant & \frac{7 n + c}{4} & \leqslant & 9\\
    0 & \leqslant & 7 n + c & \leqslant & 36 \\
    0 - c & \leqslant & 7 n & \leqslant & 36 - c
\end{array}
$$

考慮到 Python 不能很好的處理浮點數，我們做到這裡就好。
程式碼見 [basic.py](./basic.py)。
