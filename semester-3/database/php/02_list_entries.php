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
    <title>List entries</title>
</head>
<body>
    <?php
    try {
        $response = $db->listAll(Student::class);
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

            <?php foreach ($response as $value): ?>
                <tr>
                    <?php foreach ($value->toArray() as $item): ?>
                        <td><?= $item ?></td>
                    <?php endforeach; ?>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

</body>
</html>