import { FolderState } from "../ExplorerNode"
import { ContentDetails } from "../../plugins/emitters/contentIndex"
import { FullSlug, resolveRelative } from "../../util/path"

// Current state of folders
let explorerState: FolderState[]
let explorerTree: ExplorerTreeNode | undefined

type ExplorerTreeNode = {
  children: ExplorerTreeNode[]
  depth: number
  displayName: string
  name: string
  slug?: FullSlug
}

type ContentIndexData = Record<FullSlug, ContentDetails>

const observer = new IntersectionObserver((entries) => {
  // If last element is observed, remove gradient of "overflow" class so element is visible
  const explorer = document.getElementById("explorer-ul")
  for (const entry of entries) {
    if (entry.isIntersecting) {
      explorer?.classList.add("no-background")
    } else {
      explorer?.classList.remove("no-background")
    }
  }
})

function toggleExplorer(this: HTMLElement) {
  // Toggle collapsed state of entire explorer
  this.classList.toggle("collapsed")
  const content = this.nextElementSibling as HTMLElement
  content.classList.toggle("collapsed")
  content.style.maxHeight = content.style.maxHeight === "0px" ? content.scrollHeight + "px" : "0px"
}

function toggleFolder(evt: MouseEvent) {
  evt.stopPropagation()

  // Element that was clicked
  const target = evt.target as HTMLElement

  // Check if target was svg icon or button
  const isSvg = target.nodeName === "svg"

  // corresponding <ul> element relative to clicked button/folder
  let childFolderContainer: HTMLElement

  // <li> element of folder (stores folder-path dataset)
  let currentFolderParent: HTMLElement

  // Get correct relative container and toggle collapsed class
  if (isSvg) {
    childFolderContainer = target.parentElement?.nextSibling as HTMLElement
    currentFolderParent = target.nextElementSibling as HTMLElement

    childFolderContainer.classList.toggle("open")
  } else {
    childFolderContainer = target.parentElement?.parentElement?.nextElementSibling as HTMLElement
    currentFolderParent = target.parentElement as HTMLElement

    childFolderContainer.classList.toggle("open")
  }
  if (!childFolderContainer) return

  // Collapse folder container
  const isCollapsed = !childFolderContainer.classList.contains("open")

  // Save folder state to localStorage
  const clickFolderPath = currentFolderParent.dataset.folderpath as string

  // Remove leading "/"
  const fullFolderPath = clickFolderPath.substring(1)
  setCollapsedByPath(explorerState, fullFolderPath, isCollapsed)

  const stringifiedFileTree = JSON.stringify(explorerState)
  localStorage.setItem("fileTree", stringifiedFileTree)
}

async function setupExplorer(currentSlug: FullSlug) {
  // Set click handler for collapsing entire explorer
  const explorer = document.getElementById("explorer")
  if (!explorer) {
    return
  }

  // Get folder state from local storage
  const storageTree = localStorage.getItem("fileTree")

  // Convert to bool
  const useSavedFolderState = explorer?.dataset.savestate === "true"

  if (!explorerTree) {
    explorerTree = buildExplorerTree((await fetchData) as ContentIndexData)
  }

  // Get config
  const collapseBehavior = explorer.dataset.behavior
  const defaultCollapsed = explorer.dataset.collapsed === "collapsed"

  explorerState = mergeFolderState(
    getFolderPaths(explorerTree, defaultCollapsed),
    useSavedFolderState ? storageTree : null,
  )

  renderExplorer(explorerTree, currentSlug)

  // Add click handlers for all folders (click handler on folder "label")
  if (collapseBehavior === "collapse") {
    Array.prototype.forEach.call(document.getElementsByClassName("folder-button"), function (item) {
      item.removeEventListener("click", toggleFolder)
      item.addEventListener("click", toggleFolder)
    })
  }

  // Add click handler to main explorer
  explorer.removeEventListener("click", toggleExplorer)
  explorer.addEventListener("click", toggleExplorer)

  // Set up click handlers for each folder (click handler on folder "icon")
  Array.prototype.forEach.call(document.getElementsByClassName("folder-icon"), function (item) {
    item.removeEventListener("click", toggleFolder)
    item.addEventListener("click", toggleFolder)
  })

  explorerState.map((folderUl) => {
    // grab <li> element for matching folder path
    const folderLi = document.querySelector(`[data-folderpath='/${folderUl.path}']`) as HTMLElement

    // Get corresponding content <ul> tag and set state
    if (folderLi) {
      const folderUL = folderLi.parentElement?.nextElementSibling
      if (folderUL) {
        setFolderState(folderUL as HTMLElement, folderUl.collapsed)
      }
    }
  })
}

let currentExplorerSlug: FullSlug | undefined
window.addEventListener("resize", () => {
  if (currentExplorerSlug) {
    setupExplorer(currentExplorerSlug)
  }
})
document.addEventListener("nav", async () => {
  currentExplorerSlug = document.body.dataset.slug as FullSlug
  await setupExplorer(currentExplorerSlug)

  const explorerContent = document.getElementById("explorer-ul")
  // select pseudo element at end of list
  const lastItem = document.getElementById("explorer-end")

  observer.disconnect()
  if (lastItem) {
    observer.observe(lastItem as Element)
  }
})

/**
 * Toggles the state of a given folder
 * @param folderElement <div class="folder-outer"> Element of folder (parent)
 * @param collapsed if folder should be set to collapsed or not
 */
function setFolderState(folderElement: HTMLElement, collapsed: boolean) {
  if (collapsed) {
    folderElement?.classList.remove("open")
  } else {
    folderElement?.classList.add("open")
  }
}

