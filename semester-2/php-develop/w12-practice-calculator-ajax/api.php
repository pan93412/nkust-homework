<?php

class DecodedResult {
    public int $left;
    public string $op;
    public int $right;
}

$input = file_get_contents('php://input');
/** @var DecodedResult $data */
$data = json_decode($input);

$result = 0;
eval("\$result = $data->left $data->op $data->right;"); // hacky!

echo json_encode([
    "ok" => true,
    "data" => $result
]);
