<?php

require_once 'Rectangle.php';

$rectangle = new Rectangle(4, 4);
echo $rectangle . PHP_EOL;

for ($i = 10; $i <= 20; $i++) {
    for ($j = 10; $j <= 20; $j++) {
        $rectangle->setWidth($i);
        $rectangle->setHeight($j);

        echo $rectangle . PHP_EOL;
    }
}
