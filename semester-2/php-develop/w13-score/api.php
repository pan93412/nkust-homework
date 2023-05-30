<?php

$input = file_get_contents('php://input');
/** @var int[] $data */
$data = json_decode($input);

$sum = array_sum($data) / count($data);
echo '{"average": '.$sum.'}';
