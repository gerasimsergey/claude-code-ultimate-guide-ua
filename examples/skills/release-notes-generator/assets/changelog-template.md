# CHANGELOG Section Template

Use this template for generating CHANGELOG.md entries.

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Objectif
[Resume en 1-2 phrases de cette release]

### Nouvelles Fonctionnalites

#### [Feature Name] (#PR_NUMBER)
- **Description** : [Description fonctionnelle claire]
- **Spec Notion** : [Lien vers la spec si disponible]
- **Composants impactes** : `component-a`, `service-b`, etc.
- **Impact** : [Qui est concerne : Tuteurs / Eleves / Admin / Tous]

### Corrections de Bugs

#### [Module/Composant] (#PR_NUMBER)
- **Issue** : [Description du bug]
- **Cause** : [Cause racine identifiee]
- **Fix** : [Description de la correction]
- **Sentry** : METHODE-ARISTOTE-APP-XX (si applicable)

### Ameliorations Techniques

#### Performance
- [Description optimisation avec impact mesurable si possible]

#### UI/UX
- [Description amelioration interface]

#### Architecture
- [Description refactoring important]

### Securite
- **[CVE-XXXX-XXXXX]** : [Description et impact]

### Migrations Base de Donnees

#### Processus de Deploiement

**Etape 1 : Appliquer les migrations Prisma**
```bash
pnpm prisma migrate deploy
```

**Etape 2 : Scripts de data migration** (si applicable)
```bash
pnpm dotenv -e .env.production -- tsx scripts/db/migrations/[script-name].ts
```

**Verification post-migration**
```sql
-- Requetes de verification
SELECT COUNT(*) FROM [table];
```

### Breaking Changes

**Aucun** ou:

- **[Composant/API]** : Description du breaking change
  - **Migration requise** : Comment migrer
  - **Impact** : Qui est affecte

### Deprecations

**Aucune** ou:

- **[Fonctionnalite X]** : Depreciee dans cette version
  - **Raison** : Pourquoi
  - **Alternative** : Quoi utiliser a la place
  - **Suppression prevue** : Version X.Y.Z

### Tests
- [X] tests unitaires pour [feature]
- [X] tests d'integration pour [module]

### Statistiques
- **PRs** : #XX, #YY, #ZZ
- **Fichiers impactes** : XX+
- **Nouvelles tables** : [liste si applicable]
- **Migrations Prisma** : X migrations
- **Breaking changes** : 0

### Liens
- PR: https://github.com/methode-aristote/app/pull/XXX
- PRs incluses : #XX, #YY, #ZZ
- Issues Sentry : METHODE-ARISTOTE-APP-XX
```