/**
 * Toggles visibility of a folder
 * @param array array of FolderState (`fileTree`, either get from local storage or data attribute)
 * @param path path to folder (e.g. 'advanced/more/more2')
 */
function setCollapsedByPath(array: FolderState[], path: string, collapsed: boolean) {
  const entry = array.find((item) => item.path === path)
  if (entry) {
    entry.collapsed = collapsed
  }
}

function buildExplorerTree(data: ContentIndexData): ExplorerTreeNode {
  const root: ExplorerTreeNode = { name: "", displayName: "", children: [], depth: 0 }

  for (const slug of Object.keys(data) as FullSlug[]) {
    if (slug === "index" || slug.startsWith("tags/")) {
      continue
    }

    const parts = slug.split("/")
    let node = root

    for (let i = 0; i < parts.length; i++) {
      const name = parts[i]
      const isLast = i === parts.length - 1

      if (isLast && name === "index") {
        const title = data[slug]?.title
        if (title && title !== "index") {
          node.displayName = title
        }
        continue
      }

      if (isLast) {
        node.children.push({
          name,
          displayName: data[slug]?.title ?? name,
          slug,
          children: [],
          depth: node.depth + 1,
        })
        continue
      }

      let child = node.children.find((candidate) => !candidate.slug && candidate.name === name)
      if (!child) {
        child = {
          name,
          displayName: name,
          children: [],
          depth: node.depth + 1,
        }
        node.children.push(child)
      }
      node = child
    }
  }

  sortTree(root)
  return root
}

function sortTree(node: ExplorerTreeNode) {
  node.children.sort((a, b) => {
    if ((!a.slug && !b.slug) || (a.slug && b.slug)) {
      return a.displayName.localeCompare(b.displayName, undefined, {
        numeric: true,
        sensitivity: "base",
      })
    }

    return a.slug ? 1 : -1
  })

  node.children.forEach(sortTree)
}

function getFolderPaths(tree: ExplorerTreeNode, collapsed: boolean): FolderState[] {
  const folderPaths: FolderState[] = []

  function traverse(node: ExplorerTreeNode, currentPath: string) {
    if (!node.slug) {
      const folderPath = currentPath + (currentPath ? "/" : "") + node.name
      if (folderPath !== "") {
        folderPaths.push({ path: folderPath, collapsed })
      }
      node.children.forEach((child) => traverse(child, folderPath))
    }
  }

  traverse(tree, "")
  return folderPaths
}

function mergeFolderState(defaultState: FolderState[], storageTree: string | null): FolderState[] {
  if (!storageTree) {
    return defaultState
  }

  try {
    const savedState = JSON.parse(storageTree) as FolderState[]
    const savedByPath = new Map(savedState.map((folder) => [folder.path, folder.collapsed]))
    return defaultState.map((folder) => ({
      ...folder,
      collapsed: savedByPath.get(folder.path) ?? folder.collapsed,
    }))
  } catch {
    return defaultState
  }
}

function renderExplorer(tree: ExplorerTreeNode, currentSlug: FullSlug) {
  const explorer = document.getElementById("explorer-ul")
  if (!explorer) {
    return
  }

  removeAllChildren(explorer)
  tree.children.forEach((child) => explorer.appendChild(renderNode(child, currentSlug, "")))

  const end = document.createElement("li")
  end.id = "explorer-end"
  explorer.appendChild(end)
}

function renderNode(node: ExplorerTreeNode, currentSlug: FullSlug, parentPath: string): HTMLElement {
  const item = document.createElement("li")

  if (node.slug) {
    const linkItem = document.createElement("li")
    const link = document.createElement("a")
    link.href = resolveRelative(currentSlug, node.slug)
    link.dataset.for = node.slug
    link.textContent = node.displayName
    linkItem.appendChild(link)
    item.appendChild(linkItem)
    return item
  }

  const folderPath = parentPath ? `${parentPath}/${node.name}` : `/${node.name}`
  const folder = document.createElement("div")
  const folderContainer = document.createElement("div")
  folderContainer.className = "folder-container"

  const icon = document.createElementNS("http://www.w3.org/2000/svg", "svg")
  icon.setAttribute("width", "12")
  icon.setAttribute("height", "12")
  icon.setAttribute("viewBox", "5 8 14 8")
  icon.setAttribute("fill", "none")
  icon.setAttribute("stroke", "currentColor")
  icon.setAttribute("stroke-width", "2")
  icon.setAttribute("stroke-linecap", "round")
  icon.setAttribute("stroke-linejoin", "round")
  icon.classList.add("folder-icon")

  const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline")
  polyline.setAttribute("points", "6 9 12 15 18 9")
  icon.appendChild(polyline)
  folderContainer.appendChild(icon)

  const label = document.createElement("div")
  label.dataset.folderpath = folderPath

  const button = document.createElement("button")
  button.className = "folder-button"

  const title = document.createElement("p")
  title.className = "folder-title"
  title.textContent = node.displayName

  button.appendChild(title)
  label.appendChild(button)
  folderContainer.appendChild(label)
  folder.appendChild(folderContainer)

  const outer = document.createElement("div")
  outer.className = "folder-outer"

  const list = document.createElement("ul")
  list.className = "content"
  list.dataset.folderul = folderPath
  list.style.paddingLeft = "1.4rem"
  node.children.forEach((child) => list.appendChild(renderNode(child, currentSlug, folderPath)))

  outer.appendChild(list)
  folder.appendChild(outer)
  item.appendChild(folder)

  return item
}

function removeAllChildren(node: HTMLElement) {
  while (node.firstChild) {
    node.removeChild(node.firstChild)
  }
}
