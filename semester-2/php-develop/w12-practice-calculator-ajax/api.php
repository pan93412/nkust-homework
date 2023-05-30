<?php

$input = file_get_contents('php://input');
$data = json_decode($input);

$result = 0;
eval("\$result = {$data->left} {$data->op} {$data->right};");

echo json_encode([
    "ok" => true,
    "data" => $result
]);
