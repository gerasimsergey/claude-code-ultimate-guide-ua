# Slack Announcement Template

Use this template for generating product-focused Slack messages.

```
Version X.Y.Z - Deployee en production

PR : [URL de la PR de release, ex: https://github.com/methode-aristote/app/pull/XXX]

En bref : [Phrase decrivant l'objectif principal de cette release]

---

Nouvelles fonctionnalites

[Nom Feature 1]
> [Description en 1-2 phrases de ce que ca apporte aux utilisateurs]
> Qui est concerne : [Tuteurs / Eleves / Admin / Tous]

[Nom Feature 2]
> [Description en 1-2 phrases]
> Qui est concerne : [Roles]

---

Corrections importantes

- [Description du bug corrige en langage utilisateur]
- [Description du bug corrige en langage utilisateur]

---

Ameliorations

- [Amelioration UX/UI ou workflow en langage utilisateur]
- [...]

---

En chiffres

- X nouvelles fonctionnalites
- Y bugs corriges
- Z ameliorations

---

Questions ? Contactez @florian ou l'equipe tech
```

## Guidelines

### A FAIRE
- Utiliser un langage accessible (pas de jargon technique)
- Focus sur l'impact utilisateur
- Etre concis (max 10 lignes par section)
- Utiliser des emojis avec parcimonie

### A EVITER
- "Implementation du pattern DataLoader pour resoudre les N+1 queries"
- "Refactorisation complete du systeme de permissions avec scope ANY/ASSIGNED"
- "Migration de webpack vers Turbopack"

### Transformation Tech -> Produit

| Technique | Produit |
|-----------|---------|
| Optimisation N+1 queries avec DataLoader | Chargement plus rapide des listes d'utilisateurs et de sessions |
| Implementation embeddings AI avec pgvector | Nouvelle recherche intelligente d'activites similaires |
| Correction scope permissions dans getPermissionScope() | Correction d'un bug qui empechait certains utilisateurs d'acceder a leurs sessions |
| Migration vers kebab-case pour les fichiers | *Ne pas communiquer (purement technique)* |
| Fix Prisma P1001 avec retry logic | Meilleure stabilite de connexion a la base de donnees |
| Add Sentry monitoring for orphan chats | Detection automatique des conversations orphelines |

### Sections Optionnelles

Si la release contient des elements importants, ajouter:

Points d'attention
- [Information importante que les utilisateurs doivent savoir]
- [Changement de comportement qu'ils pourraient remarquer]

A venir prochainement
- [Teaser de la prochaine grosse feature]
- [Feature en cours de developpement qui arrive bientot]
