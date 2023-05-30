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
    const average = json.average;

    $average.value = average;
    $average.classList.remove("passed", "failed");
    if (average >= 60) {
        $average.classList.add("passed");
    } else {
        $average.classList.add("failed");
    }
})
