---
title: "Claude Code Workflows"
description: "Step-by-step guides for common development patterns with Claude Code"
tags: [workflow, guide, reference]
---

# Claude Code Workflows

Step-by-step guides for common development patterns with Claude Code.

---

## 🔍 Search & Discovery

### [Search Tools Mastery](./search-tools-mastery.md) ⭐ NEW

**Master the art of code search by combining rg, grepai, Serena & ast-grep**

Learn when to use each tool, how to combine them for maximum efficiency, and real-world workflows including:
- Exploring unknown codebases
- Large-scale refactoring
- Security audits
- Framework migrations
- Performance optimization

**Key Topics**:
- Quick decision matrix
- Complete feature comparison
- 5 combined workflows
- Performance benchmarks
- Common pitfalls
- Tool selection cheatsheet

---

## 🎯 Development Workflows

### [Plan-Driven Development](./plan-driven.md)

Structure complex tasks with planning mode before execution.

**When to use**: Multi-step features, architectural changes, uncertainty about approach

### [TDD with Claude](./tdd-with-claude.md)

Test-Driven Development workflow: write tests first, implement after.

**When to use**: Critical functionality, regression prevention, API design

### [Spec-First Development](./spec-first.md)

Write specifications before code for better requirements clarity.

**When to use**: Team collaboration, complex features, documentation-first projects

### [Iterative Refinement](./iterative-refinement.md)

Improve code through multiple refinement cycles.

**When to use**: Quality improvements, performance optimization, code cleanup

### [Skeleton Projects](./skeleton-projects.md) ⭐ NEW

Use existing battle-tested repositories as scaffolding for new projects.

**When to use**: Starting new projects, standardizing team patterns, rapid prototyping from proven foundations

### [Team AI Instructions](./team-ai-instructions.md)

Scale CLAUDE.md across a multi-developer, multi-tool team with profile-based module assembly.

**When to use**: Team 5+ devs, multiple AI tools (Claude Code + Cursor/Windsurf), mixed OS

---

## 🎨 Design & Content

### [Design to Code](./design-to-code.md)

Convert design mockups (Figma, wireframes) into working code.

**When to use**: Frontend development, UI implementation, design system work

### [PDF Generation](./pdf-generation.md)

Generate professional PDFs using Quarto/Typst with Claude Code.

**When to use**: Reports, documentation, whitepapers, technical documents

### [Talk Preparation Pipeline](./talk-pipeline.md) ⭐ NEW

6-stage skill pipeline: raw material → structured talk → AI-generated slides via Kimi.

**When to use**: Conference talks, meetup presentations, internal tech talks — from article, transcript, or notes

### [TTS Setup](./tts-setup.md)

Configure Text-to-Speech for Claude Code responses (Agent Vibes integration).

**When to use**: Audio feedback, accessibility, hands-free coding

---

## 🔬 Code Exploration

### [Exploration Workflow](./exploration-workflow.md)

Systematically explore and understand unfamiliar codebases.

**When to use**: New projects, legacy code, documentation gaps

**Related**: See [Search Tools Mastery](./search-tools-mastery.md) for advanced multi-tool exploration strategies.

---

## Multi-Agent & Advanced

### [Agent Teams](./agent-teams.md)

Orchestrate multiple specialized agents working in parallel on complex tasks.

**When to use**: Tasks that benefit from parallelism, specialized expertise, or independent verification

### [Agent Teams Quick Start](./agent-teams-quick-start.md)

Fast-track guide to setting up your first agent team in under 30 minutes.

**When to use**: New to multi-agent patterns, want to experiment before committing to full setup

### [Dual-Instance Planning](./dual-instance-planning.md)

Run Opus for planning and Sonnet for execution in two coordinated Claude Code instances.

**When to use**: Complex features needing deep reasoning for architecture, cost-effective execution

### [Event-Driven Agents](./event-driven-agents.md)

Coordinate agents through hook events rather than direct orchestration.

**When to use**: Reactive workflows, hook-triggered automation, loosely-coupled agent pipelines

### [Plan Pipeline](./plan-pipeline.md)

Full end-to-end plan pipeline: /plan-start, /plan-validate, /plan-execute as a coherent workflow.

**When to use**: Any significant feature where planning rigor pays off before writing code

### [Task Management](./task-management.md)

Multi-session task tracking with TodoWrite, tasks API, and context persistence across sessions.

**When to use**: Long-running tasks spanning multiple sessions, team coordination, complex backlogs

---

## Quick Selection Guide

| Your Situation | Recommended Workflow |
|----------------|---------------------|
| **New to codebase** | [Exploration Workflow](./exploration-workflow.md) + [Search Tools Mastery](./search-tools-mastery.md) |
| **Complex feature** | [Plan-Driven](./plan-driven.md) or [Spec-First](./spec-first.md) |
| **Need reliability** | [TDD with Claude](./tdd-with-claude.md) |
| **Large refactoring** | [Search Tools Mastery](./search-tools-mastery.md) |
| **UI implementation** | [Design to Code](./design-to-code.md) |
| **Code quality** | [Iterative Refinement](./iterative-refinement.md) |
| **New project from template** | [Skeleton Projects](./skeleton-projects.md) |
| **Team AI instructions** | [Team AI Instructions](./team-ai-instructions.md) |
| **Documentation** | [PDF Generation](./pdf-generation.md) |
| **Conference talk from raw material** | [Talk Preparation Pipeline](./talk-pipeline.md) |
| **Audio feedback** | [TTS Setup](./tts-setup.md) |
| **Multi-agent tasks** | [Agent Teams](./agent-teams.md) |
| **First agent team** | [Agent Teams Quick Start](./agent-teams-quick-start.md) |
| **Cost-optimized planning** | [Dual-Instance Planning](./dual-instance-planning.md) |
| **Hook-driven automation** | [Event-Driven Agents](./event-driven-agents.md) |
| **Full plan workflow** | [Plan Pipeline](./plan-pipeline.md) |
| **Multi-session tracking** | [Task Management](./task-management.md) |

---

## Contributing

New workflow ideas? Open an issue or PR in the main repository.

**Workflow Template Structure**:
1. Title & Purpose
2. When to Use
3. Prerequisites
4. Step-by-Step Guide
5. Real-World Examples
6. Common Pitfalls
7. Related Workflows

---

**Last updated**: March 2026
