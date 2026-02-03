// Weekly Report Interactive Script
// Handles tabs, search, filtering, team section management, and highlights

// State
let currentFilter = "all"
let currentTeam = "all"
let teamHighlights: Record<string, string[]> = {}

// Team mappings based on h3 header IDs (as rendered by Quartz)
// IDs are like "ift-tsbi", "ift-tsdst", etc. (colons removed)
const teamIdPatterns: Record<string, RegExp> = {
  bi: /ift-ts.?bi|ifs-ts.?bi/i,
  dst: /ift-ts.?dst/i,
  nim: /ift-ts.?nim/i,
  p2p: /ift-ts.?p2p/i,
  qa: /ift-ts.?qa|vac.?qa/i,
  rfc: /ift-ts.?rfc/i,
  sc: /ift-ts.?sc/i,
  sec: /ift-ts.?sec/i,
  tke: /ift-ts.?tke|vac.?tke/i,
  web: /ift-ts.?web|vac.?web/i,
}

function setupWeeklyReport() {
  const weeklyReport = document.querySelector(".weekly-report")
  if (!weeklyReport) return

  // Reset state on navigation
  currentFilter = "all"
  currentTeam = "all"
  teamHighlights = {}

  // Initialize in order
  extractTeamHighlights()
  wrapTeamSections()
  hideOriginalHighlightsSection()
  updateStats()
  updateTeamBadges()
  setupTabs()
  setupSearch()
  setupFilters()
  setupExpandableHeaders()
}

function extractTeamHighlights() {
  const content = document.getElementById("weekly-content")
  if (!content) return

  // Find the "team highlights" section
  const teamHighlightsHeader = content.querySelector("h3#team-highlights")
  if (!teamHighlightsHeader) return

  // Get the ul that follows the team highlights header
  let sibling = teamHighlightsHeader.nextElementSibling
  while (sibling && sibling.tagName !== "UL") {
    sibling = sibling.nextElementSibling
  }

  if (!sibling || sibling.tagName !== "UL") return

  const highlightsList = sibling as HTMLUListElement
  const items = highlightsList.querySelectorAll("li")

  // Parse each highlight - they start with "TEAM: highlight text"
  items.forEach((li) => {
    const text = li.textContent || ""
    const match = text.match(/^([A-Z]+):\s*(.+)$/i)
    if (match) {
      const team = match[1].toLowerCase()
      const highlight = match[2].trim()

      if (!teamHighlights[team]) {
        teamHighlights[team] = []
      }
      teamHighlights[team].push(highlight)
    }
  })
}

function hideOriginalHighlightsSection() {
  const content = document.getElementById("weekly-content")
  if (!content) return

  // Hide the "team highlights" and "top highlights" sections since we'll show them in tabs
  const teamHighlightsHeader = content.querySelector("h3#team-highlights")
  const topHighlightsHeader = content.querySelector("h3#top-highlights")

  if (teamHighlightsHeader) {
    ;(teamHighlightsHeader as HTMLElement).style.display = "none"
    // Hide everything until next h3
    let sibling = teamHighlightsHeader.nextElementSibling
    while (sibling && sibling.tagName !== "H3" && sibling.tagName !== "H2") {
      ;(sibling as HTMLElement).style.display = "none"
      sibling = sibling.nextElementSibling
    }
  }

  // Also hide top highlights in individual tabs (keep it visible in "All" view)
  if (topHighlightsHeader) {
    ;(topHighlightsHeader as HTMLElement).dataset.team = "highlights"
    // Mark its content too
    let sibling = topHighlightsHeader.nextElementSibling
    while (sibling && sibling.tagName !== "H3" && sibling.tagName !== "H2") {
      ;(sibling as HTMLElement).dataset.team = "highlights"
      sibling = sibling.nextElementSibling
    }
  }
}

