<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Contacts</title>
</head>
<body>
    <?php
    require_once "../lib/Contact.php";
    require_once "../lib/Database.php";
    $db = new Database("mycontacts");

    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        $dto = new ContactModelRequestDto($_POST);
        $db->insert($dto);
        header("Location: index.php");
    }
    ?>

    <form action="insert.php" method="post">
        <label for="name">名字</label>
        <input type="text" name="name" id="name">
        <label for="tel">電話</label>
        <input type="text" name="tel" id="tel">
        <input type="submit" value="新增">
    </form>
</body>
</html>