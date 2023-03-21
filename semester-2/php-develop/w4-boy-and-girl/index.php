<?php
$alertButtons = [
    [
        "id" => "man",
        "message" => "I'm a man!",
    ], [
        "id" => "woman",
        "message" => "I'm a woman!",
    ],
]
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Document</title>

    <script>
        window.onload = function() {
            document.querySelectorAll(".alert-button").forEach((b) => {
                b.addEventListener("click", () => {
                    alert(b.dataset.alert);
                });
            });
        }
    </script>
</head>
<body>

<div class="container">
    <?php
        foreach ($alertButtons as $btn) {
    ?>
        <button class="alert-button" id="<?= "{$btn["id"]}-button" ?>" data-alert="<?= $btn["message"] ?>">
            <img src="<?= "./assets/{$btn["id"]}.png" ?>" alt="<?= ucwords($btn["id"]) ?>" />
        </button>
    <?php
        }
    ?>
</div>
</body>
</html>
