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
    <title>List types</title>
</head>
<body>
    <?php
    try {
        $meta = $db->getMetadata(Student::class);
    } catch (ReflectionException $e) {
        die($e->getMessage());
    }
    ?>

    <ul>
        <li>資料表：<?= $meta->database ?></li>
        <li>欄位數：<?= $meta->fieldNums ?> 個</li>
        <li>記錄數：<?= $meta->recordNums ?> 個</li>
    </ul>

    <table>
        <thead>
            <tr>
                <th>欄位名稱</th>
                <th>資料表</th>
                <th>最大長度</th>
                <th>資料類型</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($meta->fieldMeta as $meta): ?>
                <tr>
                    <td><?= $meta->name ?></td>
                    <td><?= $meta->table ?></td>
                    <td><?= $meta->maxLength ?></td>
                    <td><?= $meta->type ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

</body>
</html>