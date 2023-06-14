<?php

use Client\CustomPdo;

require_once 'sql.php';

$client = new CustomPdo();

header("Content-Type: application/json; charset=UTF-8");

try {
    $id = $_POST["id"] ?? throw new ValueError("`id` required");
    $name = $_POST["name"] ?? throw new ValueError("`name` required");
    $birth = $_POST["birth"] ?? throw new ValueError("`birth` required");
    $addr = $_POST["addr"] ?? throw new ValueError("`addr` required");

    $client->createStudent($id, $name, $birth, $addr);
    http_response_code(200);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode([
        "type" => "PDO_EXCEPTION",
        "error" => $e->getMessage(),
    ]);
} catch (ValueError $e) {
    http_response_code(400);
    echo json_encode([
        "type" => "VALUE_ERROR",
        "error" => $e->getMessage(),
    ]);
}
