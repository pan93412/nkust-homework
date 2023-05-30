<?php

$a = intval($_POST["a"]);
$b = intval($_POST["b"]);

$sum = 0;
for ($n = $a; $n <= $b; $n++) {
    $sum += $n;
}

echo $sum;
