import { defineConfig } from "vite";
import UnoCSS from "unocss/vite";
import packageJson from "./package.json";
import Vue from "@vitejs/plugin-vue";

export default defineConfig({
  root: "./src",
  base: "./",
  build: {
    outDir: `../answers/${packageJson.name}`,
    target: ["chrome110", "edge110", "firefox110", "safari15", "es2021"],
    emptyOutDir: true,
    assetsDir: ".",
    sourcemap: true,
  },
  server: {
    port: 3000,
  },
  esbuild: {
    legalComments: "none",
  },
  plugins: [Vue(), UnoCSS()],
});
