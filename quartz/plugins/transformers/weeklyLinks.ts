import { QuartzTransformerPlugin } from "../types"
import { visit } from "unist-util-visit"

export const WeeklyLinks: QuartzTransformerPlugin = () => {
  return {
    name: "WeeklyLinks",
    htmlPlugins() {
      return [
        () => {
          return (tree, file) => {
            // Only process files in weeklies folder
            if (!file.data.slug?.startsWith("weeklies/")) return

            visit(tree, "element", (node) => {
              if (
                node.tagName === "a" &&
                node.properties &&
                typeof node.properties.href === "string"
              ) {
                const href = node.properties.href as string
                const classes = node.properties.className as string[] | undefined

                // Check if CrawlLinks already marked this as internal
                const isInternalClass = classes?.includes("internal")

                // Classify link type based on URL pattern and class
                if (href.includes("github.com")) {
                  node.properties["data-link-type"] = "github"

                  // Further classify GitHub links
                  if (href.includes("/pull/")) {
                    node.properties["data-github-type"] = "pr"
                  } else if (href.includes("/issues/")) {
                    node.properties["data-github-type"] = "issue"
                  } else if (href.includes("/commit/")) {
                    node.properties["data-github-type"] = "commit"
                  } else {
                    node.properties["data-github-type"] = "repo"
                  }
                } else if (
                  isInternalClass ||
                  href.startsWith("/") ||
                  href.startsWith("#") ||
                  href.startsWith("../") ||
                  href.includes("roadmap.vac.dev")
                ) {
                  node.properties["data-link-type"] = "internal"
                } else {
                  node.properties["data-link-type"] = "external"
                }
              }
            })
          }
        },
      ]
    },
  }
}
