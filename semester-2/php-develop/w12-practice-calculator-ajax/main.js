import {calculate} from './calculator.js';

const $result = document.getElementById("result");
if (!$result) throw new Error();

document.getElementById("calculator").onsubmit = async function (e) {
    e.preventDefault();
    const form = new FormData(this);

    $result.value = await calculate(
        Number(form.get("left")),
        form.get("op"),
        Number(form.get("right"))
    );
}
