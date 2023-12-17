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
    ?>

    <table>
        <thead>
            <tr>
                <?php foreach (Contact::header() as $item): ?>
                    <th><?= $item ?></th>
                <?php endforeach; ?>
            </tr>
        </thead>
        <tbody>
            <?php try {
                foreach ($db->listAll(Contact::class) as $contact): ?>
                    <tr>
                        <?php foreach ($contact->toArray() as $item): ?>
                            <td><?= $item ?></td>
                        <?php endforeach; ?>
                    </tr>
                <?php endforeach;
            } catch (ReflectionException $e) {
                die($e->getMessage());
            } ?>
        </tbody>
    </table>
</body>
</html>