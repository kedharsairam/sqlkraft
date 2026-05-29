import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://kedharsairam.github.io",
  base: "/sqlkraft",
  output: "static",
  build: {
    format: "directory",
  },
});