function wrapTeamSections() {
  const content = document.getElementById("weekly-content")
  if (!content) return

  const headers = content.querySelectorAll("h3")

  headers.forEach((header, index) => {
    // Skip if already wrapped
    if (header.dataset.wrapped) return
    header.dataset.wrapped = "true"

    // Determine team from header ID (more reliable than text)
    const headerId = header.id || ""
    const headerText = header.textContent || ""
    let teamId = "other"

    // First try matching by ID
    for (const [id, pattern] of Object.entries(teamIdPatterns)) {
      if (pattern.test(headerId) || pattern.test(headerText.replace(/:/g, ""))) {
        teamId = id
        break
      }
    }

    // Special cases for non-team sections
    if (headerId === "team-highlights" || headerId === "top-highlights") {
      teamId = "highlights"
    }

    header.dataset.team = teamId
    header.dataset.index = String(index)

    // Collect all siblings until next h3 or h2
    const siblings: Element[] = []
    let sibling = header.nextElementSibling

    while (sibling && sibling.tagName !== "H3" && sibling.tagName !== "H2") {
      siblings.push(sibling)
      sibling = sibling.nextElementSibling
    }

    // Wrap siblings in a team-section div
    if (siblings.length > 0) {
      const section = document.createElement("div")
      section.className = "team-section"
      section.dataset.team = teamId
      section.dataset.index = String(index)

      header.parentNode?.insertBefore(section, siblings[0])
      siblings.forEach((el) => section.appendChild(el))

      // Add highlights box for this team if we have any
      if (teamId !== "highlights" && teamId !== "other" && teamHighlights[teamId]) {
        const highlightsBox = createHighlightsBox(teamId, teamHighlights[teamId])
        section.insertBefore(highlightsBox, section.firstChild)
      }
    }
  })
}

function createHighlightsBox(teamId: string, highlights: string[]): HTMLElement {
  const box = document.createElement("div")
  box.className = "team-highlights-box"
  box.dataset.team = teamId

  const title = document.createElement("div")
  title.className = "highlights-title"
  title.textContent = "Highlights"

  const list = document.createElement("ul")
  list.className = "highlights-list"

  highlights.forEach((highlight) => {
    const li = document.createElement("li")
    li.textContent = highlight
    list.appendChild(li)
  })

  box.appendChild(title)
  box.appendChild(list)

  return box
}

function updateStats() {
  const content = document.getElementById("weekly-content")
  if (!content) return

  const githubLinks = content.querySelectorAll('a[data-link-type="github"]').length

  // Count actual team sections (not highlights)
  const teamSections = Array.from(content.querySelectorAll("h3")).filter((h) => {
    const team = (h as HTMLElement).dataset.team
    return team && team !== "highlights" && team !== "other"
  }).length

  const statTeams = document.getElementById("stat-teams")
  const statPrs = document.getElementById("stat-prs")

  if (statTeams) statTeams.textContent = String(teamSections)
  if (statPrs) statPrs.textContent = String(githubLinks)
}

function updateTeamBadges() {
  const content = document.getElementById("weekly-content")
  if (!content) return

  // Count items per team (only top-level tasks, not nested details)
  const teamCounts: Record<string, number> = {}

  content.querySelectorAll(".team-section").forEach((section) => {
    const team = (section as HTMLElement).dataset.team || "other"
    if (team === "highlights" || team === "other") return

    // Count only direct children li of the top-level ul (not nested li or highlights)
    // The structure is: .team-section > ul > li (top-level tasks) > ul > li (details)
    const topLevelUls = section.querySelectorAll(":scope > ul")
    let count = 0
    topLevelUls.forEach((ul) => {
      // Count direct li children only (not nested)
      const directLis = ul.querySelectorAll(":scope > li")
      count += directLis.length
    })

    teamCounts[team] = (teamCounts[team] || 0) + count
  })

  // Update badges
  for (const [teamId, count] of Object.entries(teamCounts)) {
    const badge = document.getElementById(`badge-${teamId}`)
    if (badge) badge.textContent = String(count)
  }
}

