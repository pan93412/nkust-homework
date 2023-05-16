import {startPage} from "./startPage.ts";
import postName from "./postName.ts";

document.querySelector<HTMLDivElement>('#app')!.innerHTML = startPage;

const $name = document.querySelector<HTMLInputElement>("#name");
const $response = document.querySelector<HTMLInputElement>(".response");
if (!$name || !$response) throw new Error("$name or $response not found");
$name.oninput = () => postName($name, $response);
