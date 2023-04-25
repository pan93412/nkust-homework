<?php
//print_r($_POST);

$products = [
    "奶茶" => 30,
    "炸雞" => 35,
    "薯條" => 40,
];

$discount = 0.8;
?>

<!doctype html>
<html lang="zh-hant-tw">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>飲料訂購單</title>

    <script>
        /** @type {Record<string, string>} */
        const products = <?= json_encode($products) ?>;
    </script>
</head>
<body>
<form method="POST">
    <table>
        <thead>
        <tr>
            <th>品項</th>
            <th>價格</th>
            <th>數量</th>
        </tr>
        </thead>
        <tbody>
        <?php $index = 0 ?>
        <?php foreach ($products as $name => $price) { ?>
            <tr>
                <td>
                    <input type="text" name="name[]" value="<?= $_POST["name"][$index] ?? $name ?>" aria-label="品項">
                </td>
                <td>
                    <input type="number" name="price[]" value="<?= $_POST["price"][$index] ?? $price ?>"
                           aria-label="價格">
                </td>
                <td>
                    <select name="quantity[]" aria-label="數量">
                        <?php for ($i = 1; $i <= 10; $i++) { ?>
                            <option
                                value="<?= $i ?>" <?= $i === intval($_POST["quantity"][$index]) ? "selected" : "" ?>><?= $i ?></option>
                        <?php } ?>
                    </select>
                </td>
            </tr>

            <?php $index++ ?>
        <?php } ?>
        </tbody>
    </table>

    <button type="submit">計算</button>

    <label><input type="radio" name="member" <?= $_POST["member"] === "on" ? "checked" : "" ?>>會員</label>
    <label><input type="radio" name="member" <?= $_POST["member"] === "on" ? "checked" : "" ?>>非會員</label>
</form>

<?php if (count($_POST) > 0) { ?>
    <section>
    <pre>
<?php
echo "親愛的顧客，您點的是：\n";

$userInput = array_map(null, $_POST["name"], $_POST["price"], $_POST["quantity"]);
$totalPrice = 0;
$totalQuantity = 0;

foreach ($userInput as $idx => [$product, $unitPrice, $quantity]) {
    $price = $unitPrice * $quantity;

    echo "$product: $unitPrice * $quantity = $price\n";

    $totalPrice += $price;
    $totalQuantity += $quantity;
}

echo "\n";

$finalPrice = $totalPrice;

if ($_POST["member"] === "on") {
    $finalPrice *= $discount;
    echo "會員八折: $totalPrice * $discount = $finalPrice\n";
}
echo "總共 $totalQuantity 份，共計 $finalPrice 元。\n";
?>
    </pre>
    </section>

<?php } ?>
</body>
</html>
