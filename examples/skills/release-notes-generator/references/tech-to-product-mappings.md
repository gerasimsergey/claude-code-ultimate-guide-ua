# Tech-to-Product Transformation Rules

This document defines how to transform technical commit messages into user-friendly product language.

## Transformation Categories

### 1. COMMUNICATE (Transform to product language)

| Technical Pattern | Product Message |
|-------------------|-----------------|
| `N+1 queries`, `DataLoader`, `batching` | "Chargement plus rapide des listes" |
| `embeddings`, `vector search`, `pgvector` | "Recherche intelligente amelioree" |
| `permissions`, `scope`, `access control` | "Correction d'un bug d'acces" |
| `retry logic`, `resilience`, `P1001` | "Meilleure stabilite de connexion" |
| `SSE`, `real-time`, `WebSocket` | "Mises a jour en temps reel" |
| `cache`, `memoization` | "Performances ameliorees" |
| `responsive`, `mobile` | "Meilleure experience mobile" |
| `accessibility`, `a11y`, `WCAG` | "Accessibilite amelioree" |
| `Sentry`, `monitoring`, `alerting` | "Meilleur suivi des erreurs" |
| `validation`, `sanitization` | "Securite renforcee" |

### 2. DO NOT COMMUNICATE (Internal/Technical only)

These patterns should NOT appear in Slack announcements:

| Technical Pattern | Reason |
|-------------------|--------|
| `refactor`, `refactoring` | Internal code quality |
| `webpack`, `turbopack`, `bundler` | Build tooling |
| `eslint`, `prettier`, `linting` | Code style |
| `kebab-case`, `naming convention` | Internal standards |
| `TypeScript`, `type safety` | Developer experience |
| `test`, `spec`, `coverage` | Testing infrastructure |
| `chore`, `maintenance` | Routine maintenance |
| `docs`, `documentation` | Internal docs |
| `deps`, `dependencies`, `bump` | Dependency updates |
| `CI`, `CD`, `workflow` | DevOps infrastructure |

### 3. SECURITY (Always communicate, simplified)

| Technical | Product |
|-----------|---------|
| `CVE-XXXX-XXXXX` | "Correction d'une vulnerabilite de securite" |
| `XSS`, `injection` | "Renforcement de la protection des donnees" |
| `authentication`, `auth bypass` | "Securite de connexion amelioree" |
| `CORS`, `CSRF` | "Protection contre les attaques web" |

## Context-Aware Transformations

### Session-related
- "Fix session status transition" -> "Correction du suivi des seances"
- "Add session conflict detection" -> "Detection automatique des conflits de planning"
- "Improve visio sync" -> "Synchronisation video amelioree"

### User-related
- "Fix user profile access" -> "Correction de l'acces aux profils"
- "Add accent-insensitive search" -> "Recherche amelioree (accents non sensibles)"
- "Improve user loader performance" -> "Chargement des utilisateurs plus rapide"

### Activity-related
- "Fix activity prompt resolution" -> "Correction de l'affichage des activites"
- "Add multi-level topics" -> "Organisation des activites par niveau amelioree"
- "Improve embeddings generation" -> "Recherche d'activites similaires amelioree"

### Chat-related
- "Fix streaming race condition" -> "Stabilite du chat amelioree"
- "Add vocal history" -> "Historique des messages vocaux"
- "Prevent empty messages" -> "Correction des messages vides"

## Role-Based Impact

Always specify who is affected:

| Impact | Roles |
|--------|-------|
| Dashboard changes | Tuteurs, Eleves, Admin |
| Session management | Tuteurs, Admin |
| Activity library | Tuteurs, Admin |
| Chat/AI features | Tuteurs, Eleves |
| Admin panel | Admin only |
| Billing/Payment | Admin, Parents |
| Reports/Analytics | Admin, Tuteurs |

## Severity Indicators

Use these prefixes when appropriate:

- **Critique** : Production-blocking issues
- **Important** : User-facing bugs
- **Mineur** : Quality of life improvements
- *Ne pas mentionner* : Internal fixes
