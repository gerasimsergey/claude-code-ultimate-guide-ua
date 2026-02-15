# Commit Categorization Rules

This document defines how to categorize commits based on Conventional Commits format.

## Primary Categories

### Features (`feat:`)
**CHANGELOG**: Nouvelles Fonctionnalites
**Slack**: Yes - always include
**Examples**:
- `feat(session): add parent report system`
- `feat(activity): add multi-level topics`
- `feat(search): add accent-insensitive search`

### Bug Fixes (`fix:`)
**CHANGELOG**: Corrections de Bugs
**Slack**: Yes - if user-facing; No - if internal
**Examples**:
- `fix(session): correct status transition` -> Include in Slack
- `fix(test): correct mock setup` -> Do NOT include in Slack

### Performance (`perf:`)
**CHANGELOG**: Ameliorations Techniques > Performance
**Slack**: Yes - simplified ("Performances ameliorees")
**Examples**:
- `perf(loader): optimize N+1 queries with batching`
- `perf(build): reduce bundle size by 30%`

### Security (`security:` or `fix(security):`)
**CHANGELOG**: Securite
**Slack**: Yes - always, with appropriate detail level
**Examples**:
- `security: fix CVE-2025-55182 React2Shell RCE`
- `fix(security): prevent XSS in chat messages`

## Secondary Categories (CHANGELOG only)

### Refactoring (`refactor:`)
**CHANGELOG**: Ameliorations Techniques > Architecture
**Slack**: No
**Examples**:
- `refactor(hooks): migrate to new pattern`
- `refactor(permissions): extract to service layer`

### Documentation (`docs:`)
**CHANGELOG**: Documentation (if significant)
**Slack**: No
**Examples**:
- `docs: update CLAUDE.md with new patterns`
- `docs(api): add tRPC endpoint documentation`

### Tests (`test:`)
**CHANGELOG**: Tests (count only)
**Slack**: No
**Examples**:
- `test(activity): add prompt resolver tests`
- `test(e2e): add session workflow tests`

### Chores (`chore:`)
**CHANGELOG**: No (unless significant)
**Slack**: No
**Examples**:
- `chore: update dependencies`
- `chore(ci): fix workflow permissions`

### Style (`style:`)
**CHANGELOG**: No
**Slack**: No
**Examples**:
- `style: apply prettier formatting`
- `style(eslint): fix linting errors`

## Scope Patterns

Common scopes in Methode Aristote:

| Scope | Area |
|-------|------|
| `session` | Session management |
| `activity` | Activities and prompts |
| `chat` | Chat and AI features |
| `user` | User management |
| `auth` | Authentication |
| `visio` | Video conferencing |
| `training` | Training/Formation system |
| `admin` | Admin panel |
| `calendar` | Calendar and scheduling |
| `permissions` | Permission system |
| `db` | Database and migrations |
| `api` | API endpoints |
| `ui` | UI components |

## Breaking Changes

Indicated by `!` after type/scope or `BREAKING CHANGE:` in footer:
- `feat(api)!: change session status enum`
- `fix(auth)!: require new token format`

**CHANGELOG**: Breaking Changes section
**Slack**: Yes - with migration instructions

## PR Number Extraction

Extract PR numbers from:
1. Commit message: `(#123)`
2. Merge commit: `Merge pull request #123`
3. GitHub API: cross-reference with commit SHA

## Sentry Issue Linking

Match patterns:
- `Sentry: METHODE-ARISTOTE-APP-XX`
- `fixes METHODE-ARISTOTE-APP-XX`
- `closes #XX` (GitHub issue)

## Statistics Calculation

Count for release stats:
- **PRs**: Unique PR numbers
- **Features**: `feat:` commits
- **Bugs**: `fix:` commits (excluding test/internal)
- **Improvements**: `perf:` + `refactor:` + UI improvements
- **Security**: `security:` commits
- **Breaking**: Commits with `!` or `BREAKING CHANGE`