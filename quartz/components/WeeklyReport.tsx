import { htmlToJsx } from "../util/jsx"
import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import weeklyReportStyle from "./styles/weeklyReport.scss"

// @ts-ignore
import script from "./scripts/weeklyReport.inline"

function WeeklyReport({ fileData, tree }: QuartzComponentProps) {
  const content = htmlToJsx(fileData.filePath!, tree)

  // Check if this is a weekly report page
  const isWeekly = fileData.slug?.startsWith("weeklies/")

  if (!isWeekly) {
    // Fall back to standard content rendering for non-weekly pages
    return <article class="popover-hint">{content}</article>
  }

  // Team definitions with colors
  const teams = [
    { id: "bi", name: "BI", fullName: "Business Intelligence", color: "#f0883e" },
    { id: "dst", name: "DST", fullName: "Distributed Systems Testing", color: "#a371f7" },
    { id: "nim", name: "Nim", fullName: "Language & Libraries", color: "#58a6ff" },
    { id: "p2p", name: "P2P", fullName: "Peer-to-Peer", color: "#3fb950" },
    { id: "qa", name: "QA", fullName: "Quality Assurance", color: "#f85149" },
    { id: "rfc", name: "RFC", fullName: "Request for Comments", color: "#db61a2" },
    { id: "sc", name: "SC", fullName: "Smart Contracts", color: "#d29922" },
    { id: "sec", name: "SEC", fullName: "Security", color: "#ff7b72" },
    { id: "tke", name: "TKE", fullName: "Token Economics", color: "#79c0ff" },
    { id: "web", name: "WEB", fullName: "Web Development", color: "#7ee787" },
    { id: "infra", name: "INFRA", fullName: "Infrastructure", color: "#9da5ff" },
  ]

  return (
    <div class="weekly-report">
      {/* Stats bar */}
      <div class="weekly-stats-bar">
        <div class="stat">
          <div class="stat-value" id="stat-teams">
            0
          </div>
          <div class="stat-label">Teams</div>
        </div>
        <div class="stat">
          <div class="stat-value" id="stat-prs">
            0
          </div>
          <div class="stat-label">GitHub Links</div>
        </div>
      </div>

      {/* Controls */}
      <div class="weekly-controls">
        <input
          type="text"
          class="weekly-search"
          id="weekly-search"
          placeholder="Search updates, PRs, teams..."
        />
        <div class="weekly-filters">
          <button class="filter-btn active" data-filter="all">
            All
          </button>
          <button class="filter-btn" data-filter="github">
            GitHub
          </button>
          <button class="filter-btn" data-filter="internal">
            Internal
          </button>
          <button class="filter-btn" data-filter="external">
            External
          </button>
        </div>
      </div>

      {/* Link legend */}
      <div class="weekly-legend">
        <span class="legend-title">Link Types:</span>
        <span class="legend-item">
          <span class="legend-color github"></span>
          <span>GitHub</span>
        </span>
        <span class="legend-item">
          <span class="legend-color internal"></span>
          <span>Internal (roadmap.vac.dev)</span>
        </span>
        <span class="legend-item">
          <span class="legend-color external"></span>
          <span>External</span>
        </span>
        <span class="legend-item">
          <span class="legend-color task-id"></span>
          <span>Task ID</span>
        </span>
      </div>

      {/* Team tabs navigation */}
      <div class="weekly-tabs" id="weekly-tabs">
        <button class="team-tab active" data-team="all">
          All Teams
        </button>
        {teams.map((team) => (
          <button class="team-tab" data-team={team.id} title={team.fullName}>
            {team.name}
            <span class="tab-badge" id={`badge-${team.id}`}>
              0
            </span>
          </button>
        ))}
      </div>

      {/* Content with popover-hint for Quartz popovers */}
      <article class="popover-hint weekly-content show-all" id="weekly-content">
        {content}
      </article>

      {/* No results message (hidden by default) */}
      <div class="weekly-no-results" id="weekly-no-results" style={{ display: "none" }}>
        <h4>No results found</h4>
        <p>Try adjusting your search or filter criteria.</p>
      </div>
    </div>
  )
}

WeeklyReport.css = weeklyReportStyle
WeeklyReport.afterDOMLoaded = script

export default (() => WeeklyReport) satisfies QuartzComponentConstructor
