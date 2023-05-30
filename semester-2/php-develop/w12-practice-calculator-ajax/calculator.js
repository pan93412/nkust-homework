/**
 *
 * @param {number} left
 * @param {"+"|"-"|"*"|"/"} op
 * @param {number} right
 */
export async function calculate(left, op, right) {
    const payload = {
        left, op, right,
    }

    const response = await fetch('./api.php', {
        body: JSON.stringify(payload),
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    });

    const data = await response.json();
    if (data.ok) {
        return data.data;
    }

    throw new Error();
}
