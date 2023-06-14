/**
 * @param {FormData} formData
 * @returns {Promise<null>}
 * @throws {Error}
 */
export async function createData(formData) {
    const response = await fetch("../do-create.php", {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        throw new Error("爆炸了 💥🤯! See console for infos.");
    }

    return null;
}

/**
 * @param {() => void | Promise<void>} onDataUpdated
 */
export function addInsertionLine(onDataUpdated) {
    const $tbody = document.querySelector("#information-table > tbody");

    const $tr = document.createElement("tr");
    /** @type {Map<string, HTMLElement>} */
    const columnValue = ["id", "name", "birth", "addr"].reduce((map, val) => {
        const $td = document.createElement("td");
        const $input = document.createElement("input");

        $input.type = "text";
        $input.name = val;

        $td.appendChild($input);
        map.set(val, $td);
        
        return map;
    }, new Map());

    const $confirm = document.createElement("button");
    $confirm.innerText = "確認";

    $tr.appendChild((() => {
        const $td = document.createElement("td");

        $td.appendChild($confirm);
        return $td;
    })());

    for (const [_, $el] of columnValue) {
        $tr.appendChild($el);
    }

    $confirm.onclick = async function () {
        try {
            const formData = new FormData();

            for (const [key, $el] of columnValue) {
                formData.append(key, $el.querySelector("input").value);
            }

            await createData(formData);
        } catch (e) {
            alert(e.message);
            return;
        }

        alert("Inserted!");
        await onDataUpdated();
    }

    $tbody.appendChild($tr);
}