<?php

function gcd(int $a, int $b): int {
    while ($b != 0) {
        $t = $b;
        $b = $a % $b;
        $a = $t;
    }

    return $a;
}

$a = intval($_POST["a"]);
$b = intval($_POST["b"]);

echo gcd($a, $b);
