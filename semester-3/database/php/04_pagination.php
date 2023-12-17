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
    <title>Pagination</title>
</head>
<body>
    <?php
    $page = $_GET["page"] ?? 1;
    $limit = $_GET["limit"] ?? 1;

    if ($page < 1) $page = 1;

    try {
        $entries = $db->getEntriesByPage(Student::class, $page, $limit);
    } catch (ReflectionException $e) {
        die($e->getMessage());
    }
    ?>

    <table>
        <thead>
        <tr>
            <?php foreach(Student::header() as $header): ?>
                <th><?= $header ?></th>
            <?php endforeach; ?>
        </tr>
        </thead>
        <tbody>

        <?php foreach ($entries as $value): ?>
            <tr>
                <?php foreach ($value->toArray() as $item): ?>
                    <td><?= $item ?></td>
                <?php endforeach; ?>
            </tr>
        <?php endforeach; ?>
        </tbody>
    </table>

    <ul style="
        display: inline;
        list-style: none;
        ">
        <li>
            <a href="?page=<?= $page - 1 ?>&limit=<?= $limit ?>">上一頁</a>
        </li>
        <?php for ($i = $page - 2; $i < $page + 2; $i++): ?>
            <?php if ($i < 1) continue; ?>
            <li>
                <a href="?page=<?= $i ?>&limit=<?= $limit ?>"><?= $i ?></a>
            </li>
        <?php endfor; ?>
        <li>
            <a href="?page=<?= $page + 1 ?>&limit=<?= $limit ?>">下一頁</a>
        </li>
    </ul>
</body>
</html>