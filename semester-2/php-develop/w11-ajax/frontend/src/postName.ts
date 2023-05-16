import axios from 'axios';

export default async function postName($el: HTMLInputElement, $resp: HTMLElement) {
    const text = $el.value;

    const params = new URLSearchParams();
    params.append("name", text);

    const response = await axios.post("./api.php", params);
    $resp.innerText = response.data;
}
