<?php
    function bmi(int $w, int $h): int|float {
        // bmi = weightKg / (heightCm / 100)^2
        return $w / (($h / 100) ** 2);
    }
?>

<!doctype html>
<html lang="zh-hant-tw">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>BMI Calculator</title>
</head>
<body>
    <main>
        <form method="POST">
            <?php
                $height = intval($_POST["height"]);
                $weight = intval($_POST["weight"]);
            ?>

            <div>
                <label for="height">身高</label>
                <input type="number" id="height" name="height" placeholder="CM">
            </div>

            <div>
                <label for="weight">體重</label>
                <input type="number" id="weight" name="weight" placeholder="KG">
            </div>

            <button type="submit">計算</button>
            <?php
                if ($height && $weight) {
                    $bmi = bmi($weight /* kg */, $height /* cm */);
                    echo "<div>BMI: $bmi</div>";
                }
            ?>
        </form>

    </main>
</body>
</html>