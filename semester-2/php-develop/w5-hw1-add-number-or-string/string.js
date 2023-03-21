function initString() {
    const leftStringInput = document.getElementById("left-string");
    const rightStringInput = document.getElementById("right-string");

    const answer = document.getElementById("string-answer");

    function updateCalculation() {
        const left = leftStringInput.value;
        const right = rightStringInput.value;

        answer.innerText = left + right + "";
    }

    [leftStringInput, rightStringInput].forEach((element) => {
        element.oninput = updateCalculation;
    })

    window.addEventListener("load", updateCalculation);
}

export default initString;