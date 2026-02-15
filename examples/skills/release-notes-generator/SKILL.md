---
name: release-notes-generator
description: Generate release notes in 3 formats (CHANGELOG.md, PR body, Slack announcement) from git commits. Automatically categorizes changes and converts technical language to user-friendly messaging. Use when preparing a production release.
---

# Release Notes Generator

Generate comprehensive release notes in 3 formats from git commits, optimized for the Methode Aristote project workflow.

## When to Use This Skill

- Preparing a production release (develop -> main)
- Creating release PR with proper documentation
- Generating Slack announcement for stakeholders
- Updating CHANGELOG.md with new version
- Analyzing commits since last release

## What This Skill Does

1. **Analyzes Git History**: Scans commits since last release tag or specified version
2. **Fetches PR Details**: Gets PR titles, descriptions, and labels via `gh api`
3. **Categorizes Changes**: Groups into features, bug fixes, improvements, security, breaking changes
4. **Generates 3 Outputs**:
   - **CHANGELOG.md section** (technical, complete)
   - **PR Release body** (semi-technical, checklist)
   - **Slack message** (product-focused, user-friendly)
5. **Transforms Language**: Converts technical jargon to accessible messaging
6. **Migration Alert**: Displays prominent warning if database migrations are required

## How to Use

### Basic Usage

```
Generate release notes since last release
```

```
Create release notes for version 0.18.0
```

### With Specific Range

```
Generate release notes from v0.17.0 to HEAD
```

### Preview Only

```
Preview release notes without writing files
```

## Output Formats

### 1. CHANGELOG.md Section

Technical format for developers:

```markdown
## [0.18.0] - 2025-12-08

### Objectif
[1-2 sentence summary]

### Nouvelles Fonctionnalites
#### [Feature Name] (#PR)
- **Description**: ...
- **Impact**: ...

### Corrections de Bugs
- **[Module]**: Description (#issue, Sentry ISSUE-XX)

### Ameliorations Techniques
#### Performance / UI/UX / Architecture
- [Description]

### Migrations Base de Donnees
[If applicable]

### Statistiques
- PRs: X
- Features: Y
- Bugs: Z
```

### 2. PR Release Body

Uses template from `.github/PULL_REQUEST_TEMPLATE/release.md`:
- Objective summary
- Features with specs links
- Bug fixes with Sentry references
- Improvements by category
- Migration instructions
- Deployment checklist

### 3. Slack Announcement

Product-focused format from `.github/COMMUNICATION_TEMPLATE/slack-release.md`:
- **PR link** included for traceability
- Non-technical language
- Focus on user impact (tuteurs, eleves, admin)
- Emojis for readability
- Statistics summary

## Workflow Integration

This skill integrates with the release workflow in CLAUDE.md Section VI.5:

```
1. Analyze commits: git log <last-tag>..HEAD
2. Determine version number (MAJOR.MINOR.PATCH)
3. Generate 3 outputs
4. Create PR develop -> main with "Release" label
5. Update CHANGELOG.md
6. After merge: create git tag
7. Generate Slack announcement
```

## Tech-to-Product Transformation

The skill automatically transforms technical language:

| Technical | Product |
|-----------|---------|
| "Optimisation N+1 queries avec DataLoader" | "Chargement plus rapide des listes" |
| "Implementation embeddings AI avec pgvector" | "Nouvelle recherche intelligente d'activites" |
| "Correction scope permissions dans getPermissionScope()" | "Correction d'un bug d'acces aux sessions" |
| "Migration webpack -> Turbopack" | *Ne pas communiquer* |
| "Refactorisation hooks React" | *Ne pas communiquer* |
| "Fix N+1 in user loaders" | "Amelioration des performances" |
| "Add retry logic for Prisma P1001" | "Meilleure stabilite de connexion" |

## Commit Categories

Commits are categorized by conventional commit prefix:

| Prefix | Category | Include in Slack? |
|--------|----------|-------------------|
| `feat:` | Nouvelles Fonctionnalites | Yes |
| `fix:` | Corrections de Bugs | Yes (if user-facing) |
| `perf:` | Performance | Yes (simplified) |
| `security:` | Securite | Yes |
| `refactor:` | Architecture | No |
| `chore:` | Maintenance | No |
| `docs:` | Documentation | No |
| `test:` | Tests | No |
| `style:` | Style | No |

## Console Output Format

When generating release notes, ALWAYS display a clear summary in the console with:

### Migration Alert (CRITICAL)

If migrations are detected, display prominently:

```
╔══════════════════════════════════════════════════════════════════╗
║  ⚠️  [ATTENTION] MIGRATIONS BASE DE DONNÉES REQUISES             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Cette release contient X migration(s) Prisma :                  ║
║                                                                  ║
║  • 20251210123456_add_activity_description                       ║
║  • 20251211094532_update_session_status                          ║
║                                                                  ║
║  Action requise AVANT déploiement :                              ║
║  → Exécuter : pnpm prisma migrate deploy                         ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

If NO migrations:

```
✅ [OK] Aucune migration base de données requise
```

### Detection Method

Check for new migration files since last release:

```bash
# Find new migrations since last tag
git diff <last-tag>..HEAD --name-only -- prisma/migrations/
```

## Example

**User**: "Generate release notes since v0.17.0"

**Output**:

```
Analyzing commits from v0.17.0 to HEAD...

Found:
- 15 commits
- 8 PRs merged
- 2 new features
- 5 bug fixes
- 3 improvements

╔══════════════════════════════════════════════════════════════════╗
║  ⚠️  [ATTENTION] MIGRATIONS BASE DE DONNÉES REQUISES             ║
╠══════════════════════════════════════════════════════════════════╣
║  Cette release contient 1 migration(s) Prisma :                  ║
║  • 20251208143021_add_user_preferences                           ║
║  Action requise : pnpm prisma migrate deploy                     ║
╚══════════════════════════════════════════════════════════════════╝

--- CHANGELOG.md Section ---
[Technical format output]

--- PR Release Body ---
[Semi-technical format output]

--- Slack Announcement ---
[Product-focused format output]

Write to files? (CHANGELOG.md, clipboard for PR/Slack)
```

## Commands Used

```bash
# Get last release tag
git tag --sort=-v:refname | head -n 1

# List commits since tag
git log <tag>..HEAD --oneline --no-merges

# Get PR details
gh api repos/{owner}/{repo}/pulls/{number}

# Get commit details
git show --stat <sha>
```

## Tips

- Run from repository root
- Ensure `gh` CLI is authenticated
- Review generated content before publishing
- Adjust product language for your audience
- Use `--preview` to see output without writing

## Reference Files

- `assets/changelog-template.md` - CHANGELOG section template
- `assets/slack-template.md` - Slack announcement template
- `references/tech-to-product-mappings.md` - Transformation rules
- `references/commit-categories.md` - Categorization rules

## Related Skills

- `github-actions-templates` - For CI/CD workflows
- `changelog-generator` - Original inspiration (ComposioHQ)