function setupTabs() {
  const tabs = document.querySelectorAll(".team-tab")

  tabs.forEach((tab) => {
    // Clone to remove existing listeners
    const newTab = tab.cloneNode(true)
    tab.parentNode?.replaceChild(newTab, tab)

    newTab.addEventListener("click", (e) => {
      const target = e.currentTarget as HTMLElement
      const team = target.dataset.team || "all"

      // Update active state
      document.querySelectorAll(".team-tab").forEach((t) => t.classList.remove("active"))
      target.classList.add("active")

      currentTeam = team
      filterByTeam(team)

      // Get current search query and apply combined filter
      const searchInput = document.getElementById("weekly-search") as HTMLInputElement
      const query = searchInput?.value.toLowerCase().trim() || ""
      filterContent(query, currentFilter, team)
    })
  })
}

function filterByTeam(team: string) {
  const content = document.getElementById("weekly-content")
  if (!content) return

  const headers = content.querySelectorAll("h3")
  const sections = content.querySelectorAll(".team-section")

  if (team === "all") {
    // Show all teams but hide the highlights sections (they're now in team tabs)
    content.classList.add("show-all")
    headers.forEach((h) => {
      const headerTeam = (h as HTMLElement).dataset.team
      if (headerTeam === "highlights") {
        ;(h as HTMLElement).style.display = "none"
      } else {
        ;(h as HTMLElement).style.display = ""
      }
    })
    sections.forEach((s) => {
      const sectionTeam = (s as HTMLElement).dataset.team
      if (sectionTeam === "highlights") {
        ;(s as HTMLElement).style.display = "none"
      } else {
        ;(s as HTMLElement).style.display = ""
      }
    })
  } else {
    // Show only selected team
    content.classList.remove("show-all")

    headers.forEach((h) => {
      const headerTeam = (h as HTMLElement).dataset.team
      ;(h as HTMLElement).style.display = headerTeam === team ? "" : "none"
    })

    sections.forEach((s) => {
      const sectionTeam = (s as HTMLElement).dataset.team
      ;(s as HTMLElement).style.display = sectionTeam === team ? "" : "none"
    })
  }
}

function setupSearch() {
  const searchInput = document.getElementById("weekly-search") as HTMLInputElement
  if (!searchInput) return

  // Remove existing listener by replacing with clone, then add new listener
  const newSearchInput = searchInput.cloneNode(true) as HTMLInputElement
  searchInput.parentNode?.replaceChild(newSearchInput, searchInput)

  newSearchInput.addEventListener("input", (e) => {
    const query = (e.target as HTMLInputElement).value.toLowerCase().trim()
    console.log("Search query:", query, "Team:", currentTeam, "Filter:", currentFilter)
    filterContent(query, currentFilter, currentTeam)
  })

  // Also handle Enter key
  newSearchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault()
      const query = (e.target as HTMLInputElement).value.toLowerCase().trim()
      filterContent(query, currentFilter, currentTeam)
    }
  })
}

function setupFilters() {
  const filterBtns = document.querySelectorAll(".filter-btn")

  filterBtns.forEach((btn) => {
    // Clone to remove existing listeners
    const newBtn = btn.cloneNode(true)
    btn.parentNode?.replaceChild(newBtn, btn)

    newBtn.addEventListener("click", (e) => {
      const target = e.target as HTMLElement
      const filter = target.dataset.filter || "all"

      // Update active state
      document.querySelectorAll(".filter-btn").forEach((b) => b.classList.remove("active"))
      target.classList.add("active")

      currentFilter = filter

      // Get current search query and apply combined filter
      const searchInput = document.getElementById("weekly-search") as HTMLInputElement
      const query = searchInput?.value.toLowerCase().trim() || ""
      filterContent(query, filter, currentTeam)
    })
  })
}

