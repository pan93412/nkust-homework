//@ts-check

((_author) => {
    /**
     * @param {string} text
     * @returns {void}
     */
    function updatePromptText(text) {
        document.getElementById("prompt").innerHTML = text;
    }

    function registerControls() {
        for (const $el of document.querySelectorAll(".controls > *")) {
            switch ($el.textContent) {
                case 'Homepage':
                    $el.addEventListener("click", () => {
                        updatePromptText("<a href='https://pan93.com'>click me</a>")
                    });
                    break;
                case 'Expertise':
                    $el.addEventListener("click", () => {
                        alert("coding, l10n, design, ???")
                    });
                    break;
                case 'Click me':
                    $el.addEventListener("click", () => {
                        location.href = 'https://link.pan93.com/resume';
                    });
                    break;
            }
        }
    }

    registerControls();
})("yi-jyun pan");
