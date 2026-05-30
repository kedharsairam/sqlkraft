import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://kedharsairam.github.io",
  base: "/sqlkraft",
  output: "static",
  prefetch: {
    prefetchAll: true,
    defaultStrategy: "hover",
  },
  build: {
    format: "directory",
  },
  integrations: [
    sitemap({
      // Exclude trash directory pages from sitemap
      filter: (page) => !page.includes("/trash/"),
      // Customize the changefreq and priority
      changefreq: "weekly",
      priority: 0.7,
      lastmod: new Date(),
    }),
  ],
});
