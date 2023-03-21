function initNumber() {
    const leftNumberInput = document.getElementById("left-number");
    const rightNumberInput = document.getElementById("right-number");

    const answer = document.getElementById("number-answer");

    function updateCalculation() {
        const left = +leftNumberInput.value;
        const right = +rightNumberInput.value;

        answer.innerText = left + right + "";
    }

    [leftNumberInput, rightNumberInput].forEach((element) => {
        element.oninput = updateCalculation;
    })

    window.addEventListener("load", updateCalculation);
}

export default initNumber;