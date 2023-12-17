<?php
require_once "lib/Database.php";
$db = new Database();
?>

<!doctype html>
<html lang="zh-hant-tw">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Show info</title>
</head>
<body>
    <h1>Database Information</h1>
    <table>
        <thead>
            <tr>
                <th>項目</th>
                <th>資訊</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($db->info() as $key => $value): ?>
                <tr>
                    <td><?= $key ?></td>
                    <td><?= $value ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

</body>
</html>