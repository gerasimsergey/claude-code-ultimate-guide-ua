---
title: "Claude Code Release History"
description: "Condensed changelog of official Claude Code releases with highlights and breaking changes"
tags: [reference, release]
---

# Claude Code Release History

> Condensed changelog of Claude Code official releases.
> **Full details**: [github.com/anthropics/claude-code/CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
> **Machine-readable**: [claude-code-releases.yaml](../machine-readable/claude-code-releases.yaml)

**Latest**: v2.1.126 | **Updated**: 2026-05-01

---

## Quick Jump

- [2.1.x Series (January-May 2026)](#21x-series-january-may-2026) — Worktree isolation, background agents, ConfigChange hook, Fast mode Opus 4.6, 1M context, claude.ai MCP connectors, remote-control, auto-memory, /copy command, HTTP hooks, worktree config sharing, ultrathink re-introduced, InstructionsLoaded hook, 4 security fixes, Agent model override restored, 12x SDK token cost reduction, /context actionable suggestions, modelOverrides setting, 1M context Opus 4.6 default for Max/Team/Enterprise, MCP elicitation, PostCompact hook, /effort command, Opus 4.6 64k/128k output tokens, allowRead sandbox setting, /branch command, StopFailure hook, streaming line-by-line, --console auth flag, SessionEnd fix, enterprise retry fix, rate_limits statusline field, effort frontmatter for skills, --channels MCP research preview, --bare flag, worktree session resume fix, MCP query collapsing, managed-settings.d/ drop-in, CwdChanged/FileChanged hooks, transcript search, credential scrubbing, PowerShell tool Windows preview, conditional hooks if field, MCP headersHelper multi-server env vars, headless AskUserQuestion hooks, X-Claude-Code-Session-Id header, Jujutsu/Sapling VCS exclusions, @ mention token reduction, Read tool compact format, Cowork Dispatch fix, PermissionDenied hook, thinking summaries off by default, "defer" PreToolUse permission, CLAUDE_CODE_NO_FLICKER, /powerup interactive lessons, PowerShell hardened permissions, SSE linear-time performance, MCP 500K result override, disableSkillShellExecution, plugin bin/ executables, Edit tool shorter anchors, interactive Bedrock wizard, forceRemoteSettingsRefresh, /cost per-model breakdown, interactive /release-notes, Linux sandbox apply-seccomp fix, Bedrock Mantle support, high effort default for API/enterprise users, Bedrock auth fix, NO_FLICKER focus view (Ctrl+O), refreshInterval status line, 30+ bug fixes, Vertex AI wizard, Monitor tool, CLAUDE_CODE_PERFORCE_MODE, Bash security hardening, subprocess PID namespace sandboxing, /team-onboarding command, OS CA cert store trust by default, /ultraplan auto-cloud-environment, 40+ bug fixes, PreCompact hook blocking, EnterWorktree path param, plugin monitors, /proactive alias, WebFetch CSS/JS stripping, /doctor status icons, thinking hints sooner, ENABLE_PROMPT_CACHING_1H, /recap session context, built-in slash commands via Skill tool, /undo alias, rotating extended-thinking indicator, /tui fullscreen command, push notification tool, --resume resurrects scheduled tasks, /focus command, autoScrollEnabled config, session recap for telemetry-disabled, 30+ bug fixes, Opus 4.7 xhigh effort, /ultrareview cloud code review, /less-permission-prompts skill, Auto mode for Max subscribers, plan files named after prompts, read-only bash glob patterns no prompt, interactive /effort slider, many bug fixes, native binary spawning, sandbox.network.deniedDomains, security hardening exec wrappers, crash fix permission dialog, /resume 67% faster, inline thinking progress, sandbox dangerous-path security fix, agent frontmatter hooks via --agent, many terminal and UI bug fixes, default effort high for Pro/Max on Opus 4.6+Sonnet 4.6, native bfs/ugrep on macOS/Linux, /model persistence across restarts, Opus 4.7 1M context fix, 15+ bug fixes, vim visual mode, /usage merged from /cost+/stats, custom named themes, hooks invoke MCP tools, DISABLE_UPDATES env var, wslInheritsWindowsSettings, 15+ bug fixes, /config settings persist to settings.json, --from-pr multi-platform support, agent frontmatter honors tools+permissionMode, blockedMarketplaces security fix, TaskList ordering fix, 30+ bug fixes, Windows no longer requires Git Bash (PowerShell fallback), claude ultrareview CI subcommand, ${CLAUDE_EFFORT} in skills, alwaysLoad MCP option, plugin prune, PostToolUse output replacement for all tools, ANTHROPIC_BEDROCK_SERVICE_TIER, PR URL in /resume search, OAuth 401 hotfix, gateway /v1/models listing in /model picker, claude project purge, OAuth paste code for WSL2/SSH/containers, security fix allowManagedDomainsOnly/allowManagedReadPathsOnly, Windows PowerShell 7 as primary shell, 40+ bug fixes
- [2.0.x Series (Nov 2025 - Jan 2026)](#20x-series-november-2025---january-2026) — Opus 4.5, Claude in Chrome, Background agents
- [Breaking Changes Summary](#breaking-changes-summary)
- [Milestone Features](#milestone-features)

---

## 2.1.x Series (January-May 2026)

### v2.1.126 (2026-05-01)

> Gateway /v1/models listing in /model picker, claude project purge, OAuth paste code for WSL2/SSH, Windows PowerShell 7 as primary shell, security fix, 40+ bug fixes.

- **New**: `/model` picker now lists models from your gateway's `/v1/models` endpoint when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway
- **New**: `claude project purge [path]` deletes all Claude Code state for a project (transcripts, tasks, file history, config entry) — supports `--dry-run`, `-y/--yes`, `-i/--interactive`, and `--all`
- **Improved**: `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and other previously-protected paths (catastrophic removal commands still prompt as a safety net)
- **Improved**: `claude auth login` accepts the OAuth code pasted into the terminal when the browser callback can't reach localhost (WSL2, SSH, containers)
- **Improved**: `claude_code.skill_activated` OpenTelemetry event now fires for user-typed slash commands with a new `invocation_trigger` attribute (`"user-slash"`, `"claude-proactive"`, or `"nested-skill"`)
- **Improved**: Auto mode spinner now turns red when a permission check stalls, instead of looking like the tool is running
- **Improved**: Windows — PowerShell 7 installed via Microsoft Store, MSI without PATH, or `.NET global tool` is now detected; when PowerShell tool is enabled, Claude treats PowerShell as the primary shell instead of defaulting to Bash
- **Improved**: Read tool — removed the per-file malware-assessment reminder that caused spurious refusals on legacy models
- **Security**: Fixed `allowManagedDomainsOnly` / `allowManagedReadPathsOnly` being ignored when a higher-priority managed-settings source lacked a `sandbox` block
- **Fixed**: Pasting an image larger than 2000px no longer breaks the session — images are downscaled on paste, oversized images in history are automatically removed and the request retried
- **Fixed**: OAuth login failing with timeout on slow or proxied connections, in IPv6-only devcontainers, and when the browser callback can't reach localhost
- **Fixed**: "Stream idle timeout" error after waking Mac from sleep mid-request; background and remote sessions no longer falsely abort during long model thinking pauses
- **Fixed**: Japanese/Korean/Chinese text rendering as garbled characters on Windows in no-flicker mode
- **Fixed**: `Ctrl+L` clearing the prompt input — it now only forces a screen redraw, matching readline behavior
- **Fixed**: Deferred tools (WebSearch, WebFetch, etc.) not available to skills with `context: fork` on their first turn
- **Fixed**: Windows clipboard writes no longer expose copied content in process command-line arguments visible to EDR/SIEM telemetry; also fixes >22KB selections not reaching the clipboard
- **Fixed**: Agent SDK hang when the model emits a malformed tool name in a parallel tool call batch
- **Fixed**: `/plugin` Uninstall reporting "Enabled" instead of "Uninstalled"

---

### v2.1.123 (2026-04-29)

> Hotfix: OAuth 401 retry loop when CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1.

- **Fixed**: OAuth authentication failing with a 401 retry loop when `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` is set

---

### v2.1.122 (2026-04-28)

> ANTHROPIC_BEDROCK_SERVICE_TIER env var, PR URL in /resume search, Vertex AI/Bedrock fixes, image resize fix, many bug fixes.

- **New**: `ANTHROPIC_BEDROCK_SERVICE_TIER` environment variable to select a Bedrock service tier (`default`, `flex`, or `priority`) via `X-Amzn-Bedrock-Service-Tier` header
- **New**: Pasting a PR URL into the `/resume` search box now finds the session that created that PR (GitHub, GitHub Enterprise, GitLab, and Bitbucket)
- **Improved**: `/mcp` now shows claude.ai connectors hidden by a manually-added server with the same URL, with a hint to remove the duplicate
- **Fixed**: `/branch` producing forks that fail with "tool_use ids were found without tool_result blocks" from rewound timelines
- **Fixed**: `/model` not showing Effort option for Bedrock application inference profile ARNs
- **Fixed**: Vertex AI / Bedrock returning `invalid_request_error: output_config: Extra inputs are not permitted` on title generation and structured-output queries
- **Fixed**: Vertex AI `count_tokens` endpoint returning 400 errors for users behind proxy gateways
- **Fixed**: `!exit` / `!quit` in bash mode terminating the CLI instead of running as a shell command
- **Fixed**: Images sent to newer models being resized to 2576px instead of the correct 2000px maximum
- **Fixed**: Remote control session idle status redrawing twice per second, flooding `tmux -CC` control pipes
- **Fixed**: `ToolSearch` missing MCP tools that connected after session start in nonblocking mode
- **Fixed**: A malformed hooks entry in `settings.json` no longer invalidating the entire file
- **Fixed**: `spinnerTipsOverride.excludeDefault` not suppressing time-based spinner tips
- **Fixed**: Assistant messages appearing blank in some sessions due to a stale view preference

---

### v2.1.121 (2026-04-27)

> alwaysLoad MCP config, plugin prune, PostToolUse output replacement for all tools, critical memory leak fixes, many bug fixes.

- **New**: `alwaysLoad` option in MCP server config — when `true`, all tools from that server skip tool-search deferral and are always available
- **New**: `claude plugin prune` removes orphaned auto-installed plugin dependencies; `plugin uninstall --prune` cascades
- **New**: Type-to-filter search box in `/skills` for finding a skill without scrolling
- **New**: `PostToolUse` hooks can now replace tool output for all tools via `hookSpecificOutput.updatedToolOutput` (previously MCP-only)
- **New**: Vertex AI: support X.509 certificate-based Workload Identity Federation (mTLS ADC)
- **Improved**: Fullscreen mode: typing into the prompt no longer jumps scroll to the bottom after scrolling up
- **Improved**: Dialogs that overflow the terminal are now scrollable with arrow keys, PgUp/PgDn, home/end, and mouse wheel
- **Improved**: Clicking any line of a long URL wrapping across rows in fullscreen now opens the full URL
- **Improved**: `--dangerously-skip-permissions` no longer prompts for writes to `.claude/skills/`, `.claude/agents/`, and `.claude/commands/`
- **Improved**: `/terminal-setup` now enables iTerm2's "Applications in terminal may access clipboard" for `/copy` in tmux
- **Improved**: MCP servers that hit a transient startup error now auto-retry up to 3 times
- **Improved**: Terminal tab session title is now generated in your configured `language` setting
- **Improved**: Claude.ai connectors with the same upstream URL are now deduplicated
- **Improved**: LSP diagnostic summaries now expand on click/ctrl+o and show the expand hint
- **Improved**: OpenTelemetry: added `stop_reason`, `gen_i.response.finish_reasons`, and `user_system_prompt` (gated behind `OTEL_LOG_USER_PROMPTS`)
- **[VSCode]**: `/context` now opens a native token usage dialog; voice dictation respects `accessibility.voice.speechLanguage`
- **Fixed**: Unbounded memory growth (multi-GB RSS) when processing many images in a session
- **Fixed**: `/usage` leaking up to ~2GB of memory on machines with large transcript histories
- **Fixed**: Memory leak when long-running tools fail to emit a clear progress event
- **Fixed**: Bash tool becoming permanently unusable when the start directory is deleted or moved mid-session
- **Fixed**: `--resume` crashing on startup in external builds
- **Fixed**: `--resume` failing on large sessions when a transcript line was corrupted by an unclean shutdown
- **Fixed**: `thinking.type.enabled is not supported` error with Bedrock application inference profile ARNs
- **Fixed**: Microsoft 365 MCP OAuth failing with duplicate or unsupported `prompt` parameter
- **Fixed**: Scrollback duplication when pressing Ctrl+L in non-fullscreen mode on tmux, GNOME Terminal, Windows Terminal, Konsole
- **Fixed**: claude.ai MCP connectors silently disappearing on transient auth error at startup
- **Fixed**: "Always allow" rules for built-in tools in remote sessions not surviving worker restarts
- **Fixed**: `NO_PROXY` not respected for all HTTP clients when set via `managed-settings.json` on native build
- **Fixed**: Managed settings approval prompt exiting the session even when accepted

---

### v2.1.120 (2026-04-24)

> Windows no longer requires Git Bash, claude ultrareview CI subcommand, ${CLAUDE_EFFORT} in skills, many bug fixes.

- **New**: Windows: Git for Windows (Git Bash) is no longer required — when absent, Claude Code uses PowerShell as the shell tool
- **New**: `claude ultrareview [target]` subcommand to run `/ultrareview` non-interactively from CI or scripts; `--json` for raw output; exits 0 on completion or 1 on failure
- **New**: Skills can reference the current effort level with `${CLAUDE_EFFORT}` in their content
- **New**: `AI_AGENT` environment variable set for subprocesses so `gh` can attribute traffic to Claude Code
- **Improved**: Faster session start when many claude.ai connectors are configured but not authorized
- **Improved**: `claude plugin validate` now accepts `$schema`, `version`, and `description` at the top level of `marketplace.json`
- **Improved**: Auto-compact in auto mode now displays `auto` (lowercase) instead of a misleading token value
- **Improved**: Spinner tips recommending the desktop app or creating skills/agents are hidden when you already have them
- **Improved**: Show a "use PgUp/PgDn to scroll" hint when the terminal sends arrow keys instead of scroll events
- **Fixed**: Pressing Esc during a stdio MCP tool call closing the entire server connection (regression in 2.1.105)
- **Fixed**: `/rewind` and other interactive overlays not responding to keyboard input after `--resume`
- **Fixed**: Terminal scrollback duplication in non-fullscreen mode (resize, dialog dismiss, long sessions)
- **Fixed**: `DISABLE_TELEMETRY` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` not suppressing usage metrics telemetry for API and enterprise users
- **Fixed**: False-positive "Dangerous rm operation" permission prompts in auto mode for multi-line bash with pipe and redirect
- **Fixed**: Long selection menus clipping below the terminal in fullscreen mode
- **Fixed**: Write tool output collapsing instead of expanding when clicking "+N lines" in fullscreen
- **Fixed**: Slash command picker jumping while typing; highlight now only matches contiguous substrings
- **Fixed**: `/plugin` marketplace failing to load when one entry uses an unrecognized source format
- **Fixed**: `find` in the Bash tool exhausting open file descriptors on large directory trees, causing host-wide crashes (macOS/Linux native builds)
- **[VSCode]**: `/usage` now opens the native Account & Usage dialog; voice dictation respects the `language` setting

---

### v2.1.119 (2026-04-24)

> /config settings persist to settings.json with override precedence, --from-pr supports GitLab/Bitbucket/GitHub Enterprise, agent frontmatter improvements, security fix for blockedMarketplaces, 30+ bug fixes.

- **New**: `/config` settings (theme, editor mode, verbose, etc.) now persist to `~/.claude/settings.json` and participate in project/local/policy override precedence
- **New**: `prUrlTemplate` setting to point the footer PR badge at a custom code-review URL instead of github.com
- **New**: `CLAUDE_CODE_HIDE_CWD` environment variable to hide the working directory in the startup logo
- **New**: `--from-pr` now accepts GitLab merge-request, Bitbucket pull-request, and GitHub Enterprise PR URLs
- **Improved**: `--print` mode now honors the agent's `tools:` and `disallowedTools:` frontmatter, matching interactive-mode behavior
- **Improved**: `--agent <name>` now honors the agent definition's `permissionMode` for built-in agents
- **Improved**: PowerShell tool commands can now be auto-approved in permission mode, matching Bash behavior
- **Improved**: `PostToolUse` and `PostToolUseFailure` hook inputs now include `duration_ms` (tool execution time, excluding permission prompts and PreToolUse hooks)
- **Improved**: Subagent and SDK MCP server reconfiguration now connects servers in parallel instead of serially
- **Improved**: Plugins pinned by another plugin's version constraint now auto-update to the highest satisfying git tag
- **Improved**: Vim mode: Esc in INSERT no longer pulls a queued message back into the input; press Esc again to interrupt
- **Improved**: Slash command suggestions now highlight the characters that matched your query; picker wraps long descriptions instead of truncating
- **Improved**: `owner/repo#N` shorthand links now use your git remote's host instead of always pointing at github.com
- **Security**: `blockedMarketplaces` now correctly enforces `hostPattern` and `pathPattern` entries
- **Fixed**: Pasting CRLF content (Windows clipboards, Xcode console) inserting an extra blank line between every line
- **Fixed**: Glob and Grep tools disappearing on native macOS/Linux builds when Bash tool is denied via permissions
- **Fixed**: Scrolling up in fullscreen mode snapping back to the bottom every time a tool finishes
- **Fixed**: Auto mode overriding plan mode with conflicting "Execute immediately" instructions
- **Fixed**: `Agent` tool with `isolation: "worktree"` reusing stale worktrees from prior sessions
- **Fixed**: `TaskList` returning tasks in arbitrary filesystem order instead of sorted by ID
- **Fixed**: `/plan` and `/plan open` not acting on the existing plan when entering plan mode
- **Fixed**: Skills invoked before auto-compaction being re-executed against the next user message
- **Fixed**: Verbose output setting not persisting after restart; disabled MCP servers appearing as "failed" in `/status`
- **Fixed**: `${ENV_VAR}` placeholders in `headers` for HTTP/SSE/WebSocket MCP servers not being substituted
- **Fixed**: MCP OAuth `--client-secret` not sent during token exchange for `client_secret_post` servers
- **Fixed**: `/skills` Enter key closing dialog instead of pre-filling `/<skill-name>` in the prompt
- **Fixed**: Spurious "GitHub API rate limit exceeded" hints from PR titles mentioning "rate limit"
- **Fixed**: Async `PostToolUse` hooks emitting no response writing empty entries to session transcript
- **Fixed**: `@`-file Tab completion replacing the entire prompt when used inside a slash command with an absolute path

### v2.1.118 (2026-04-23)

> Vim visual mode, /usage merging /cost+/stats, custom named themes, hooks invoke MCP tools directly, many bug fixes.

- **New**: Vim visual mode (`v`) and visual-line mode (`V`) with selection, operators (d, y, c, >, <), and visual feedback
- **New**: `/cost` and `/stats` merged into `/usage` — both old commands remain as typing shortcuts that open the relevant tab
- **New**: Create and switch between named custom themes from `/theme`, or hand-edit JSON files in `~/.claude/themes/`; plugins can ship themes via a `themes/` directory
- **New**: Hooks can now invoke MCP tools directly via `type: "mcp_tool"` in hook configuration
- **New**: `DISABLE_UPDATES` env var completely blocks all update paths including manual `claude update` (stricter than `DISABLE_AUTOUPDATER`)
- **New**: WSL on Windows can inherit Windows-side managed settings via `wslInheritsWindowsSettings` policy key
- **Improved**: Auto mode `"$defaults"` sentinel — include in `autoMode.allow`, `autoMode.soft_deny`, or `autoMode.environment` to add custom rules alongside built-in list instead of replacing it
- **Improved**: "Don't ask again" option added to auto mode opt-in prompt
- **Improved**: `--continue`/`--resume` now find sessions that added the current directory via `/add-dir`
- **Improved**: `/color` syncs the session accent color to claude.ai/code when Remote Control is connected
- **Improved**: `/model` picker now honors `ANTHROPIC_DEFAULT_*_MODEL_NAME`/`_DESCRIPTION` overrides when using a custom `ANTHROPIC_BASE_URL` gateway
- **Improved**: `claude plugin tag` to create release git tags for plugins with version validation
- **Improved**: Auto-update skip due to version constraints now appears in `/doctor` and `/plugin` Errors tab
- **Fixed**: `/mcp` menu hiding OAuth Authenticate/Re-authenticate for servers with `headersHelper`, and HTTP/SSE servers stuck in "needs authentication" after a transient 401
- **Fixed**: MCP OAuth tokens with no `expires_in` in response requiring re-authentication every hour
- **Fixed**: MCP step-up authorization silently refreshing instead of prompting when `insufficient_scope` 403 names a scope already held
- **Fixed**: macOS keychain race where concurrent token refresh could overwrite a freshly-refreshed OAuth token
- **Fixed**: Credential save crash on Linux/Windows corrupting `~/.claude/.credentials.json`
- **Fixed**: `/login` having no effect in sessions launched with `CLAUDE_CODE_OAUTH_TOKEN` env var
- **Fixed**: Agent-type hooks failing with "Messages are required for agent hooks" for non-Stop events
- **Fixed**: `prompt` hooks re-firing on tool calls made by an agent-hook verifier subagent
- **Fixed**: `/fork` writing full parent conversation to disk per fork — now writes a pointer and hydrates on read
- **Fixed**: Alt+K / Alt+X / Alt+^ / Alt+_ freezing keyboard input
- **Fixed**: `plugin install` on an already-installed plugin not re-resolving a dependency at wrong version
- **Fixed**: Subagents resumed via `SendMessage` not restoring their explicit `cwd`

### v2.1.117 (2026-04-22)

> Default effort now `high` for Pro/Max on Opus 4.6 + Sonnet 4.6, native bfs/ugrep on macOS/Linux, Opus 4.7 1M context fix, /model persistence, 15+ bug fixes.

- **Changed**: Default effort level changed to `high` for Pro/Max subscribers on Opus 4.6 and Sonnet 4.6 (was `medium`)
- **Fixed**: Opus 4.7 sessions were computing `/context` percentage against a 200K window instead of the native 1M — causing inflated percentages and premature autocompact
- **New**: Native macOS/Linux builds now use embedded `bfs` (search) and `ugrep` (grep) replacing the Glob/Grep tools — faster without an extra tool round-trip (Windows and npm-installed builds unchanged)
- **Improved**: `/model` selections now persist across restarts even when the project pins a different model; startup header shows when the active model comes from a project or managed-settings pin
- **Improved**: `/resume` now offers to summarize stale, large sessions before re-reading them (matching existing `--resume` behavior)
- **Improved**: Faster startup when both local and claude.ai MCP servers are configured (concurrent connect now default)
- **Improved**: `plugin install` on an already-installed plugin now installs any missing dependencies instead of stopping at "already installed"; dependency errors say "not installed" with an install hint
- **Improved**: `cleanupPeriodDays` retention sweep now also covers `~/.claude/tasks/`, `~/.claude/shell-snapshots/`, and `~/.claude/backups/`
- **Improved**: Agent frontmatter `mcpServers` are now loaded for main-thread agent sessions via `--agent`
- **Improved**: OpenTelemetry `user_prompt` events now include `command_name` and `command_source` for slash commands; cost/token/API events include `effort` attribute when supported
- **Fixed**: Plain-CLI OAuth sessions dying with "Please run /login" when access token expires mid-session — token now refreshed reactively on 401
- **Fixed**: `WebFetch` hanging on very large HTML pages (truncates input before HTML-to-markdown conversion)
- **Fixed**: Crash when a proxy returns HTTP 204 No Content
- **Fixed**: `/login` having no effect when launched with `CLAUDE_CODE_OAUTH_TOKEN` env var and that token expires
- **Fixed**: Prompt-input undo (`Ctrl+_`) doing nothing immediately after typing, and skipping a state on each undo step
- **Fixed**: `NO_PROXY` not being respected for remote API requests when running under Bun
- **Fixed**: Bedrock application-inference-profile requests failing with 400 when backed by Opus 4.7 with thinking disabled

### v2.1.116 (2026-04-21)

> Regression fix release: ends the six-week Triple Harness Incident (Mar 4–Apr 20, 2026). Also: /resume up to 67% faster on large sessions, inline thinking progress spinner, sandbox security fix, many bug fixes.

- **Regression fix**: All three harness-level changes responsible for the six-week quality regression (effort defaults, thinking-budget clear, verbosity instruction) are reverted or fixed in this release — see [Triple Harness Incident](./known-issues.md#triple-harness-incident-effort-thinking-tokens-verbosity-mar-apr-2026) for the full timeline
- **Improved**: `/resume` is up to 67% faster on sessions 40MB+ and handles sessions with many dead-fork entries more efficiently
- **Improved**: Faster MCP startup when multiple stdio servers are configured; `resources/templates/list` is deferred to the first `@`-mention
- **Improved**: Smoother fullscreen scrolling in VS Code, Cursor, and Windsurf; `/terminal-setup` now configures the editor's scroll sensitivity
- **Improved**: Thinking spinner shows inline progress ("still thinking", "thinking more", "almost done thinking") replacing the separate hint row
- **Improved**: `/config` search now matches option values (e.g., searching "vim" finds the Editor mode setting)
- **Improved**: `/doctor` can now be opened while Claude is responding, without waiting for the current turn to finish
- **Improved**: `/reload-plugins` and background plugin auto-update now auto-install missing dependencies from already-added marketplaces
- **Improved**: Bash tool surfaces a hint when `gh` commands hit GitHub's API rate limit, so agents can back off instead of retrying
- **Improved**: Usage tab shows 5-hour and weekly usage immediately and no longer fails when the usage endpoint is rate-limited
- **Improved**: Agent frontmatter `hooks:` now fire when running as a main-thread agent via `--agent`
- **Improved**: Slash command menu shows "No commands match" when filter has zero results, instead of disappearing
- **Security**: Sandbox auto-allow no longer bypasses the dangerous-path safety check for `rm`/`rmdir` targeting `/`, `$HOME`, or other critical system directories
- **Fixed**: Devanagari and other Indic scripts rendering with broken column alignment in the terminal UI
- **Fixed**: `Ctrl+-` not triggering undo in terminals using the Kitty keyboard protocol (iTerm2, Ghostty, kitty, WezTerm, Windows Terminal)
- **Fixed**: `Cmd+Left/Right` not jumping to line start/end in Kitty protocol terminals (Warp fullscreen, kitty, Ghostty, WezTerm)
- **Fixed**: `Ctrl+Z` hanging the terminal when Claude Code is launched via a wrapper process (e.g., `npx`, `bun run`)
- **Fixed**: Scrollback duplication in inline mode where resizing the terminal or large output bursts would repeat earlier conversation history
- **Fixed**: Modal search dialogs overflowing the screen at short terminal heights, hiding the search box and keyboard hints
- **Fixed**: Scattered blank cells and disappearing composer chrome in the VS Code integrated terminal during scrolling
- **Fixed**: Intermittent API 400 error related to cache control TTL ordering that could occur when a parallel request completed during request setup
- **Fixed**: `/branch` rejecting conversations with transcripts larger than 50MB
- **Fixed**: `/resume` silently showing an empty conversation on large session files instead of reporting the load error
- **Fixed**: `/plugin` Installed tab showing the same item twice when it appears under Needs attention or Favorites
- **Fixed**: `/update` and `/tui` not working after entering a worktree mid-session

---

### v2.1.114 (2026-04-18)

> Fixed crash in permission dialog when an agent teams teammate requested tool permission.

- **Fixed**: Crash in the permission dialog when an agent teams teammate requested tool permission

---

### v2.1.113 (2026-04-18)

> Native Claude Code binary spawning, sandbox.network.deniedDomains setting, security hardening, many bug fixes.

- **New**: CLI now spawns a native Claude Code binary via a per-platform optional dependency instead of bundled JavaScript
- **New**: `sandbox.network.deniedDomains` setting — block specific domains even when a broader `allowedDomains` wildcard would otherwise permit them
- **Improved**: Fullscreen mode — `Shift+↑/↓` now scrolls the viewport when extending a selection past the visible edge
- **Improved**: `Ctrl+A` and `Ctrl+E` now move to the start/end of the current logical line in multiline input (readline behavior)
- **Improved**: Windows: `Ctrl+Backspace` now deletes the previous word
- **Improved**: Long URLs in responses and bash output stay clickable when they wrap across lines (in terminals with OSC 8 hyperlinks)
- **Improved**: `/loop` — pressing Esc now cancels pending wakeups; wakeups display as "Claude resuming /loop wakeup" for clarity
- **Improved**: `/extra-usage` now works from Remote Control (mobile/web) clients
- **Improved**: Remote Control clients can now query `@`-file autocomplete suggestions
- **Improved**: `/ultrareview` — faster launch with parallelized checks, diffstat in the launch dialog, animated launching state
- **Improved**: Subagents that stall mid-stream now fail with a clear error after 10 minutes instead of hanging silently
- **Improved**: Bash tool — multi-line commands whose first line is a comment now show the full command in the transcript, closing a UI-spoofing vector
- **Improved**: Running `cd <current-directory> && git …` no longer triggers a permission prompt when the `cd` is a no-op
- **Security**: On macOS, `/private/{etc,var,tmp,home}` paths are now treated as dangerous removal targets under `Bash(rm:*)` allow rules
- **Security**: Bash deny rules now match commands wrapped in `env`/`sudo`/`watch`/`ionice`/`setsid` and similar exec wrappers
- **Security**: `Bash(find:*)` allow rules no longer auto-approve `find -exec`/`-delete`
- **Fixed**: MCP concurrent-call timeout handling where a message for one tool call could silently disarm another call's watchdog
- **Fixed**: Cmd-backspace / `Ctrl+U` to once again delete from the cursor to the start of the line
- **Fixed**: Markdown tables breaking when a cell contains an inline code span with a pipe character
- **Fixed**: Session recap auto-firing while composing unsent text in the prompt
- **Fixed**: `/copy` "Full response" not aligning markdown table columns for pasting into GitHub, Notion, or Slack
- **Fixed**: Messages typed while viewing a running subagent hidden from its transcript and misattributed to the parent AI
- **Fixed**: `Bash dangerouslyDisableSandbox` running commands outside the sandbox without a permission prompt
- **Fixed**: `/effort auto` confirmation now says "Effort level set to max" to match the status bar label
- **Fixed**: The "copied N chars" toast overcounting emoji and other multi-code-unit characters
- **Fixed**: `/insights` crashing with `EBUSY` on Windows
- **Fixed**: Exit confirmation dialog mislabeling one-shot scheduled tasks as recurring — now shows a countdown
- **Fixed**: Slash/@ completion menu not sitting flush against the prompt border in fullscreen mode
- **Fixed**: `CLAUDE_CODE_EXTRA_BODY output_config.effort` causing 400 errors on subagent calls to models without effort support and on Vertex AI
- **Fixed**: Prompt cursor disappearing when `NO_COLOR` is set
- **Fixed**: `ToolSearch` ranking so pasted MCP tool names surface the actual tool instead of description-matching siblings
- **Fixed**: Compacting a resumed long-context session failing with "Extra usage is required for long context requests"
- **Fixed**: `plugin install` succeeding when a dependency version conflicts with an already-installed plugin — now reports `range-conflict`
- **Fixed**: "Refine with Ultraplan" not showing the remote session URL in the transcript
- **Fixed**: SDK image content blocks that fail to process crashing the session — now degrade to a text placeholder
- **Fixed**: Remote Control sessions not streaming subagent transcripts
- **Fixed**: Remote Control sessions not being archived when Claude Code exits
- **Fixed**: `thinking.type.enabled is not supported` 400 error when using Opus 4.7 via a Bedrock Application Inference Profile ARN

---

### v2.1.111 (2026-04-16)

> Claude Opus 4.7 xhigh effort level, /ultrareview cloud code review, /less-permission-prompts skill, Auto mode for Max subscribers.

- **New**: Claude Opus 4.7 `xhigh` effort level — between `high` and `max`; available via `/effort`, `--effort`, and the model picker; other models fall back to `high`
- **New**: Auto mode for Max subscribers on Opus 4.7 — no longer requires `--enable-auto-mode`
- **New**: `/ultrareview` skill — runs comprehensive code review in the cloud using parallel multi-agent analysis; invoke without arguments for current branch, or `/ultrareview <PR#>` for a specific GitHub PR
- **New**: `/less-permission-prompts` skill — scans transcripts for common read-only Bash and MCP tool calls, proposes a prioritized allowlist for `.claude/settings.json`
- **New**: "Auto (match terminal)" theme option — follows your terminal's dark/light mode; selectable via `/theme`
- **New**: `/effort` opens an interactive slider when called without arguments; arrow-key navigation + Enter to confirm
- **Improved**: Plan files now named after your prompt (e.g. `fix-auth-race-snug-otter.md`) instead of purely random words
- **Improved**: Read-only bash commands with glob patterns (e.g. `ls *.ts`) and commands starting with `cd <project-dir> &&` no longer trigger a permission prompt
- **Improved**: `/setup-vertex` and `/setup-bedrock` show the actual `settings.json` path when `CLAUDE_CONFIG_DIR` is set, seed model candidates from existing pins on re-run, offer a "with 1M context" option
- **Improved**: `/skills` menu now supports sorting by estimated token count — press `t` to toggle
- **Improved**: `Ctrl+U` clears the entire input buffer (`Ctrl+Y` restores); `Ctrl+L` forces full screen redraw
- **Improved**: Typo suggestions for near-miss `claude <word>` invocations (e.g. `claude udpate` → "Did you mean `claude update`?")
- **Improved**: Headless `--output-format stream-json` includes `plugin_errors` on the init event; `OTEL_LOG_RAW_API_BODIES` env var emits full API bodies as OpenTelemetry log events
- **Fixed**: Terminal display tearing (random characters, drifting input) in iTerm2 + tmux setups when terminal notifications are sent
- **Fixed**: `@` file suggestions re-scanning entire project on every turn in non-git directories; only config files shown in freshly-initialized git repos with no tracked files
- **Fixed**: LSP diagnostics from before an edit appearing after it, causing model to re-read already-edited files
- **Fixed**: Tab-completing `/resume` immediately resuming an arbitrary titled session instead of showing the session picker
- **Fixed**: `/clear` dropping the session name set by `/rename`, causing statusline to lose `session_name`
- **Fixed**: Claude calling non-existent `commit` skill showing "Unknown skill: commit" for users without a custom `/commit` command
- **Fixed**: 429 rate-limit errors on Bedrock/Vertex/Foundry incorrectly referencing status.claude.com
- **Fixed**: Multiple additional issues — bare URLs unclickable when terminal wraps them across lines, feedback surveys appearing back-to-back, Windows `CLAUDE_ENV_FILE` and SessionStart hook env files now apply, drive-letter path permission rules correctly root-anchored
- **Fixed**: Plugin error handling improvements — dependency errors distinguish conflicting/invalid/overly complex version requirements; stale resolved versions after `plugin update`; `plugin install` recovers from interrupted installs
- **Reverted**: v2.1.110 cap on non-streaming fallback retries — it traded long waits for more outright failures during API overload

---

### v2.1.110 (2026-04-16)

> /tui fullscreen command, push notification tool, --resume resurrects scheduled tasks, /focus command, 30+ bug fixes.

- **New**: `/tui` command and `tui` setting — run `/tui fullscreen` to switch to flicker-free rendering within the same conversation
- **New**: Push notification tool (`PushNotification`) — Claude can send mobile push notifications when Remote Control and "Push when Claude decides" config are enabled
- **New**: `--resume`/`--continue` now resurrects unexpired scheduled tasks
- **New**: `/focus` command — focus view is now toggled separately; `Ctrl+O` reverts to toggling between normal and verbose transcript only
- **New**: `autoScrollEnabled` config — disable conversation auto-scroll in fullscreen mode
- **New**: Option to show Claude's last response as commented context in the `Ctrl+G` external editor (enable via `/config`)
- **Improved**: `/plugin` Installed tab — items needing attention and favorites appear at the top; disabled items hidden behind a fold; `f` to favorite
- **Improved**: `/doctor` warns when an MCP server is defined in multiple config scopes with different endpoints
- **Improved**: Session recap now enabled for users with telemetry disabled (Bedrock, Vertex, Foundry, `DISABLE_TELEMETRY`); opt out via `/config` or `CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0`
- **Improved**: Write tool informs the model when you edit proposed content in the IDE diff before accepting; Bash tool enforces documented maximum timeout
- **Fixed**: MCP tool calls hanging indefinitely when server connection drops mid-response on SSE/HTTP transports
- **Fixed**: Non-streaming fallback retries causing multi-minute hangs when API is unreachable
- **Fixed**: `PermissionRequest` hooks returning `updatedInput` not being re-checked against `permissions.deny` rules; `setMode:'bypassPermissions'` now respects `disableBypassPermissionsMode`
- **Fixed**: `PreToolUse` hook `additionalContext` dropped when the tool call fails
- **Fixed**: stdio MCP servers that print stray non-JSON lines to stdout being disconnected on first stray line (regression in 2.1.105)
- **Fixed**: Headless/SDK auto-title firing an extra Haiku request when `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` is set
- **Fixed**: Garbled startup rendering in macOS Terminal.app and other terminals without synchronized output support
- **Security**: Hardened "Open in editor" actions against command injection from untrusted filenames
- **Fixed**: Multiple additional issues — high CPU usage in fullscreen, dropped keystrokes after relaunch, `/skills` menu not scrolling, Remote Control session renames not persisting, session cleanup not removing subagent transcripts

---

### v2.1.109 (2026-04-15)

> Improved extended-thinking indicator with a rotating progress hint.

- **Improved**: Extended-thinking indicator now shows a rotating progress hint for better visibility during long thinking phases

---

### v2.1.108 (2026-04-15)

> 1-hour prompt cache TTL option, /recap session context feature, built-in slash commands discoverable via Skill tool, /undo alias for /rewind.

- **New**: `ENABLE_PROMPT_CACHING_1H` env var — opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK` deprecated but still honored); `FORCE_PROMPT_CACHING_5M` to force 5-minute TTL
- **New**: `/recap` feature — provides context when returning to a session after a break; configurable in `/config`; force with `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` if telemetry disabled
- **New**: Model can now discover and invoke built-in slash commands like `/init`, `/review`, `/security-review` via the Skill tool
- **New**: `/undo` is now an alias for `/rewind`
- **New**: "verbose" indicator when viewing the detailed transcript (`Ctrl+O`)
- **New**: Startup warning when prompt caching is disabled via `DISABLE_PROMPT_CACHING*` environment variables
- **Improved**: `/model` now warns before switching models mid-conversation (next response re-reads full history uncached)
- **Improved**: `/resume` picker defaults to sessions from the current directory; press `Ctrl+A` to show all projects
- **Improved**: Error messages distinguish server rate limits from plan usage limits; 5xx/529 errors link to status.claude.com; unknown slash commands suggest closest match
- **Improved**: Memory footprint for file reads, edits, and syntax highlighting reduced by loading language grammars on demand
- **Fixed**: Paste not working in the `/login` code prompt (regression in 2.1.105)
- **Fixed**: `DISABLE_TELEMETRY` subscribers falling back to 5-minute prompt cache TTL instead of 1 hour
- **Fixed**: Bash tool producing no output when `CLAUDE_ENV_FILE` (e.g. `~/.zprofile`) ends with a `#` comment line
- **Fixed**: `--resume <session-id>` losing session's custom name and color set via `/rename`
- **Fixed**: Diacritical marks (accents, umlauts, cedillas) being dropped from responses when `language` setting is configured
- **Fixed**: `--teleport` and `--resume <id>` precondition errors (dirty git tree, session not found) exiting silently

---

### v2.1.107 (2026-04-14)

> Show thinking hints sooner during long operations.

- **Improved**: Thinking hints now appear sooner during long operations for better real-time feedback

---

### v2.1.105 (2026-04-13)

> EnterWorktree path parameter, PreCompact hook blocking, plugin background monitors, /proactive alias, WebFetch strips CSS/JS, /doctor with status icons and f-to-fix, and multiple bug fixes.

- **New**: `path` parameter on `EnterWorktree` tool — switch into an existing worktree of the current repository
- **New**: PreCompact hook support — hooks can block compaction by exiting with code 2 or returning `{"decision":"block"}`
- **New**: Background monitor support for plugins via a top-level `monitors` manifest key — auto-arms at session start or on skill invoke
- **New**: `/proactive` is now an alias for `/loop`
- **Improved**: Stalled API streams now abort after 5 minutes of no data and retry non-streaming instead of hanging indefinitely
- **Improved**: Network error messages show retry immediately instead of a silent spinner
- **Improved**: `/doctor` layout with status icons; press `f` to have Claude fix reported issues
- **Improved**: `WebFetch` strips `<style>` and `<script>` contents — CSS-heavy pages no longer exhaust content budget before reaching actual text
- **Improved**: Skill description listing cap raised from 250 to 1,536 characters; startup warning when descriptions are truncated
- **Improved**: Stale agent worktree cleanup now removes worktrees whose PR was squash-merged
- **Fixed**: Images attached to queued messages (sent while Claude is working) being dropped
- **Fixed**: Screen going blank when prompt input wraps to second line in long conversations
- **Fixed**: `/model` picker on Bedrock in non-US regions persisting invalid `us.*` model IDs when inference profile discovery is in-flight
- **Fixed**: 429 rate-limit errors showing raw JSON dump instead of clean message for API-key, Bedrock, and Vertex users
- **Fixed**: MCP tools missing on first turn of headless/remote-trigger sessions when MCP servers connect asynchronously
- **Fixed**: Various crash and `/resume` failures including malformed text blocks and `/help` layout at short terminal heights
- **Fixed**: `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` in one project settings permanently disabling usage metrics for all projects

---

### v2.1.101 (2026-04-10)

> /team-onboarding command for teammate ramp-up, OS CA certificate store trusted by default for enterprise TLS proxies, /ultraplan auto-creates cloud environment, and 40+ bug fixes including --resume context loss, Bedrock SigV4 auth, sub-agent worktree file access, and Grep ENOENT self-heal.

- **New**: `/team-onboarding` command — generates a teammate ramp-up guide from your local Claude Code usage patterns
- **New**: OS CA certificate store is now trusted by default — enterprise TLS proxies work without extra config; set `CLAUDE_CODE_CERT_STORE=bundled` to revert to bundled CAs only
- **New**: `/ultraplan` and other remote-session features now auto-create a default cloud environment instead of requiring web setup first
- **Improved**: `claude -p --resume <name>` now accepts session titles set via `/rename` or `--name`
- **Improved**: Unrecognized hook event names in `settings.json` no longer cause the entire file to be ignored
- **Improved**: Rate-limit retry messages show which limit was hit and when it resets (instead of opaque countdown)
- **Improved**: Brief mode retries once when Claude responds with plain text instead of a structured message
- **Fixed**: `--resume`/`--continue` losing conversation context on large sessions when the loader anchored on a dead-end branch
- **Fixed**: Bedrock SigV4 authentication failing with 403 when `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper`, or `ANTHROPIC_CUSTOM_HEADERS` set an Authorization header
- **Fixed**: Sub-agents running in isolated worktrees denied Read/Edit access to files inside their own worktree
- **Fixed**: `RemoteTrigger` tool's `run` action sending an empty body and being rejected by the server
- **Fixed**: Grep tool ENOENT when the embedded ripgrep binary path becomes stale (VS Code extension auto-update, macOS App Translocation) — now falls back to system `rg` and self-heals mid-session
- **Fixed**: Hardcoded 5-minute request timeout aborting slow backends (local LLMs, extended thinking, slow gateways) regardless of `API_TIMEOUT_MS`
- **Fixed**: Command injection vulnerability in POSIX `which` fallback used by LSP binary detection
- **Fixed**: `permissions.deny` rules not overriding a PreToolUse hook's `permissionDecision: "ask"`
- **Fixed**: Memory leak where long sessions retained dozens of historical copies of the message list in the virtual scroller
- **Fixed**: `/btw` writing a full conversation copy to disk on every use

### v2.1.98 (2026-04-10)

> Vertex AI interactive setup wizard, Monitor tool for background script streaming, major Bash security hardening (8+ permission bypasses fixed), and subprocess PID namespace sandboxing.

- **New**: Interactive Vertex AI setup wizard from the login screen (select "3rd-party platform") — guides through GCP authentication, project and region configuration, credential verification, and model pinning
- **New**: Monitor tool for streaming events from background scripts
- **New**: `CLAUDE_CODE_PERFORCE_MODE` env var — Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting
- **New**: Subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set; `CLAUDE_CODE_SCRIPT_CAPS` env var to limit per-session script invocations
- **New**: `--exclude-dynamic-system-prompt-sections` flag in print mode for improved cross-user prompt caching
- **New**: W3C `TRACEPARENT` env var injected into Bash tool subprocesses when OTEL tracing is enabled
- **New**: LSP: Claude Code now identifies itself via `clientInfo` in the initialize request
- **Security (Bash)**: Fixed permission bypass where backslash-escaped flags could be auto-allowed as read-only and execute arbitrary code
- **Security (Bash)**: Fixed compound commands bypassing forced permission prompts in auto and bypass-permissions modes
- **Security (Bash)**: Fixed read-only commands with unknown env-var prefixes not prompting (only `LANG`, `TZ`, `NO_COLOR`, etc. are now safe-listed)
- **Security (Bash)**: Fixed `/dev/tcp/...` and `/dev/udp/...` redirects not prompting
- **Security (Bash)**: Fixed `grep -f FILE` / `rg -f FILE` not prompting when reading pattern files outside the working directory
- **Fixed**: Stalled streaming responses timing out instead of falling back to non-streaming mode
- **Fixed**: `--dangerously-skip-permissions` silently downgraded to accept-edits mode after approving a protected-path Bash write
- **Fixed**: Managed-settings allow rules remaining active after admin removal until process restart
- **Fixed**: `permissions.additionalDirectories` changes not applying mid-session; `--add-dir` access unaffected by removal
- **Fixed**: MCP OAuth `oauth.authServerMetadataUrl` not honored on token refresh — fixes ADFS and similar IdPs
- **Fixed**: 429 retries burning all attempts in ~13s with small `Retry-After` — exponential backoff now applies as minimum
- **Fixed**: Capital letters dropped to lowercase in xterm/VS Code integrated terminal with kitty keyboard protocol active
- **Fixed**: macOS text replacements deleting trigger word instead of inserting substitution
- **Fixed**: Agent team members not inheriting leader's permission mode with `--dangerously-skip-permissions`
- **Fixed**: `CLAUDE_CODE_MAX_CONTEXT_TOKENS` now honors `DISABLE_COMPACT`
- **Improved**: `/agents` with tabbed layout — Running tab shows live subagents, Library tab adds Run and View actions
- **Improved**: `/resume` filter hint labels; project/worktree/branch names in filter indicator
- **Improved**: Accept Edits mode auto-approves filesystem commands prefixed with safe env vars or process wrappers
- **Improved**: Write tool diff computation 60% faster on files with tabs/`&`/`$`

### v2.1.97 (2026-04-09)

> Major bug-fix release with 30+ fixes across NO_FLICKER mode, /resume, permissions, and MCP — plus focus view toggle and status line enhancements.

- **New**: Focus view toggle (`Ctrl+O`) in NO_FLICKER mode — shows prompt, one-line tool summary with edit diffstats, and final response
- **New**: `refreshInterval` status line setting — re-runs the status line command every N seconds
- **New**: `workspace.git_worktree` field added to status line JSON input, populated when inside a linked git worktree
- **New**: `● N running` indicator in `/agents` next to agent types with live subagent instances
- **New**: Syntax highlighting for Cedar policy files (`.cedar`, `.cedarpolicy`)
- **Fixed (permissions)**: `--dangerously-skip-permissions` silently downgraded to accept-edits mode after approving a write to a protected path
- **Fixed (permissions)**: Permission rules with names matching JS prototype properties (e.g. `toString`) causing `settings.json` to be silently ignored
- **Fixed (permissions)**: Managed-settings allow rules remaining active after admin removal until process restart
- **Fixed (permissions)**: `permissions.additionalDirectories` changes not applying mid-session; removing a dir now correctly revokes access without affecting `--add-dir` entries
- **Fixed (MCP)**: HTTP/SSE connections accumulating ~50 MB/hr of unreleased buffers on reconnect
- **Fixed (MCP)**: OAuth `oauth.authServerMetadataUrl` not honored on token refresh after restart — fixes ADFS and similar IdPs
- **Fixed (rate limits)**: 429 retries burning all attempts in ~13 s when server returns small `Retry-After` — exponential backoff now applies as minimum
- **Fixed (rate limits)**: Rate-limit upgrade options disappearing after context compaction
- **Fixed (/resume)**: 6 fixes — `--resume <name>` opened uneditable, Ctrl+A wiped search, empty list swallowed navigation, task-status replaced conversation summary, cross-project staleness, file-edit diffs disappearing for files >10 KB
- **Fixed (transcript)**: `--resume` cache misses from attachment messages not saved; messages typed during Claude's response not persisted
- **Fixed (hooks)**: `Stop`/`SubagentStop` hooks failing on long sessions; hook evaluator API errors showing "JSON validation failed" instead of actual message
- **Fixed (subagents)**: Worktree isolation / `cwd:` override leaking working directory back to parent Bash tool
- **Fixed (compaction)**: Duplicate multi-MB subagent transcript files on prompt-too-long retries
- **Fixed (plugins)**: `claude plugin update` reporting "already at latest" for git-based marketplace plugins with newer remote commits; slash command picker breaking when plugin frontmatter `name` is a YAML boolean keyword
- **Fixed (NO_FLICKER, 15 fixes)**: Wrapped URL spaces, zellij scroll artifacts, MCP result hover crash, API retry memory leak, slow Windows Terminal mouse-wheel, custom status line hidden on terminals <24 rows, Shift+Enter/Alt+arrow in Warp, CJK text garbled on Windows copy, footer indicator wrapping, blockquote left bar across wrapped lines, transient context-low notification
- **Fixed (Bedrock)**: SigV4 auth failing when `AWS_BEARER_TOKEN_BEDROCK` / `ANTHROPIC_BEDROCK_BASE_URL` set to empty strings (as GitHub Actions does for unset inputs)
- **Improved**: Accept Edits mode auto-approves filesystem commands prefixed with safe env vars or process wrappers (e.g. `LANG=C rm foo`, `timeout 5 mkdir out`)
- **Improved**: Auto mode and bypass-permissions mode auto-approve sandbox network access prompts; `sandbox.network.allowMachLookup` now takes effect on macOS
- **Improved**: Pasted and attached images compressed to same token budget as Read tool images
- **Improved**: Slash command and `@`-mention completion now triggers after CJK sentence punctuation — Japanese/Chinese input no longer requires a space before `/` or `@`
- **Improved**: Bridge sessions show local git repo, branch, and working directory on the claude.ai session card
- **Improved**: Session transcript size reduced by skipping empty hook entries and capping stored pre-edit file copies; per-block entries now carry final token usage
- **Updated**: `/claude-api` skill covers Managed Agents alongside the Claude API

---

### v2.1.96 (2026-04-08)

> Hotfix release addressing a Bedrock authentication regression introduced in v2.1.94.

- **Fixed**: Bedrock requests failing with `403 "Authorization header is missing"` when using `AWS_BEARER_TOKEN_BEDROCK` or `CLAUDE_CODE_SKIP_BEDROCK_AUTH` (regression from v2.1.94)

---

### v2.1.94 (2026-04-07)

> Feature release adding Amazon Bedrock Mantle support, raising the default effort level for professional users, and improving plugin skill naming.

- **New**: Amazon Bedrock powered by Mantle support — set `CLAUDE_CODE_USE_MANTLE=1`
- **New**: Default effort level changed from medium to **high** for API-key, Bedrock/Vertex/Foundry, Team, and Enterprise users (control with `/effort`)
- **New**: Plugin skills declared via `"skills": ["./"]` now use frontmatter `name` instead of directory basename — stable naming across install methods
- **New**: Compact `Slacked #channel` header with clickable link for Slack MCP send-message tool calls
- **New**: `keep-coding-instructions` frontmatter field support for plugin output styles
- **New**: `hookSpecificOutput.sessionTitle` on `UserPromptSubmit` hooks for setting session title programmatically
- **Fixed**: Agents stuck after 429 rate-limit with long Retry-After — error surfaces immediately instead of silently waiting
- **Fixed**: Console login on macOS silently failing with "Not logged in" when login keychain is locked — error now surfaced with `claude doctor` fix guidance
- **Fixed**: Plugin skill hooks defined in YAML frontmatter being silently ignored
- **Fixed**: Scrollback showing duplicate diffs and blank pages in long-running sessions

---

### v2.1.92 (2026-04-04)

> Feature release adding interactive Bedrock wizard, fail-closed managed settings enforcement, and /cost per-model breakdown.

- **New**: Interactive Bedrock setup wizard from the login screen ("3rd-party platform") — step-by-step AWS auth, region config, credential verification, and model pinning
- **New**: `forceRemoteSettingsRefresh` policy setting — blocks CLI startup until managed settings are freshly fetched, exits with error if fetch fails (fail-closed enforcement)
- **New**: Per-model and cache-hit cost breakdown in `/cost` for subscription users
- **New**: `/release-notes` is now an interactive version picker
- **New**: Remote Control session names use hostname as default prefix (e.g. `myhost-graceful-unicorn`), overridable with `--remote-control-session-name-prefix`
- **New**: Pro users see a footer hint when returning after prompt cache expiry, estimating uncached tokens for next turn
- **Fixed**: Subagent spawning permanently failing with "Could not determine pane count" after tmux windows are killed or renumbered
- **Fixed**: API 400 error when extended thinking produced a whitespace-only text block alongside real content
- **Fixed**: Linux sandbox `apply-seccomp` helper now shipped in both npm and native builds — restores unix-socket blocking for sandboxed commands
- **Improved**: Write tool diff computation 60% faster for large files with tabs/`&`/`$`
- **Removed**: `/tag` command
- **Removed**: `/vim` command — toggle vim mode via `/config` → Editor mode

---

### v2.1.91 (2026-04-03)

> Maintenance release with MCP result size override, plugin executable support, and Edit tool token reduction.

- **New**: MCP tool result size override via `_meta["anthropic/maxResultSizeChars"]` annotation (up to 500K) — large DB schemas and API payloads pass through without truncation
- **New**: `disableSkillShellExecution` setting — disable inline shell execution in skills, slash commands, and plugin commands
- **New**: Plugins can ship executables under `bin/` for direct Bash tool invocation without full path
- **New**: Multi-line prompts now supported in `claude-cli://open?q=` deep links (`%0A` encoded newlines accepted)
- **Fixed**: `--resume` losing conversation history when async transcript writes fail silently
- **Fixed**: `cmd+delete` not deleting to start of line in iTerm2, Kitty, WezTerm, Ghostty, Windows Terminal
- **Fixed**: Plan mode in remote sessions losing track of plan file after container restart
- **Fixed**: JSON schema validation for `permissions.defaultMode: "auto"` in settings.json
- **Improved**: Edit tool uses shorter `old_string` anchors — reduces output tokens
- **Improved**: `/claude-api` skill guidance expanded with agent design patterns (tool surface decisions, context management, caching strategy)
- **Improved**: `stripAnsi` ~2x faster on Bun via `Bun.stripANSI`

---

### v2.1.90 (2026-04-02)

> Feature release adding `/powerup` interactive lessons, PowerShell tool hardening, and key performance/reliability fixes.

- **New**: `/powerup` command — interactive animated lessons teaching Claude Code features with live terminal demos
- **Fixed**: Infinite loop crashing sessions when rate-limit options dialog repeatedly auto-opened after hitting usage limit
- **Fixed**: `--resume` causing full prompt-cache miss on first request for users with deferred tools, MCP servers, or custom agents (regression since v2.1.69)
- **Fixed**: `PreToolUse` hooks that emit JSON to stdout and exit with code 2 not correctly blocking the tool call
- **Fixed**: Collapsed search/read summary badge appearing multiple times in fullscreen scrollback during CLAUDE.md auto-load
- **Fixed**: Auto mode not respecting explicit user boundaries ("don't push", "wait for X before Y")
- **Fixed**: Headers disappearing when scrolling `/model`, `/config`, and other selection screens
- **Hardened**: PowerShell tool permissions — trailing `&` background job bypass, `-ErrorAction Break` debugger hang, archive-extraction TOCTOU, parse-fail fallback deny-rule degradation
- **Improved**: SSE transport handles large streamed frames in linear time (was quadratic)
- **Improved**: Eliminated per-turn JSON.stringify of MCP tool schemas on cache-key lookup
- **Improved**: `/resume` all-projects view loads project sessions in parallel
- **Changed**: `--resume` picker no longer shows sessions created by `claude -p` or SDK invocations

---

### v2.1.89 (2026-04-01)

> Large bugfix + feature release with new hook types, headless workflow improvements, and notable behavior changes.

- **New**: `"defer"` permission decision for `PreToolUse` hooks — headless sessions can pause at a tool call and resume with `-p --resume` to re-evaluate
- **New**: `PermissionDenied` hook — fires after auto mode classifier denials; return `{retry: true}` to let the model retry with an alternative approach
- **New**: Named subagents now appear in `@` mention typeahead suggestions for easier invocation
- **New**: `CLAUDE_CODE_NO_FLICKER=1` env var to opt into flicker-free alt-screen rendering with virtualized scrollback
- **New**: `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode — skips MCP connection wait; `--mcp-config` servers bounded at 5s
- **New**: Auto mode denied commands now show a notification and appear in `/permissions` → Recent tab
- **Changed**: Thinking summaries are no longer generated by default in interactive sessions — add `showThinkingSummaries: true` to `settings.json` to restore
- **Improved**: `/env` now applies to PowerShell tool commands (previously only affected Bash)
- **Improved**: PowerShell tool prompt with version-appropriate syntax guidance (5.1 vs 7+)
- **Fixed**: `StructuredOutput` schema cache bug causing ~50% failure rate in workflows with multiple schemas
- **Fixed**: Edit/Write tools doubling CRLF on Windows and stripping Markdown hard line breaks (two trailing spaces)
- **Fixed**: Hooks `if` condition filtering not matching compound commands (`ls && git push`) or commands with env-var prefixes (`FOO=bar git push`)
- **Fixed**: Prompt cache misses in long sessions caused by tool schema bytes changing mid-session
- **Fixed**: Nested CLAUDE.md files being re-injected dozens of times in long sessions that read many files
- **Fixed**: Memory leaks: large JSON LRU cache key retention, LSP diagnostic data, StructuredOutput cache
- **Fixed**: Crashes: large file edits (>1 GiB), large session file removal (>50 MB), `--resume` with old tool results
- **Fixed**: Voice mode: macOS Apple Silicon microphone permission, Windows WebSocket 101 error, modifier-combo push-to-talk
- **Fixed**: `/stats` losing historical data beyond 30 days; `/stats` undercounting tokens from subagent/fork usage
- **Fixed**: Scrollback disappearing when scrolling up in long sessions; rendering artifacts on main-screen terminals
- **Fixed**: SDK error result messages (`error_during_execution`, `error_max_turns`) now correctly set `is_error: true`
- **Fixed**: PreToolUse/PostToolUse hooks not providing `file_path` as absolute path for Write/Edit/Read tools

> **Breaking**: Thinking summaries now off by default. Set `showThinkingSummaries: true` in settings.json to restore.

---

### v2.1.87 (2026-03-30)

- **Fixed**: Messages in Cowork Dispatch not getting delivered

---

### v2.1.86 (2026-03-28)

- **New**: `X-Claude-Code-Session-Id` header added to API requests — proxies can aggregate requests by session without parsing the body
- **New**: `.jj` and `.sl` added to VCS directory exclusion lists so Grep and file autocomplete don't descend into Jujutsu or Sapling metadata
- **Improved**: Reduced token overhead when mentioning files with `@` — raw string content no longer JSON-escaped
- **Improved**: Better prompt cache hit rate for Bedrock, Vertex, and Foundry users by removing dynamic content from tool descriptions
- **Improved**: Read tool now uses compact line-number format and deduplicates unchanged re-reads, reducing token usage
- **Improved**: Skill descriptions in `/skills` listing capped at 250 characters to reduce context usage; `/skills` menu now sorted alphabetically
- **Improved**: Reduced startup event-loop stalls when many claude.ai MCP connectors are configured (macOS keychain cache extended from 5s to 30s)
- **Fixed**: Official marketplace plugin scripts failing with "Permission denied" on macOS/Linux since v2.1.83
- **Fixed**: `--resume` failing with "tool_use ids were found without tool_result blocks" on sessions created before v2.1.85
- **Fixed**: Write/Edit/Read failing on files outside the project root (e.g., `~/.claude/CLAUDE.md`) when conditional skills or rules are configured
- **Fixed**: Unnecessary config disk writes on every skill invocation — could cause performance issues and config corruption on Windows
- **Fixed**: Potential out-of-memory crash when using `/feedback` on very long sessions with large transcript files
- **Fixed**: `--bare` mode dropping MCP tools in interactive sessions and silently discarding messages enqueued mid-turn
- **Fixed**: `c` shortcut copying only ~20 characters of the OAuth login URL instead of the full URL
- **Fixed**: Masked input (e.g., OAuth code paste) leaking the start of the token when wrapping across multiple lines on narrow terminals
- **Fixed**: Statusline showing another session's model when running multiple Claude Code instances and using `/model`
- **Fixed**: Scroll not following new messages after wheel scroll or click-to-select at bottom of a long conversation
- **Fixed**: `/plugin` uninstall dialog: pressing `n` now correctly uninstalls while preserving the plugin's data directory
- **Fixed**: Regression where pressing Enter after clicking could leave the transcript blank until the response arrived
- **Fixed**: `ultrathink` hint lingering after deleting the keyword
- **Fixed**: Memory growth in long sessions from markdown/highlight render caches retaining full content strings
- **Fixed (VSCode)**: Extension incorrectly showing "Not responding" during long-running operations
- **Fixed (VSCode)**: Extension defaulting Max plan users to Sonnet after OAuth token refresh (8 hours after login)

### v2.1.85 (2026-03-27)

- **New**: Conditional `if` field for hooks — filter when hooks run using permission rule syntax (e.g., `Bash(git *)`) to reduce unnecessary process spawning overhead
- **New**: `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` env vars for MCP `headersHelper` scripts, allowing one helper script to serve multiple MCP servers
- **New**: PreToolUse hooks can now satisfy `AskUserQuestion` by returning `updatedInput` alongside `permissionDecision: "allow"` — enables headless integrations to collect answers via their own UI
- **New**: Timestamp markers in transcripts when scheduled tasks (`/loop`, `CronCreate`) fire
- **New**: Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters with a "scroll to review" warning for long pre-filled prompts
- **New**: MCP OAuth now follows RFC 9728 Protected Resource Metadata discovery to find the authorization server
- **New**: Plugins blocked by organization policy (`managed-settings.json`) are now hidden from marketplace views and cannot be installed/enabled
- **New**: `tool_parameters` in OpenTelemetry `tool_result` events are now gated behind `OTEL_LOG_TOOL_DETAILS=1`
- **Improved**: Scroll performance with large transcripts — WASM yoga-layout replaced with pure TypeScript implementation
- **Improved**: `@`-mention file autocomplete performance on large repositories
- **Improved**: PowerShell dangerous command detection
- **Fixed**: `/compact` failing with "context exceeded" when the conversation itself was too large for the compact request to fit
- **Fixed**: `deniedMcpServers` setting not blocking claude.ai MCP servers
- **Fixed**: Terminal left in enhanced keyboard mode after exit in Ghostty, Kitty, WezTerm — Ctrl+C and Ctrl+D now work correctly after quitting
- **Fixed**: `--worktree` exiting with an error in non-git repositories before the `WorktreeCreate` hook could run
- **Fixed**: MCP step-up authorization failing when a refresh token exists (servers requesting elevated scopes via `403 insufficient_scope`)
- **Fixed**: Prompts getting stuck in queue after running certain slash commands (up-arrow unable to retrieve them)
- **Fixed**: Raw key sequences appearing in prompt when running over SSH or in VS Code integrated terminal
- **Fixed**: `shift+enter` and `meta+enter` being intercepted by typeahead suggestions instead of inserting newlines
- **Fixed**: Remote Control session status stuck on "Requires Action" after a permission is resolved
- **Fixed**: Memory leak in remote sessions when a streaming response is interrupted
- **Fixed**: Python Agent SDK: `type:'sdk'` MCP servers passed via `--mcp-config` no longer dropped during startup
- **Fixed**: Crash when `OTEL_LOGS_EXPORTER`, `OTEL_METRICS_EXPORTER`, or `OTEL_TRACES_EXPORTER` is set to `none`
- **Fixed**: Diff syntax highlighting not working in non-native builds
- **Fixed**: Stale content bleeding through when scrolling up during streaming

### v2.1.84 (2026-03-26)

- **New**: PowerShell tool for Windows (opt-in preview) — direct PowerShell access alongside Bash tool. Learn more at https://code.claude.com/docs/en/tools-reference#powershell-tool
- **New**: `TaskCreated` hook fires when a task is created via `TaskCreate`
- **New**: `WorktreeCreate` hook now supports `type: "http"` — return the created worktree path via `hookSpecificOutput.worktreePath` in the response JSON
- **New**: `allowedChannelPlugins` managed setting for team/enterprise admins to define a channel plugin allowlist
- **New**: `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override effort/thinking capability detection for pinned models on Bedrock, Vertex, Foundry; `_MODEL_NAME`/`_DESCRIPTION` to customize the `/model` picker label
- **New**: `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)
- **New**: Idle-return prompt nudging users back after 75+ minutes to `/clear`, reducing unnecessary token re-caching on stale sessions
- **New**: Deep links (`claude-cli://`) now open in your preferred terminal instead of whichever terminal is detected first
- **New**: `x-client-request-id` header added to API requests for debugging timeouts
- **New**: Rules and skills `paths:` frontmatter now accepts a YAML list of globs
- **New**: MCP tool descriptions and server instructions capped at 2KB to prevent OpenAPI-generated servers from bloating context
- **New**: `ANTHROPIC_CUSTOM_MODEL_OPTION` env var to add a custom entry to the `/model` picker
- **New**: Managed settings can now be set via macOS plist or Windows Registry
- **Improved**: Global system-prompt caching now works when `ToolSearch` is enabled, including for users with many MCP tools
- **Improved**: Better dangerous-removal detection for Windows drive roots (`C:\`, `C:\Windows`, etc.)
- **Improved**: Interactive startup ~30ms faster (parallel `setup()` with slash command/agent loading)
- **Improved**: Stats screenshot (Ctrl+S in `/stats`) now works in all builds and is 16x faster
- **Improved**: p90 prompt cache hit rate improved
- **Fixed**: `ANTHROPIC_BETAS` environment variable being silently ignored when using Haiku models
- **Fixed**: Startup performance issue on partial clone repositories (Scalar/GVFS) that triggered mass blob downloads
- **Fixed**: Spurious "Not logged in" errors on macOS caused by transient keychain read failures
- **Fixed**: Cold-start race where core tools could be deferred without their bypass active (Edit/Write failing with InputValidationError)
- **Fixed**: Native terminal cursor not tracking input caret (IME composition for CJK now renders inline)
- **Fixed**: Workflow subagents failing with API 400 when outer session uses `--json-schema` and subagent also specifies a schema
- **Fixed**: Hang when generating attachment snippets for large edited files; MCP tool/resource cache leak on reconnect
- **Fixed**: Voice push-to-talk leaking characters into text input; transcripts now insert at correct position
- **Fixed**: `Ctrl+U` (kill-to-line-start) being a no-op at line boundaries in multiline input
- **Fixed**: Null-unbinding a default chord binding still entering chord-wait mode instead of freeing the prefix key
- **Changed**: Issue/PR references only become clickable links when written as `owner/repo#123` — bare `#123` no longer auto-linked
- **Changed**: Slash commands unavailable for current auth setup (`/voice`, `/mobile`, `/chrome`, `/upgrade`, etc.) are now hidden instead of shown
- **VSCode**: Added rate limit warning banner with usage percentage and reset time
- **VSCode**: Fixed Windows PATH inheritance for Bash tool regression (regression from v2.1.78 fix)

### v2.1.83 (2026-03-25)

- **New**: `managed-settings.d/` drop-in directory alongside `managed-settings.json` — separate teams can deploy independent policy fragments that merge alphabetically
- **New**: `CwdChanged` and `FileChanged` hook events for reactive environment management (e.g., direnv, auto-toolchain switching)
- **New**: `sandbox.failIfUnavailable` setting — exits with an error when sandbox is enabled but cannot start, instead of running unsandboxed
- **New**: `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol handler registration
- **New**: `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` strips Anthropic and cloud provider credentials from Bash tool, hooks, and MCP stdio server subprocess environments
- **New**: Transcript search — press `/` in transcript mode (Ctrl+O) to search, `n`/`N` to step through matches
- **New**: `Ctrl+X Ctrl+E` as an alias for opening the external editor (readline-native binding; `Ctrl+G` still works)
- **New**: Pasted images now insert an `[Image #N]` chip at cursor for positional referencing in prompts
- **New**: Agents can declare `initialPrompt` in frontmatter to auto-submit a first turn
- **New**: `chat:killAgents` and `chat:fastMode` are now rebindable via `~/.claude/keybindings.json`
- **Security**: Fixed `--mcp-config` CLI flag bypassing `allowedMcpServers`/`deniedMcpServers` managed policy enforcement
- **Fixed**: Claude Code hanging on exit on macOS
- **Fixed**: Screen flashing blank after being idle for a few seconds
- **Fixed**: Mouse tracking escape sequences leaking to shell prompt after exit
- **Fixed**: Background subagents becoming invisible after context compaction (could cause duplicate agents)
- **Fixed**: `--mcp-config` CLI flag bypassing `allowedMcpServers`/`deniedMcpServers` managed policy
- **Fixed**: Native modules not loading on Amazon Linux 2 and glibc 2.26 systems; Linux sandbox failing with "ripgrep not found"
- **Fixed**: Sessions with `saved_hook_context` causing startup performance issues
- **Fixed**: Conditional `.claude/rules/*.md` and nested CLAUDE.md files not loading in print mode
- **Fixed**: Agents from `.claude/agents/` not discovered in git worktrees (now loads from main repo)
- **Improved**: `WebFetch` identifies as `Claude-User` in requests; binary content (PDFs, audio) saved to disk with correct extension
- **Improved**: Reduced scrollback resets from once per turn to once per ~50 messages
- **Improved**: Increased non-streaming fallback token cap (21k → 64k) and timeout (120s → 300s)
- **Changed**: "Stop all background agents" keybinding moved from `Ctrl+F` to `Ctrl+X Ctrl+K`

### v2.1.81 (2026-03-22)

- **New**: `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
- **New**: `--channels` permission relay — channel servers that declare the permission capability can now forward tool approval prompts to your phone
- **Changed**: Plan mode hides the "clear context" option by default (restore with `"showClearContextOnPlanAccept": true` in settings)
- **Improved**: MCP read/search tool calls collapse into a single "Queried {server}" line (expand with Ctrl+O)
- **Improved**: `!` bash mode discoverability — Claude now suggests it when you need to run an interactive command
- **Improved**: Plugin freshness — ref-tracked plugins re-clone on every load to pick up upstream changes
- **Improved**: Remote Control session titles refresh after your third message; `/rename` now syncs title for RC sessions
- **Improved**: MCP OAuth updated to support Client ID Metadata Document (CIMD / SEP-991) for servers without Dynamic Client Registration
- **Fixed**: Resuming a worktree session now switches back to that worktree automatically
- **Fixed**: Multiple concurrent sessions requiring repeated re-authentication when one session refreshes its OAuth token
- **Fixed**: Voice mode silently swallowing retry failures with misleading "check your network" message; voice audio not recovering when server silently drops WebSocket
- **Fixed**: `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` not suppressing the structured-outputs beta header (caused 400 errors on Vertex/Bedrock proxies)
- **Fixed**: Race condition where background agent task output could hang indefinitely when task completed between polling intervals
- **Fixed**: `/btw` not including pasted text when used during an active response
- **Fixed**: Plugin hooks blocking prompt submission when plugin directory is deleted mid-session
- **Fixed**: Remote Control `/exit` not reliably archiving the session
- **Fixed**: Node.js 18 crash
- **Fixed**: Unnecessary permission prompts for Bash commands containing dashes in strings
- **Disabled**: Line-by-line response streaming on Windows (including WSL in Windows Terminal) due to rendering issues
- **VSCode**: Fixed Windows PATH inheritance for Bash tool when using Git Bash (regression in v2.1.78)

### v2.1.80 (2026-03-20)

- **New**: `rate_limits` field in statusline scripts for displaying Claude.ai rate limit usage (5-hour and 7-day windows with `used_percentage` and `resets_at`)
- **New**: `source: 'settings'` plugin marketplace source — declare plugin entries inline in `settings.json`
- **New**: CLI tool usage detection to plugin tips, in addition to file pattern matching
- **New**: `effort` frontmatter support for skills and slash commands to override the model effort level when invoked
- **New**: `--channels` (research preview) — allow MCP servers to push messages into your session
- **Fixed**: `--resume` dropping parallel tool results — sessions with parallel tool calls now restore all tool_use/tool_result pairs instead of showing `[Tool result missing]` placeholders
- **Fixed**: Voice mode WebSocket failures caused by Cloudflare bot detection on non-browser TLS fingerprints
- **Fixed**: 400 errors when using fine-grained tool streaming through API proxies, Bedrock, or Vertex
- **Fixed**: `/remote-control` appearing for gateway and third-party provider deployments where it cannot function
- **Fixed**: Managed settings not being applied at startup when `remote-settings.json` was cached from a prior session
- **Performance**: ~80MB memory reduction on startup for large repositories (tested on 250k-file repos)
- **Improved**: Responsiveness of `@` file autocomplete in large git repos; `/effort` now shows what auto currently resolves to
- **Improved**: `/permissions` — Tab and arrow keys now switch tabs from within a list; background tasks panel left arrow closes list view

### v2.1.79 (2026-03-19)

- **New**: `--console` flag to `claude auth login` for Anthropic Console (API billing) authentication
- **New**: "Show turn duration" toggle added to the `/config` menu
- **Fixed**: `claude -p` hanging when spawned as a subprocess without explicit stdin (e.g. Python `subprocess.run`)
- **Fixed**: Ctrl+C not working in `-p` (print) mode
- **Fixed**: `/btw` returning the main agent's output instead of answering the side question when triggered during streaming
- **Fixed**: Voice mode not activating correctly on startup when `voiceEnabled: true` is set
- **Fixed**: Enterprise users unable to retry on rate limit (429) errors
- **Fixed**: `SessionEnd` hooks not firing when using interactive `/resume` to switch sessions
- **Fixed**: Custom status line showing nothing when workspace trust is blocking it
- **Fixed**: `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` not preventing terminal title from being set on startup
- **Performance**: Improved startup memory usage by ~18MB across all scenarios
- **Performance**: Non-streaming API fallback now has a 2-minute per-attempt timeout (prevents indefinite hangs)
- **VSCode**: Added `/remote-control` to bridge session to claude.ai/code for browser/phone continuation
- **VSCode**: Session tabs now get AI-generated titles based on first message
- **VSCode**: Fixed thinking pill showing "Thinking" instead of "Thought for Ns" after response completes

### v2.1.78 (2026-03-18)

- **New**: `StopFailure` hook event that fires when the turn ends due to an API error (rate limit, auth failure, etc.)
- **New**: `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives plugin updates; `/plugin uninstall` now prompts before deleting plugin data
- **New**: `effort`, `maxTurns`, and `disallowedTools` frontmatter support for plugin-shipped agents
- **New**: `ANTHROPIC_CUSTOM_MODEL_OPTION` env var to add a custom entry to the `/model` picker (with optional `_NAME` and `_DESCRIPTION` suffixed vars)
- **New**: Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach the outer terminal when running inside tmux with `set -g allow-passthrough on`
- **New**: Response text now streams line-by-line as it's generated
- **Fixed**: ⚠️ **Security** — Silent sandbox disable when `sandbox.enabled: true` is set but dependencies are missing — now shows a visible startup warning
- **Fixed**: ⚠️ **Security** — `deny: ["mcp__servername"]` permission rules were not removing MCP server tools before sending to the model, allowing it to see and attempt blocked tools
- **Fixed**: ⚠️ **Security** — `.git`, `.claude`, and other protected directories were writable without a prompt in `bypassPermissions` mode
- **Fixed**: Infinite loop when API errors triggered stop hooks that re-fed blocking errors to the model
- **Fixed**: `cc log` and `--resume` silently truncating conversation history on large sessions (>5 MB) that used subagents
- **Fixed**: `sandbox.filesystem.allowWrite` not working with absolute paths (previously required `//` prefix)
- **Fixed**: `--worktree` flag not loading skills and hooks from the worktree directory
- **Fixed**: `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` and `includeGitInstructions` setting not suppressing git status section in system prompt
- **Fixed**: Bash tool not finding Homebrew and other PATH-dependent binaries when VS Code is launched from Dock/Spotlight
- **Fixed**: Voice mode modifier-combo push-to-talk keybindings requiring a hold instead of activating immediately
- **Fixed**: Voice mode not working on WSL2 with WSLg (Windows 11)
- **Fixed**: `ANTHROPIC_BETAS` environment variable being silently ignored when using Haiku models
- **VSCode**: Fixed "API Error: Rate limit reached" when selecting Opus — model dropdown no longer offers 1M context variant to subscribers whose plan tier is unknown
- **Performance**: Improved memory usage and startup time when resuming large sessions

### v2.1.77 (2026-03-17)

- **New**: ⭐ Opus 4.6 default maximum output tokens raised to 64k; upper bound for Opus 4.6 and Sonnet 4.6 raised to 128k tokens
- **New**: `allowRead` sandbox filesystem setting to re-allow read access within `denyRead` regions
- **New**: `/copy N` to copy the Nth-latest assistant response directly
- **New**: `/branch` command (replaces `/fork`; `/fork` still works as an alias)
- **New**: `SendMessage` now auto-resumes stopped agents in the background instead of returning an error
- **Fixed**: ⚠️ **Security** — `PreToolUse` hooks returning `"allow"` could bypass `deny` permission rules including enterprise managed settings
- **Fixed**: Auto-updater accumulating tens of gigabytes of memory when slash-command overlay repeatedly opened/closed, triggering overlapping binary downloads
- **Fixed**: `--resume` silently truncating recent conversation history due to a race between memory-extraction writes and the main transcript
- **Fixed**: "Always Allow" on compound bash commands (e.g. `cd src && npm test`) saving a single rule for the full string instead of per-subcommand, leading to dead rules and repeated permission prompts
- **Fixed**: Write tool silently converting line endings when overwriting CRLF files or creating files in CRLF directories
- **Fixed**: Cost and token usage not tracked when API falls back to non-streaming mode
- **Fixed**: `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` not stripping beta tool-schema fields, causing proxy gateways to reject requests
- **Fixed**: Bash tool reporting errors for successful commands when system temp directory path contains spaces
- **Fixed**: Paste being lost when typing immediately after pasting; Ctrl+D in `/feedback` deleting forward instead of exiting
- **Fixed**: Various rendering fixes: ordered list numbers, CJK bleeding, background colors in tmux, hyperlinks opening twice in VS Code
- **Fixed**: Teammate panes not closing when leader exits; iTerm2 session crash when selecting text inside tmux over SSH
- **Breaking**: `Agent` tool no longer accepts a `resume` parameter — use `SendMessage({to: agentId})` to continue a previously spawned agent
- **VSCode**: Fixed gitignore patterns with commas silently excluding filetypes from `@`-mention file picker; improved scroll wheel responsiveness; improved plan preview tab titles
- **Performance**: Faster startup on macOS (~60ms) by reading keychain credentials in parallel with module loading; faster `--resume` on fork-heavy sessions (up to 45% faster, 100-150MB less peak memory)

### v2.1.76 (2026-03-14)

- **New**: ⭐ MCP elicitation support — MCP servers can now request structured input mid-task via an interactive dialog (form fields or browser URL)
- **New**: `Elicitation` and `ElicitationResult` hooks to intercept and override MCP input responses before they're sent back to the server
- **New**: `PostCompact` hook that fires after compaction completes
- **New**: `-n` / `--name <name>` CLI flag to set a display name for the session at startup
- **New**: `worktree.sparsePaths` setting for `claude --worktree` in large monorepos — check out only needed directories via git sparse-checkout
- **New**: `/effort` slash command to set model effort level
- **Fixed**: Deferred tools (loaded via `ToolSearch`) losing their input schemas after conversation compaction — array and number parameters were being rejected with type errors
- **Fixed**: Auto-compaction retrying indefinitely after consecutive failures — circuit breaker now stops after 3 attempts
- **Fixed**: `Bash(cmd:*)` permission rules not matching when a quoted argument contains `#`
- **Fixed**: Slash commands showing "Unknown skill"
- **Fixed**: Plan mode asking for re-approval after the plan was already accepted
- **Fixed**: Voice mode swallowing keypresses while a permission dialog or plan editor was open
- **Fixed**: `/voice` not working on Windows when installed via npm
- **Fixed**: Bridge sessions failing to recover after extended WebSocket disconnects
- **Improved**: `--worktree` startup performance by reading git refs directly, skipping redundant `git fetch`
- **Improved**: Killing a background agent now preserves its partial results in the conversation context
- **Improved**: Model fallback notifications — now always visible with human-friendly model names
- **Improved**: Stale worktree cleanup — worktrees left behind after interrupted parallel runs are automatically cleaned up
- **Improved**: Blockquote readability on dark terminal themes — italic with left bar instead of dim
- **Updated**: `--plugin-dir` now accepts one path only; use repeated flags for multiple directories
- **VSCode**: Fixed gitignore patterns containing commas silently excluding entire filetypes from the `@`-mention file picker

### v2.1.75 (2026-03-13)

- **New**: ⭐ 1M context window for Opus 4.6 now enabled by default for Max, Team, and Enterprise plans (previously required extra usage)
- **New**: Session name display on the prompt bar when using `/rename`
- **New**: Last-modified timestamps on memory files — helps Claude reason about freshness of memories
- **New**: Hook source display (settings/plugin/skill) in permission prompts when a hook requires confirmation
- **New**: `/color` command available for all users to set a prompt-bar color
- **Fixed**: Token estimation over-counting for thinking and `tool_use` blocks (was causing premature context compaction)
- **Fixed**: Bash tool mangling `!` in piped commands (e.g. `jq 'select(.x != .y)'` now works correctly)
- **Fixed**: Voice mode not activating correctly on fresh installs without toggling `/voice` twice
- **Fixed**: Claude Code header not updating model name after switching with `/model` or Option+P
- **Fixed**: Session crash when attachment message computation returns undefined values
- **Fixed**: Managed-disabled plugins showing up in `/plugin` Installed tab
- **Fixed**: Corrupted marketplace config path handling
- **Fixed**: `/resume` losing session names after resuming a forked or continued session
- **Improved**: Startup performance on macOS non-MDM machines (skips unnecessary subprocess spawns)
- **Improved**: Async hook completion messages suppressed by default (visible with `--verbose` or transcript mode)

### v2.1.74 (2026-03-12)

- **New**: `/context` command shows actionable suggestions — identifies context-heavy tools, memory bloat, capacity warnings with optimization tips
- **New**: `autoMemoryDirectory` setting to configure custom directory for auto-memory storage
- **Fixed**: Memory leak in streaming API response buffers — unbounded RSS growth on Node.js/npm path resolved
- **Fixed**: Managed policy `ask` rules being bypassed by user `allow` rules or skill `allowed-tools`
- **Fixed**: MCP OAuth authentication hanging when callback port is already in use
- **Fixed**: MCP OAuth refresh (Slack) never prompting re-auth after refresh token expires
- **Fixed**: Voice mode on macOS native binary — binary now includes `audio-input` entitlement for microphone permission prompt
- **Fixed**: `SessionEnd` hooks killed after 1.5s regardless of `hook.timeout` (now configurable via `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS`)
- **Changed**: `--plugin-dir` local dev copies now override installed marketplace plugins with same name
- **VSCode**: Fixed delete button not working for Untitled sessions

### v2.1.73 (2026-03-11)

- **New**: `modelOverrides` setting — map model picker entries to custom provider model IDs (Bedrock inference profile ARNs, etc.)
- **New**: Actionable guidance when OAuth login or connectivity checks fail due to SSL certificate errors (corporate proxies, `NODE_EXTRA_CA_CERTS`)
- **Fixed**: Freezes and 100% CPU loops triggered by permission prompts for complex bash commands
- **Fixed**: Deadlock when many skill files changed at once (e.g. `git pull` in repo with large `.claude/skills/` directory)
- **Fixed**: Bash tool output lost when running multiple Claude Code sessions in the same project directory
- **Fixed**: Subagents with `model: opus`/`sonnet`/`haiku` being silently downgraded on Bedrock, Vertex, Foundry
- **Fixed**: Background bash processes from subagents not cleaned up when agent exits
- **Fixed**: `SessionStart` hooks firing twice when resuming via `--resume` or `--continue`
- **Fixed**: JSON-output hooks injecting no-op system-reminder messages into the model's context on every turn
- **Fixed**: Linux sandbox failing with "ripgrep not found" on native builds
- **Fixed**: Linux native modules on Amazon Linux 2 (glibc 2.26 systems)
- **Changed**: Default Opus model on Bedrock, Vertex, Foundry → Opus 4.6 (was 4.1)
- **Changed**: Deprecated `/output-style` — use `/config` instead; output style fixed at session start for better prompt caching
- **VSCode**: Fixed HTTP 400 errors for users behind proxies or on Bedrock/Vertex with Claude 4.5 models

### v2.1.72 (2026-03-09)

- **New**: Restored `model` parameter on Agent tool — per-invocation model overrides are back
- **New**: `/plan` accepts optional description (e.g., `/plan fix the auth bug`) to enter plan mode and start immediately
- **New**: `ExitWorktree` tool to leave an `EnterWorktree` session
- **New**: `CLAUDE_CODE_DISABLE_CRON` env var to stop scheduled cron jobs mid-session
- **New**: `lsof`, `pgrep`, `tput`, `ss`, `fd`, `fdfind` added to bash auto-approval allowlist
- **New**: `/copy` `w` key writes selection directly to file, bypassing clipboard (useful over SSH)
- **Changed**: Simplified effort levels to low/medium/high (removed max), new symbols ○ ◐ ●; use `/effort auto` to reset
- **Changed**: CLAUDE.md HTML comments (`<!-- ... -->`) now hidden from Claude when auto-injected (visible via Read tool)
- **Changed**: `/config` — Escape cancels changes, Enter saves and closes, Space toggles settings
- **Fixed**: SDK `query()` prompt cache invalidation — up to 12x input token cost reduction
- **Fixed**: Tool search now activates with `ANTHROPIC_BASE_URL` when `ENABLE_TOOL_SEARCH` is set
- **Fixed**: Skill hooks firing twice per event when a hooks-enabled skill is invoked by the model
- **Fixed**: `/clear` killing background agent/bash tasks — only foreground tasks now cleared
- **Fixed**: Worktree isolation: Task tool resume not restoring cwd, background task notifications missing `worktreePath`/`worktreeBranch`
- **Fixed**: `--continue` not resuming from most recent point after `--compact`
- **Fixed**: Team agents now inherit the leader's model
- **Fixed**: Parallel tool calls — only Bash errors cascade to siblings (Read/WebFetch/Glob failures no longer cancel siblings)
- **Fixed**: Multiple hooks issues: `transcript_path` wrong for resumed/forked sessions, async hooks not receiving stdin, PostToolUse block reason displaying twice
- **Fixed**: Several sandbox permission, plugin installation (Windows/OneDrive), and voice mode issues
- **Perf**: Reduced bundle size by ~510 KB; improved CPU utilization in long sessions; faster bash init via native module

### v2.1.69 (2026-03-04)

- **Security**: Fixed nested skill discovery loading skills from gitignored directories like `node_modules` — critical security fix
- **Security**: Fixed symlink bypass allowing writes outside working directory in `acceptEdits` mode
- **Security**: Fixed trust dialog silently enabling all `.mcp.json` servers on first run (per-server approval now required)
- **Security**: Fixed sandbox not blocking non-allowed domains when `allowManagedDomainsOnly` is enabled
- **New**: `InstructionsLoaded` hook event fires when CLAUDE.md or `.claude/rules/*.md` files are loaded into context
- **New**: `agent_id`, `agent_type`, `worktree` fields added to all hook events (subagent tracking, worktree metadata)
- **New**: `${CLAUDE_SKILL_DIR}` variable for skills to reference their own installation directory in SKILL.md content
- **New**: `/reload-plugins` command to activate pending plugin changes without restarting Claude Code
- **New**: Voice STT expanded to 20 languages (+10: Russian, Polish, Turkish, Dutch, Ukrainian, Greek, Czech, Danish, Swedish, Norwegian)
- **New**: `sandbox.enableWeakerNetworkIsolation` setting (macOS) for Go tools (gh, gcloud, terraform) behind MITM proxy
- **New**: `includeGitInstructions` setting (and `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` env var) to remove built-in commit/PR instructions from system prompt
- **New**: `oauth.authServerMetadataUrl` config option for MCP servers with custom OAuth discovery
- **New**: `pluginTrustMessage` in managed settings for organization-specific plugin trust context
- **New**: Optional `--name` argument for `/remote-control` to set a custom session title visible in claude.ai/code
- **Changed**: Sonnet 4.5 users on Pro/Max/Team auto-migrated to Sonnet 4.6
- **Changed**: `/resume` picker now shows most recent prompt instead of first one
- **Fixed**: 15+ memory leaks — React Compiler memoCache, REPL render scopes (~35MB over 1000 turns), teammate history pinning, hook event accumulation
- **Fixed**: ~16MB baseline memory reduction (deferred Yoga WASM preloading)
- **Fixed**: MCP binary content (PDFs, Office docs, audio) now saved to disk with correct extension instead of raw base64 in context
- **Fixed**: Startup performance — skills/plugins loading, worktree git subprocess, macOS keychain, managed settings
- **Fixed**: Escape not interrupting running turn when input box has draft text
- **Fixed**: Duplicate CLAUDE.md, slash commands, agents, and rules when running from nested worktree
- **Fixed**: macOS keychain corruption with multiple OAuth MCP servers (stdin buffer overflow)

### v2.1.68 (2026-03-04)

- **Changed**: Opus 4.6 now defaults to medium effort for Max and Team subscribers (sweet spot between speed and thoroughness)
- **New**: Re-introduced `ultrathink` keyword to enable high effort for the next turn specifically
- **Breaking**: Opus 4 and Opus 4.1 removed from Claude Code on first-party API — users auto-migrated to Opus 4.6

### v2.1.66 (2026-03-04)

- **Fixed**: Reduced spurious error logging

### v2.1.63 (2026-02-27)

- **New**: HTTP hooks — hooks can now `POST` JSON to a URL and receive JSON back, instead of running a shell command. Useful for CI/CD integrations and stateless backend endpoints (v2.1.63+)
- **New**: Project configs & auto-memory now shared across all git worktrees of the same repository
- **New**: `/simplify` and `/batch` bundled slash commands
- **New**: `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var to opt out of claude.ai MCP server exposure
- **Improved**: `/model` command shows currently active model in picker
- **Fixed**: Major wave of memory leaks — WebSocket listeners, MCP caches, git root detection cache, JSON parsing cache, bash prefix cache, subagent AppState after compaction, MCP server fetch caches on reconnect
- **Fixed**: VSCode remote sessions not appearing in conversation history
- **Fixed**: `/clear` not resetting cached skills (stale skill content persisted to new conversation)
- **Fixed**: Local slash command output (e.g. `/cost`) appearing as user messages in UI

### v2.1.62 (2026-02-27)

- **Fixed**: Prompt suggestion cache regression that reduced cache hit rates

### v2.1.61 (2026-02-27)

- **Fixed**: Concurrent writes corrupting config file on Windows

### v2.1.59 (2026-02-26)

- **New**: Auto-memory — Claude automatically saves useful context to memory; manage with `/memory`
- **New**: `/copy` command — interactive picker when code blocks are present, select individual blocks or full response
- **Improved**: Smarter "always allow" prefix suggestions for compound bash commands (per-subcommand prefixes instead of treating whole command as one)
- **Improved**: Memory usage in multi-agent sessions (releases completed subagent task state)
- **Improved**: Ordering of short task lists
- **Fixed**: MCP OAuth token refresh race condition when running multiple Claude Code instances simultaneously
- **Fixed**: Shell commands not showing clear error message when working directory has been deleted
- **Fixed**: Config file corruption that could wipe authentication when multiple Claude Code instances ran simultaneously

### v2.1.58 (2026-02-26)

- **Expanded**: Remote Control available to more users

### v2.1.56 (2026-02-25)

- **Fixed**: VSCode: Another cause of "command 'claude-vscode.editor.openLast' not found" crashes

### v2.1.55 (2026-02-25)

- **Fixed**: BashTool failing on Windows with EINVAL error

### v2.1.53 (2026-02-25)

- **Fixed**: UI flicker where user input briefly disappeared after submission before rendering
- **Fixed**: Bulk agent kill (ctrl+f) now sends single aggregate notification instead of one per agent, and properly clears command queue
- **Fixed**: Graceful shutdown sometimes leaving stale sessions when using Remote Control (parallelized teardown)
- **Fixed**: `--worktree` flag sometimes being ignored on first launch
- **Fixed**: Panic ("switch on corrupted value") on Windows
- **Fixed**: Crash when spawning many processes on Windows
- **Fixed**: Crash in WebAssembly interpreter on Linux x64 & Windows x64
- **Fixed**: Crash that sometimes occurred after 2 minutes on Windows ARM64

### v2.1.52 (2026-02-24)

- **Fixed**: VSCode extension crash on Windows ("command 'claude-vscode.editor.openLast' not found")

### v2.1.51 (2026-02-24)

- **New**: `claude remote-control` subcommand for external builds — enables local environment serving for all users
- **New**: Custom npm registries and specific version pinning when installing plugins from npm sources
- **New**: SDK: `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, `CLAUDE_CODE_ORGANIZATION_UUID` env vars to provide account info synchronously (eliminates race conditions in early telemetry)
- **Changed**: BashTool now skips login shell (`-l` flag) by default when shell snapshot is available — performance improvement (previously required `CLAUDE_BASH_NO_LOGIN=true`)
- **Changed**: Tool results larger than 50K characters now persisted to disk (previously 100K threshold)
- **Improved**: `/model` picker now shows human-readable labels (e.g., "Sonnet 4.5") instead of raw model IDs for pinned versions, with upgrade hint when newer version available
- **Fixed**: Security issue where `statusLine` and `fileSuggestion` hook commands could execute without workspace trust acceptance in interactive mode
- **Fixed**: Duplicate `control_response` messages from WebSocket reconnects causing API 400 errors
- **Fixed**: Slash command autocomplete crashing when a plugin's SKILL.md description is a YAML array or other non-string type

### v2.1.50 (2026-02-21)

- **New**: `WorktreeCreate` and `WorktreeRemove` hook events — custom VCS setup/teardown when agent worktree isolation creates or removes worktrees
- **New**: `isolation: worktree` in agent definitions for declarative worktree isolation (no longer requires setting in each call)
- **New**: `claude agents` CLI command to list all configured agents
- **New**: `startupTimeout` configuration for LSP servers
- **New**: `CLAUDE_CODE_DISABLE_1M_CONTEXT` env var to disable 1M context window support
- **New**: Pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (Slack); use `--client-id` and `--client-secret` with `claude mcp add`
- **New**: VSCode `/extra-usage` command support
- **Changed**: Opus 4.6 (fast mode) now includes full 1M context window
- **Changed**: `CLAUDE_CODE_SIMPLE` mode now also disables MCP tools, attachments, hooks, and CLAUDE.md loading for fully minimal experience
- **Fixed**: Bug where resumed sessions could be invisible when working directory involved symlinks
- **Fixed**: `disableAllHooks` setting to respect managed settings hierarchy (non-managed settings can no longer disable managed hooks)
- **Fixed**: Linux: native modules not loading on systems with glibc older than 2.30 (RHEL 8)
- **Fixed**: Memory leak in agent teams where completed teammate tasks were never garbage collected
- **Fixed**: Memory leak where completed task state objects were never removed from AppState
- **Fixed**: Memory leak where LSP diagnostic data was never cleaned up after delivery
- **Fixed**: Unbounded memory growth in long sessions (file history snapshots capped; circular buffer fix; stream buffers released after use)
- **Fixed**: MCP tools not discovered when tool search is enabled and prompt passed as launch argument
- **Fixed**: Prompt suggestion cache regression that reduced cache hit rates
- **Improved**: Startup performance for headless mode (`-p`) by deferring Yoga WASM and UI component imports
- **Improved**: Memory usage during long sessions by clearing internal caches after compaction and clearing large tool results after processing

### v2.1.49 (2026-02-20)

- **New**: `--worktree` / `-w` CLI flag to start Claude in an isolated git worktree
- **New**: Subagents support `isolation: "worktree"` for working in a temporary git worktree
- **New**: `background: true` field in agent definitions to always run as a background task
- **New**: `ConfigChange` hook event — fires when configuration files change during a session (enterprise security auditing + blocking)
- **New**: Plugins can ship `settings.json` for default configuration
- **New**: `--from-pr` flag to resume sessions linked to a specific GitHub PR (+ sessions auto-linked when created via `gh pr create`)
- **New**: `PreToolUse` hooks can return `additionalContext` to the model
- **New**: `plansDirectory` setting to customize where plan files are stored
- **New**: `auto:N` syntax for configuring MCP tool search auto-enable threshold
- **New**: `Setup` hook event triggered via `--init`, `--init-only`, or `--maintenance` CLI flags
- **Changed**: Sonnet 4.5 1M context removed from Max plan — Sonnet 4.6 now has 1M context (switch in `/model`)
- **Changed**: Simple mode now includes file edit tool (not just Bash)
- **Fixed**: File-not-found errors now suggest corrected paths when model drops repo folder
- **Fixed**: Ctrl+C and ESC silently ignored when background agents running + main thread idle (double-press within 3s now kills all agents)
- **Fixed**: Plugin `enable`/`disable` auto-detects correct scope (no longer defaults to user scope)
- **Fixed**: Context window blocking limit calculated too aggressively (~65% instead of ~98%)
- **Fixed**: Memory issues causing crashes with parallel subagents
- **Fixed**: Memory leak in long sessions where stream resources not cleaned up
- **Fixed**: `@` symbol incorrectly triggering file autocomplete in bash mode
- **Fixed**: Background agent results returning raw transcript data instead of final answer
- **Fixed**: Slash command autocomplete selecting wrong command (e.g. `/context` vs `/compact`)
- **Improved**: `@` mention file suggestion speed (~3× faster in git repos)
- **Improved**: MCP connection: `list_changed` notification support for dynamic tool updates without reconnection
- **Improved**: Skills invoke progress display; skill suggestions prioritize recently/frequently used
- **Improved**: Incremental output for async agents; token count includes background agent tokens

### v2.1.47 (2026-02-19)

- **Improved**: VS Code plan preview auto-updates as Claude iterates; commenting enabled only when plan is ready for review; preview stays open when rejected for revision
- **New**: `ctrl+f` kills all background agents simultaneously (replaces double-ESC); ESC now cancels main thread only, background agents keep running
- **New**: `last_assistant_message` field added to Stop and SubagentStop hook inputs (access final response without parsing transcript files)
- **New**: `chat:newline` keybinding action; `added_dirs` in statusline JSON workspace section
- **Fixed**: Compaction failing when conversation contains many PDF documents (strips document blocks alongside images)
- **Fixed**: Edit tool corrupting Unicode curly quotes (`"` `"` `'` `'`) by replacing with straight quotes
- **Fixed**: Parallel file write/edit — single file failure no longer aborts sibling operations
- **Fixed**: OSC 8 hyperlinks only clickable on first line when link text wraps across multiple terminal lines
- **Fixed**: Bash permission classifier now validates match descriptions against actual input rules (prevents hallucinated permissions)
- **Fixed**: Config backups timestamped and rotated (5 most recent kept) instead of overwriting
- **Fixed**: Session name lost after context compaction; plan mode lost after compaction
- **Fixed**: Hooks (PreToolUse, PostToolUse) silently failing on Windows (now uses Git Bash)
- **Fixed**: Custom agents/skills not discovered in git worktrees (main repo `.claude/` now included)
- **Fixed**: 70+ additional rendering, session, permission, and platform fixes

### v2.1.46 (2026-02-19)

- **Fixed**: Orphaned Claude Code processes after terminal disconnect on macOS
- **New**: Support for using claude.ai MCP connectors in Claude Code

### v2.1.45 (2026-02-17)

- **New**: Claude Sonnet 4.6 model support
- **New**: `spinnerTipsOverride` setting — customize spinner tips via `tips` array, opt out of built-in tips with `excludeDefault: true`
- **New**: SDK `SDKRateLimitInfo` and `SDKRateLimitEvent` types for rate limit status tracking (utilization, reset times, overage)
- **Fixed**: Agent Teams teammates failing on Bedrock, Vertex, and Foundry (env vars now propagated to tmux-spawned processes)
- **Fixed**: Sandbox "operation not permitted" errors on macOS temp file writes
- **Fixed**: Task tool (backgrounded agents) crashing with `ReferenceError` on completion
- **Improved**: Memory usage for large shell command outputs (RSS no longer grows unboundedly)
- **Improved**: Startup performance (removed eager session history loading)
- **Improved**: Plugin-provided commands, agents, and hooks available immediately after install (no restart needed)

### v2.1.44 (2026-02-17)

- Fixed: Auth refresh errors

### v2.1.43 (2026-02-17)

- Fixed: AWS auth refresh hanging indefinitely (added 3-minute timeout)
- Fixed: Structured-outputs beta header being sent unconditionally on Vertex/Bedrock
- Fixed: Spurious warnings for non-agent markdown files in `.claude/agents/` directory

### v2.1.42 (2026-02-14)

- **Improved**: Startup performance via deferred Zod schema construction (faster on large projects)
- **Improved**: Prompt cache hit rate by moving date outside the system prompt (avoids daily cache invalidation)
- **New**: Opus 4.6 effort callout for eligible users (one-time onboarding)
- Fixed: `/resume` showing interrupt messages as session titles
- Fixed: Image dimension limit errors now suggest using `/compact` instead of opaque failure

### v2.1.41 (2026-02-13)

- **New**: Guard against launching Claude Code inside another Claude Code session
- **New**: `claude auth login`, `claude auth status`, `claude auth logout` CLI subcommands
- **New**: Windows ARM64 (win32-arm64) native binary support
- Added `speed` attribute to OTel events and trace spans for fast mode visibility
- **Improved**: `/rename` auto-generates session name from conversation context when called without arguments
- Improved narrow terminal layout for prompt footer
- Fixed: Agent Teams using wrong model identifier for Bedrock, Vertex, and Foundry customers
- Fixed: Crash when MCP tools return image content during streaming
- Fixed: `/resume` session previews showing raw XML tags instead of readable command names
- Fixed: Opus 4.6 launch announcement showing for Bedrock/Vertex/Foundry users
- Fixed: Hook blocking errors (exit code 2) not showing stderr to the user
- Fixed: Structured-outputs beta header sent unconditionally on Vertex/Bedrock
- Fixed: File resolution for @-mentions with anchor fragments (e.g., `@README.md#installation`)
- Fixed: FileReadTool blocking on FIFOs, `/dev/stdin`, and large files
- Fixed: Background task notifications not delivered in streaming Agent SDK mode
- Fixed: Auto-compact failure error notifications shown to users
- Fixed: Stale permission rules not clearing when settings change on disk
- Fixed: Permission wait time included in subagent elapsed time display
- Fixed: Proactive ticks firing while in plan mode
- Improved: Model error messages for Bedrock/Vertex/Foundry with fallback suggestions

### v2.1.39 (2026-02-10)

- Improved: Terminal rendering performance
- Fixed: Fatal errors being swallowed instead of displayed
- Fixed: Process hanging after session close
- Fixed: Character loss at terminal screen boundary
- Fixed: Blank lines in verbose transcript view

### v2.1.38 (2026-02-10)

- Fixed: VS Code terminal scroll-to-top regression introduced in 2.1.37
- Fixed: Tab key queueing slash commands instead of autocompleting
- Fixed: Bash permission matching for commands using environment variable wrappers
- Fixed: Text between tool uses disappearing when not using streaming
- **Security**: Improved heredoc delimiter parsing to prevent command smuggling
- **Security**: Blocked writes to `.claude/skills` directory in sandbox mode

### v2.1.37 (2026-02-08)

- Fixed `/fast` not immediately available after enabling `/extra-usage`

### v2.1.36 (2026-02-08) ⭐

- ⭐ **Fast mode now available for Opus 4.6** — Same model, faster output. Toggle with `/fast`. [Learn more](https://code.claude.com/docs/en/fast-mode)

### v2.1.34 (2026-02-07)

- Fixed a crash when agent teams setting changed between renders
- **Security fix**: Commands excluded from sandboxing (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled

### v2.1.33 (2026-02-06)

**Highlights**:
- **Agent teams fixes** — Improved tmux session handling and availability warnings
- **New hook events** — `TeammateIdle` and `TaskCompleted` for multi-agent workflows
- **Agent frontmatter enhancements**:
  - `memory` field for user/project/local scope memory selection
  - `Task(agent_type)` syntax to restrict sub-agent spawning in agent definitions
- **Plugin identification** — Plugin name now shown in skill descriptions and `/skills` menu
- **VSCode improvements** — Remote sessions support, branch/message count in session picker
- Fixed: Thinking interruption, streaming abort, proxy settings, `/resume` XML markup
- Improved: API connection errors show specific cause instead of generic message
- Improved: Invalid managed settings errors now surfaced properly
- Multiple stability fixes across agent workflows and tool interactions

### v2.1.32 (2026-02-05) ⭐ MAJOR

**Highlights**:
- ⭐ **Claude Opus 4.6 is now available!**
- ⭐ **Agent teams research preview** — Multi-agent collaboration for complex tasks (token-intensive, requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- ⭐ **Automatic memory recording and recall** — Claude now automatically records and recalls memories as it works
- **"Summarize from here"** — Message selector now allows partial conversation summarization
- Skills from `.claude/skills/` in `--add-dir` directories auto-load
- Fixed: `@` file completion showing incorrect relative paths from subdirectories
- Fixed: Bash tool no longer throws "Bad substitution" errors with JavaScript template literals (e.g., `${index + 1}`)
- Improved: Skill character budget now scales with context window (2% of context)
- Improved: `--resume` re-uses `--agent` value from previous conversation by default
- Fixed: Thai/Lao spacing vowels rendering issues
- [VSCode] Fixed slash commands incorrectly executing when pressing Enter with preceding text
- [VSCode] Added spinner when loading past conversations list

### v2.1.31 (2026-02-03)

- **Session resume hint** — Exit message now shows how to continue your conversation later
- **Full-width (zenkaku) space support** — Added Japanese IME checkbox selection support
- Fixed: PDF too large errors permanently locking sessions (now recoverable without starting new conversation)
- Fixed: Bash commands incorrectly reporting "Read-only file system" when sandbox enabled
- Fixed: Plan mode crash when project config missing default fields
- Fixed: `temperatureOverride` being silently ignored in streaming API path
- Fixed: LSP shutdown/exit compatibility with strict language servers
- Improved: System prompts now guide model toward Read/Edit/Glob/Grep tools instead of bash equivalents
- Improved: PDF and request size error messages show actual limits (100 pages, 20MB)
- Reduced: Layout jitter when spinner appears/disappears during streaming

### v2.1.30 (2026-02-02)

- **⭐ PDF page range support** — `pages` parameter in Read tool for PDFs (e.g., `pages: "1-5"`) with lightweight references for large PDFs (>10 pages)
- **⭐ Pre-configured OAuth for MCP servers** — Built-in client credentials for servers without Dynamic Client Registration (Slack support via `--client-id` and `--client-secret`)
- **⭐ New `/debug` command** — Claude can help troubleshoot current session issues
- **Additional git flags** — Support for `git log` and `git show` read-only flags (`--topo-order`, `--cherry-pick`, `--format`, `--raw`)
- **Task tool metrics** — Results now include token count, tool uses, and duration
- **Reduced motion mode** — New config option for accessibility
- Fixed: Phantom "(no content)" text blocks in API history (reduces token waste)
- Fixed: Prompt cache not invalidating when tool schemas changed
- Fixed: 400 errors after `/login` with thinking blocks
- Fixed: Session resume hang with corrupted `parentUuid` cycles
- Fixed: Rate limit showing wrong "/upgrade" for Max 20x users
- Fixed: Permission dialogs stealing focus while typing
- Fixed: Subagents unable to access SDK MCP tools
- Fixed: Windows users with `.bashrc` unable to run bash
- Improved: Memory usage for `--resume` (68% reduction for many sessions)
- Improved: TaskStop displays stopped command description instead of generic message
- Changed: `/model` executes immediately instead of queuing
- [VSCode] Added multiline input in "Other" text fields (Shift+Enter for new lines)
- [VSCode] Fixed duplicate sessions in session list

### v2.1.29 (2026-01-31)

- **Performance**: Fixed startup performance issues when resuming sessions with saved hook context
- Significantly improved session recovery speed for long-duration sessions

### v2.1.27 (2026-01-29)

- **New**: `--from-pr` flag to resume sessions linked to a specific GitHub PR number or URL
- **New**: Sessions automatically linked to PRs when created via `gh pr create`
- Added tool call failures and denials to debug logs
- Fixed context management validation error for Bedrock/Vertex gateway users
- Fixed `/context` command not displaying colored output
- Fixed status bar duplicating background task indicator when PR status was shown
- [Windows] Fixed bash command execution failing for users with `.bashrc` files
- [Windows] Fixed console windows flashing when spawning child processes
- [VSCode] Fixed OAuth token expiration causing 401 errors after extended sessions

### v2.1.25 (2026-01-30)

- Fixed beta header validation for Bedrock and Vertex gateway users — Ensures `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` environment variable works correctly

### v2.1.23 (2026-01-29)

- **Customizable spinner verbs** — New `spinnerVerbs` setting allows personalization of spinner action words
- mTLS and corporate proxy connectivity fixes — Improved support for users behind corporate proxies with client certificates
- Per-user temp directory isolation — Prevents permission conflicts on shared systems
- Improved terminal rendering performance — Optimized screen data layout for faster updates
- Fixed: Prompt caching race condition causing 400 errors
- Fixed: Async hooks not canceling when headless streaming ends
- Fixed: Tab completion not updating input field
- Fixed: Ripgrep search timeouts returning empty results instead of errors
- Changed: Bash commands show timeout duration alongside elapsed time
- Changed: Merged PRs show purple status indicator in prompt footer
- [IDE] Fixed: Model options displaying incorrect region strings for Bedrock users in headless mode

### v2.1.22 (2026-01-28)

- Improved task UI performance with virtualization — Task list now uses virtual scrolling for better responsiveness with many tasks
- Vim selection and deletion fixes — Fixed visual mode selections and `dw` command behavior
- LSP improvements: Kotlin support, UTF-16 range handling, better error recovery
- Tasks now consistently use `task-N` IDs instead of internal UUIDs
- Fixed: `#` keyboard shortcut not working in task creation fields
- Fixed: Compact tool use rendering in chat history
- Fixed: Session URL escaping in git commit messages
- Fixed: Command output handling improvements

### v2.1.21 (2026-01-28)

- **Skills/commands can specify required/recommended Claude Code version** — Use `minClaudeCodeVersion` and `recommendedClaudeCodeVersion` in frontmatter
- **New TaskCreate fields**: `category` (testing, implementation, documentation, etc.), `checklist` (subtasks as markdown list), `parentId` (task hierarchy)
- **Automatic Claude Code update checking** at session start (respects auto-update settings)
- Tasks appear in `/context` output with 'Disable tasks' shortcut for quick toggling
- Improved task UI: Delete button added, better empty state messaging
- Fixed: Task deletion now properly removes all related task data
- Fixed: Shell environment variables expanded correctly in hook commands
- Fixed: Pasted URLs with parentheses properly formatted in markdown
- Fixed: Bash output capture for commands with large output

### v2.1.20 (2026-01-27)

- **New**: TaskUpdate tool can delete tasks via `status="deleted"`
- **New**: PR review status indicator in prompt footer — Shows PR state (approved, changes requested, pending, draft) as colored dot with clickable link
- Arrow key history navigation in vim normal mode when cursor cannot move further
- External editor shortcut (Ctrl+G) added to help menu
- Support for loading CLAUDE.md from `--add-dir` directories (requires `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`)
- Fixed: Session compaction issues causing full history load instead of compact summary
- Fixed: Agents ignoring user messages while actively working
- Fixed: Wide character (emoji, CJK) rendering artifacts
- Improved: Task list dynamically adjusts to terminal height
- Changed: Background agents prompt for tool permissions before launching
- Changed: Config backups timestamped and rotated (keeps 5 most recent)

### v2.1.19 (2026-01-25)

- **New**: `CLAUDE_CODE_ENABLE_TASKS` environment variable — Set to `false` to temporarily revert to old task system
- **New**: Argument shorthand in custom commands — Use `$0`, `$1`, etc. instead of verbose syntax
- [VSCode] Session forking and rewind functionality enabled for all users
- Fixed: Crashes on processors without AVX instruction support
- Fixed: Dangling Claude Code processes when terminal closed (SIGKILL fallback)
- Fixed: `/rename` and `/tag` not updating correct session when resuming from different directory (git worktrees)
- Fixed: Resuming sessions by custom title from different directory
- Fixed: Pasted text lost when using prompt stash (Ctrl+S) and restore
- Fixed: Agent list displaying "Sonnet (default)" instead of "Inherit (default)" for agents without explicit model
- Fixed: Backgrounded hook commands blocking session instead of returning early
- Fixed: File write preview omitting empty lines
- Changed: Skills without additional permissions/hooks allowed without approval
- [SDK] Added replay of queued_command attachment messages when `replayUserMessages` enabled

**⚠️ Breaking**:
- Indexed argument syntax changed: `$ARGUMENTS.0` → `$ARGUMENTS[0]` (bracket syntax)

### v2.1.18 (2026-01-24) ⭐

- ⭐ **Customizable keyboard shortcuts** — Configure keybindings per context, create chord sequences, personalize workflow
- Run `/keybindings` to get started
- Learn more: [code.claude.com/docs/en/keybindings](https://code.claude.com/docs/en/keybindings)

### v2.1.17 (2026-01-23)

- Fix: Crashes on processors without AVX instruction support

### v2.1.16 (2026-01-22) ⭐

- ⭐ **New task management system** with dependency tracking
- [VSCode] Native plugin management support
- [VSCode] OAuth users can browse and resume remote sessions from Sessions dialog
- Fixed: Out-of-memory crashes when resuming sessions with heavy subagent usage
- Fixed: "Context remaining" warning not hidden after `/compact`
- [IDE] Fixed race condition on Windows where sidebar view container wouldn't appear

### v2.1.15 (2026-01-22)

- **⚠️ Deprecation notice for npm installations** — Run `claude install` or see [docs](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- Improved UI rendering performance with React Compiler
- Fixed: MCP stdio server timeout not killing child process, which could cause UI freezes

### v2.1.14 (2026-01-21)

- **History-based autocomplete in bash mode** — Type `!` followed by a partial command and press Tab to complete from bash history
- Search functionality in installed plugins list
- Support for pinning plugins to specific git commit SHAs for exact version control
- Fixed: Context window blocking limit calculated too aggressively (~65% instead of ~98%)
- Fixed: Memory issues and leaks in long-running sessions with parallel subagents
- Fixed: `@` symbol incorrectly triggering file autocomplete in bash mode
- Fixed: Slash command autocomplete selecting wrong command for similar names
- Improved: Backspace deletes pasted text as single token

### v2.1.12 (2026-01-18)

- Bug fix: Message rendering

### v2.1.11 (2026-01-17)

- Fix: Excessive MCP connection requests for HTTP/SSE transports

### v2.1.10 (2026-01-17)

- New `Setup` hook event (--init, --init-only, --maintenance flags)
- Keyboard shortcut 'c' to copy OAuth URL
- File suggestions show as removable attachments
- [VSCode] Plugin install count + trust warnings

### v2.1.9 (2026-01-16)

- **`auto:N` syntax for MCP tool search threshold** — Configure when Tool Search activates: `ENABLE_TOOL_SEARCH=auto:5` (5% context), `auto:10` (default), `auto:20` (conservative). See [architecture.md](./architecture.md#mcp-tool-search-lazy-loading) for details.
- `plansDirectory` setting for custom plan file locations
- Session URL attribution to commits/PRs from web sessions
- PreToolUse hooks can return `additionalContext`
- `${CLAUDE_SESSION_ID}` string substitution for skills

### v2.1.7 (2026-01-15)

- `showTurnDuration` setting to hide turn duration messages
- **MCP Tool Search auto mode enabled by default** — Lazy loading for MCP tools when definitions exceed 10% of context. Based on Anthropic's [Advanced Tool Use](https://www.anthropic.com/engineering/advanced-tool-use) API feature. Result: **85% token reduction** on tool definitions, improved tool selection accuracy (Opus 4: 49%→74%, Opus 4.5: 79.5%→88.1%)
- Inline display of agent final response in task notifications

**⚠️ Breaking**:
- OAuth/API Console URLs changed: `console.anthropic.com` → `platform.claude.com`
- Security fix: Wildcard permission rules could match compound commands

### v2.1.6 (2026-01-14)

- Search functionality in `/config` command
- Date range filtering in `/stats` (press `r` to cycle)
- Auto-discovery of skills from nested `.claude/skills` directories
- Updates section in `/doctor` showing auto-update channel

**⚠️ Security Fix**: Permission bypass via shell line continuation

### v2.1.5 (2026-01-13)

- `CLAUDE_CODE_TMPDIR` environment variable for custom temp directory

### v2.1.4 (2026-01-12)

- `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable

### v2.1.3 (2026-01-11)

- Merged slash commands and skills (simplified mental model)
- Release channel toggle (stable/latest) in `/config`
- `/doctor` warnings for unreachable permission rules

### v2.1.2 (2026-01-10)

- Windows Package Manager (winget) support
- Clickable hyperlinks for file paths (OSC 8 terminals)
- Shift+Tab shortcut in plan mode for auto-accept edits
- Large bash outputs saved to disk instead of truncated

**⚠️ Breaking**:
- Security fix: Command injection in bash command processing
- Deprecated: `C:\ProgramData\ClaudeCode` managed settings path

### v2.1.0 (2026-01-08) ⭐ MAJOR

**Highlights**:
- ⭐ **Automatic skill hot-reload** — Skills modified in `~/.claude/skills` or `.claude/skills` immediately available
- ⭐ **Shift+Enter works OOTB** in iTerm2, WezTerm, Ghostty, Kitty
- ⭐ **New Vim motions**: `;` `,` `y` `yy` `Y` `p` `P` text objects (`iw` `aw` `i"` etc.) `>>` `<<` `J`
- **Unified Ctrl+B** for backgrounding all running tasks
- `/plan` command shortcut to enable plan mode
- Slash command autocomplete anywhere in input
- `language` setting for response language (e.g., `language: "japanese"`)
- Skills `context: fork` support for forked sub-agent context
- Hooks support in agent/skill/command frontmatter
- MCP `list_changed` notifications support
- `/teleport` and `/remote-env` commands for web sessions
- Disable specific agents with `Task(AgentName)` syntax
- `--tools` flag in interactive mode
- YAML-style lists in frontmatter `allowed-tools`

**⚠️ Breaking**:
- OAuth URLs: `console.anthropic.com` → `platform.claude.com`
- Removed permission prompt for entering plan mode
- [SDK] Minimum zod peer dependency: `^4.0.0`

---

## 2.0.x Series (November 2025 - January 2026)

### v2.0.76 (2026-01-05)

- Fix: macOS code-sign warning with Claude in Chrome

### v2.0.74 (2026-01-04) ⭐

- ⭐ **LSP (Language Server Protocol) tool** for code intelligence (go-to-definition, find references, hover)
- `/terminal-setup` for Kitty, Alacritty, Zed, Warp
- Ctrl+T in `/theme` to toggle syntax highlighting
- Grouped skills/agents by source in `/context`

### v2.0.72 (2026-01-02) ⭐

- ⭐ **Claude in Chrome (Beta)** — Control browser directly from Claude Code
- Reduced terminal flickering
- QR code for mobile app download
- Thinking toggle changed: Tab → Alt+T

### v2.0.70 (2025-12-30)

- Enter key accepts/submits prompt suggestions immediately
- Wildcard syntax `mcp__server__*` for MCP tool permissions
- Auto-update toggle for plugin marketplaces
- 3x memory usage improvement for large conversations

**⚠️ Breaking**: Removed `#` shortcut for quick memory entry

### v2.0.67 (2025-12-26) ⭐

- ⭐ **Thinking mode enabled by default for Opus 4.5**
- Thinking config moved to `/config`
- Search in `/permissions` with `/` shortcut

### v2.0.64 (2025-12-22) ⭐

- ⭐ **Instant auto-compacting**
- ⭐ **Async agents and bash commands** with wake-up messages
- `/stats` with usage graphs, streaks, favorite model
- Named sessions: `/rename`, `/resume <name>`
- Support for `.claude/rules/` directory
- Image dimension metadata for coordinate mappings

### v2.0.60 (2025-12-18) ⭐

- ⭐ **Background agents** — Agents run while you work
- `--disable-slash-commands` CLI flag
- Model name in Co-Authored-By commits
- `/mcp enable|disable [server-name]`

### v2.0.51 (2025-12-10) ⭐ MAJOR

- ⭐ **Opus 4.5 released**
- ⭐ **Claude Code for Desktop**
- Updated usage limits for Opus 4.5
- Plan Mode builds more precise plans

### v2.0.45 (2025-12-05) ⭐

- ⭐ **Microsoft Foundry support**
- `PermissionRequest` hook for auto-approve/deny
- `&` prefix for background tasks to web

### v2.0.28 (2025-11-18) ⭐

- ⭐ **Plan mode: introduced Plan subagent**
- Subagents: resume capability
- Subagents: dynamic model selection
- `--max-budget-usd` flag (SDK)
- Git-based plugins branch/tag support (`#branch`)

### v2.0.24 (2025-11-10)

- Claude Code Web: Web → CLI teleport
- Sandbox mode for BashTool (Linux & Mac)
- Bedrock: `awsAuthRefresh` output display

---

## Breaking Changes Summary

### URLs

| Version | Change |
|---------|--------|
| v2.1.0, v2.1.7 | OAuth/API Console: `console.anthropic.com` → `platform.claude.com` |

### Windows

| Version | Change |
|---------|--------|
| v2.0.58 | Managed settings prefer `C:\Program Files\ClaudeCode` |
| v2.1.2 | Deprecated `C:\ProgramData\ClaudeCode` path |

### SDK / Agent Tool

| Version | Change |
|---------|--------|
| v2.0.25 | Removed legacy SDK entrypoint → `@anthropic-ai/claude-agent-sdk` |
| v2.1.0 | Minimum zod peer dependency: `^4.0.0` |
| v2.1.77 | `Agent` tool no longer accepts `resume` parameter — use `SendMessage({to: agentId})` instead |

### API Ecosystem

| Date | Feature |
|------|---------|
| 2026-01-29 | **Structured Outputs GA**: `output_config.format` remplace `output_format`. [Docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) |
| 2026-04-30 | **1M context beta retired**: `context-1m-2025-08-07` header no longer accepted for Sonnet 4.5/4 — requests >200k tokens error. Migrate to Sonnet 4.6 or Opus 4.6. |

### Shortcuts

| Version | Change |
|---------|--------|
| v2.0.70 | Removed `#` shortcut for quick memory entry |

### Security Fixes

| Version | Issue |
|---------|-------|
| v2.1.2 | Command injection in bash command processing |
| v2.1.6 | Shell line continuation permission bypass |
| v2.1.7 | Wildcard permission rules compound commands |
| v2.1.38 | Heredoc delimiter command smuggling prevention |

### Syntax

| Version | Change |
|---------|--------|
| v2.1.19 | Indexed argument syntax changed: `$ARGUMENTS.0` → `$ARGUMENTS[0]` (bracket syntax) |

---

## Milestone Features

| Version | Key Features |
|---------|--------------|
| **v2.1.69** | InstructionsLoaded hook, 4 security fixes, 15+ memory fixes, Voice STT 20 languages |
| **v2.1.68** | ultrathink re-introduced, Opus 4.6 medium effort default, Opus 4/4.1 removed |
| **v2.1.63** | HTTP hooks, worktree config sharing, /simplify + /batch bundled commands |
| **v2.1.32** | Opus 4.6, Agent teams preview, Automatic memory |
| **v2.1.18** | Customizable keyboard shortcuts with /keybindings |
| **v2.1.16** | New task management system with dependency tracking |
| **v2.1.0** | Skill hot-reload, Shift+Enter OOTB, Vim motions, /plan command |
| **v2.0.74** | LSP tool for code intelligence |
| **v2.0.72** | Claude in Chrome (browser control) |
| **v2.0.67** | Thinking mode default for Opus 4.5 |
| **v2.0.64** | Instant auto-compact, async agents, named sessions |
| **v2.0.60** | Background agents |
| **v2.0.51** | Opus 4.5, Claude Code for Desktop |
| **v2.0.45** | Microsoft Foundry, PermissionRequest hook |
| **v2.0.28** | Plan subagent, subagent resume/model selection |
| **v2.0.24** | Web teleport, Sandbox mode |

---

## Updating This Document

1. **Watch**: [github.com/anthropics/claude-code/releases](https://github.com/anthropics/claude-code/releases)
2. **Update**: `machine-readable/claude-code-releases.yaml` (source of truth)
3. **Regenerate**: Update this markdown accordingly
4. **Sync landing**: Run `./scripts/check-landing-sync.sh`

---

*Last updated: 2026-03-05 | [Back to main guide](./ultimate-guide.md)*
