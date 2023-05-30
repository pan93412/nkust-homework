const $sumForm = document.getElementById("sum-form");
const $ans = document.getElementById("ans");

$sumForm.onsubmit = async function (e) {
    e.preventDefault();

    const response = await fetch("./api.php", {
        body: new FormData(this),
        method: "POST"
    });

    $ans.value = await response.json();
}
