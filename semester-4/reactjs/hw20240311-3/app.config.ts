import { defineConfig } from "@solidjs/start/config";
import devtools from "solid-devtools/vite";
import UnoCSS from "unocss/vite";

export default defineConfig({
	vite: {
		plugins: [
			UnoCSS(),
			devtools({
				autoname: true,
			}),
		],
	},
});
