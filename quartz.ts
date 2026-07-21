import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import WeeklyReport from "./quartz/components/WeeklyReport"
import { WeeklyLinks } from "./quartz/plugins/transformers/weeklyLinks"
import { QuartzPageTypePluginInstance } from "./quartz/plugins/types"

const weeklyReportPage: QuartzPageTypePluginInstance = {
  name: "WeeklyReportPage",
  priority: 100,
  match: ({ slug }) => slug.startsWith("weeklies/"),
  layout: "content",
  body: WeeklyReport,
}

const config = await loadQuartzConfig()

// Weekly reports retain their custom UI while using the Quartz 5 page-type dispatcher.
config.plugins.transformers.push(WeeklyLinks())
config.plugins.pageTypes ??= []
config.plugins.pageTypes.push(weeklyReportPage)

export default config
export const layout = await loadQuartzLayout()
