/**
 * @typedef {import("./retrieve-data.js").Data} Data
 */

/**
 * @param {Data[]} columns
 * @param {(id: string) => void} onSelect
 * @return {HTMLElement}
 */
export function tbodyRender(columns, onSelect) {
    const $tbody = document.createElement('tbody');

    columns.forEach((column) => {
        const [$radioButton] = createRadioButton(column.id, 'selection');

        const $tr = document.createElement('tr');
        $tr.id = `--column-id-${column.id}`;

        const columns = [$radioButton, column.id, column.name, column.birth, column.addr];

        columns.forEach((column) => {
            const $td = document.createElement('td');

            if (typeof column === "string") {
                $td.appendChild(document.createTextNode(column));
            } else {
                $td.appendChild(column);
            }

            $tr.appendChild($td);
        });

        $radioButton.onchange = function () {
            onSelect(column.id);
        };

        $tbody.appendChild($tr);
    });

    return $tbody;
}

/**
 *
 * @param {string} id
 * @param {string} name
 * @return {[HTMLElement, string]} [input, input.id]
 */
function createRadioButton(id, name) {
    const $input = document.createElement('input');

    $input.type = 'radio';
    $input.name = name;
    $input.id = `--selection-${name}-${id}`;

    return [$input, $input.id];
}
