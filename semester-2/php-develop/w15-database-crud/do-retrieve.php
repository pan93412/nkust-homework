<?php

require_once 'sql.php';

use Client\CustomPdo;
$client = new CustomPdo();

header("Content-Type: application/json; charset=UTF-8");

try {
    $motherfuckers = $client->retrieveAllRows();

    if (count($motherfuckers) == 0) {
        http_response_code(404);
        echo '{"status": "No rows available."}';
        return;
    }

    http_response_code(200);
    echo json_encode([
        "status" => "excellent!",
        "data" => $motherfuckers,
    ]);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode([
        "status" => "my server 爆炸. Details: $e"
    ]);
}