function setupExpandableHeaders() {
  const content = document.getElementById("weekly-content")
  if (!content) return

  const headers = content.querySelectorAll("h3")

  headers.forEach((header) => {
    // Skip if already set up or if it's a special section
    if ((header as HTMLElement).dataset.expandable) return
    const team = (header as HTMLElement).dataset.team
    if (team === "highlights") return
    ;(header as HTMLElement).dataset.expandable = "true"

    header.addEventListener("click", () => {
      const index = (header as HTMLElement).dataset.index
      const section = content.querySelector(`.team-section[data-index="${index}"]`)

      header.classList.toggle("collapsed")
      if (section) {
        section.classList.toggle("hidden")
      }
    })
  })
}

function filterContent(searchQuery: string, linkFilter: string, teamFilter: string) {
  const content = document.getElementById("weekly-content")
  const noResults = document.getElementById("weekly-no-results")
  if (!content) return

  let visibleItemCount = 0

  // First, handle team-level filtering (show/hide entire sections based on team tab)
  const headers = content.querySelectorAll("h3")
  headers.forEach((header) => {
    const headerEl = header as HTMLElement
    const index = headerEl.dataset.index
    const section = content.querySelector(`.team-section[data-index="${index}"]`)
    if (!section) return

    const sectionEl = section as HTMLElement
    const headerTeam = headerEl.dataset.team || ""

    // Skip highlights sections
    if (headerTeam === "highlights") {
      headerEl.style.display = "none"
      sectionEl.style.display = "none"
      return
    }

    // Team filter - hide entire section if team doesn't match
    const matchesTeam = teamFilter === "all" || headerTeam === teamFilter
    if (!matchesTeam) {
      headerEl.classList.add("filtered-out")
      sectionEl.classList.add("filtered-out")
      return
    }

    // Team matches - show header and section, then filter individual items
    headerEl.classList.remove("filtered-out")
    sectionEl.classList.remove("filtered-out")
  })

  // Now filter individual list items within visible sections
  content.querySelectorAll(".team-section:not(.filtered-out)").forEach((section) => {
    // Get top-level list items (direct children of top-level ul)
    const topLevelUls = section.querySelectorAll(":scope > ul")

    topLevelUls.forEach((ul) => {
      const items = ul.querySelectorAll(":scope > li")

      items.forEach((item) => {
        const itemEl = item as HTMLElement
        const itemText = item.textContent?.toLowerCase() || ""

        // Search filter
        const matchesSearch = !searchQuery || itemText.includes(searchQuery)

        // Link type filter
        let matchesLinkFilter = true
        if (linkFilter !== "all") {
          const links = item.querySelectorAll(`a[data-link-type="${linkFilter}"]`)
          matchesLinkFilter = links.length > 0
        }

        const isVisible = matchesSearch && matchesLinkFilter

        if (isVisible) {
          itemEl.classList.remove("filtered-out")
          visibleItemCount++
        } else {
          itemEl.classList.add("filtered-out")
        }
      })
    })

    // Also handle highlights box visibility
    const highlightsBox = section.querySelector(".team-highlights-box")
    if (highlightsBox) {
      const boxEl = highlightsBox as HTMLElement
      if (searchQuery) {
        // Hide highlights box when searching
        boxEl.style.display = "none"
      } else {
        boxEl.style.display = ""
      }
    }
  })

  // Check if any team sections have visible items
  let sectionsWithVisibleItems = 0
  content.querySelectorAll(".team-section:not(.filtered-out)").forEach((section) => {
    const visibleItems = section.querySelectorAll(":scope > ul > li:not(.filtered-out)")
    if (visibleItems.length > 0) {
      sectionsWithVisibleItems++
    }
  })

  // Show/hide no results message
  if (noResults) {
    noResults.style.display =
      visibleItemCount === 0 && (searchQuery || linkFilter !== "all") ? "block" : "none"
  }
}

// Initial setup
document.addEventListener("DOMContentLoaded", setupWeeklyReport)

// Re-run setup on SPA navigation
document.addEventListener("nav", () => {
  setupWeeklyReport()
})
