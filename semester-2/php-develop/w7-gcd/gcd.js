//@ts-check

/**
 * GCD Algorithm in recursive.
 *
 * @param {number} x
 * @param {number} y
 * @returns {number}
 */
function gcd(x, y) {
  if (y === 0) return x;
  return gcd(y, x % y);
}

/**
 * GCD Algorithm in loop.
 *
 * @param {number} x
 * @param {number} y
 * @returns {number}
 */
function gcdLoop(x, y) {
  while (x != 0 && y != 0) {
    if (x >= y) {
      x %= y;
    } else {
      y %= x;
    }
  }

  return Math.max(x, y);
}

window.onload = () => {
  const $number1 = /** @type {HTMLInputElement?} */ (
    document.getElementById("number-1")
  );
  const $number2 = /** @type {HTMLInputElement?} */ (
    document.getElementById("number-2")
  );
  const $result = /** @type {HTMLInputElement?} */ (
    document.getElementById("result")
  );

  if (!$number1 || !$number2 || !$result)
    throw new Error("no #result in webpage");

  const writeResult = () => {
    $result.value = gcdLoop(+$number1.value, +$number2.value) + "";
  };

  for (const $element of [$number1, $number2]) {
    $element.oninput = writeResult;
  }

  debugger;
  writeResult();
};
