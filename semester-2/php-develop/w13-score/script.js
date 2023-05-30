const $scoreTable = document.getElementById("score-table");
const $average = document.getElementById("average");

$scoreTable.addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = new FormData($scoreTable);

    const scores = form.getAll("score").map(Number);
    const response = await fetch("./api.php", {
        method: "POST",
        body: JSON.stringify(scores),
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    });
    const json = await response.json();

    $average.value = json.average;
})
