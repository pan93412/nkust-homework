/**
 * @typedef {{
 *     id: string,
 *     name: string,
 *     birth: string,
 *     addr: string,
 * }} Data
 */

/**
 * @returns {Promise<Data[] | null>}
 */
export async function retrieveData() {
    const response = await fetch("../do-retrieve.php", {
        cache: "no-cache",
    });
    if (!response.ok) {
        alert("爆炸了 💥🤯! See console for infos.");
        return null;
    }

    const json = await response.json();

    return json?.data;
}
