# sovaia-automations — Claude Code Instructions

## What This Repo Is

Workflows, orchestration, document renderers and templates for the
Sovereign AI Platform (L2). Contains the document rendering pipeline,
workflow/automation tooling, and output templates.

---

## Design Principles (Non-Negotiable)

See `sovaia-contracts/architecture/principles.md` for full details.

1. **Strict Isolation.** Every component works independently.
2. **Interface Contract.** Explicit APIs between components.
3. **Orchestrator Exclusivity.** Only orchestrators know dependencies.
4. **Semantic & Ontological Data.** Enrich data semantically where possible.
5. **Lean, Effective, Efficient.** Minimal complexity for maximum value.

---

## Layer Model

This repo is **L2 (Orchestration & Automation)** in the platform layer model.

**Dependency rules:**
- L2 may use: L3 (AI Services), L1 (Platform Infrastructure)
- L2 must NOT use: L5 (Applications), L6 (Tenants)
- L2 is consumed by: L5 (Applications), L4 (Plugins)

---

## Decision Authority

The user is the architect. Claude implements.

**Hard rule — STOP and ask when:**
- New workflow or orchestrator design
- Renderer output format changes
- Template structure changes affecting multiple brands
- Integration with external systems (N8N, APIs)
- Changes that affect document output quality

**Claude may decide autonomously:**
- Bug fixes within existing patterns
- Code formatting and style
- Template syntax fixes
- Commit message wording

---

## Key Components

### Document Renderer (existing)
- `src/pipeline.py` — Main rendering pipeline
- `config/brands/` — Per-brand configuration
- `config/document-types/` — Document type definitions (angebot, konzept, etc.)
- `examples/` — Example documents per brand
- `build/` — Assembled output documents

### Renderers
- `renderers/markdown-to-pdf/` — Markdown to PDF conversion
- `renderers/markdown-to-word/` — Markdown to DOCX conversion
- `renderers/markdown-to-pptx/` — Markdown to PowerPoint conversion

### Templates
- `templates/markdown-styles/` — Markdown style definitions
- `templates/renderer-templates/` — PDF, Word, PowerPoint templates

### Workflows & Orchestration
- `workflows/` — N8N workflow definitions
- `orchestrators/` — Agent orchestrator, pipeline manager
- `monitors/` — Agent monitor, pipeline monitor

---

## Forbidden Patterns

- Renderers must not contain business logic — they transform, not decide
- Templates must not be stored in sovaia-data-packages (they belong here)
- No direct database access — use AI Services (L3) APIs
- No hardcoded brand names — use config/brands/ for brand-specific settings
- No secrets or credentials in config files
- Force-pushing to main

---

## Working Mode

1. **Read before editing.** Always read a file before modifying it.
2. **One concern per commit.** Don't mix renderer changes with workflow changes.
3. **Brand configs follow patterns.** Use `config/brands/{brand-key}/brand.yaml`.
4. **Renderers are tools.** Triggered via workflows or API — not user-facing.

---

## Related Repositories

| Repo | Layer | Relationship |
|------|-------|-------------|
| `sovaia-contracts` | L0 | API specs, architecture guidelines |
| `sovaia-platform` | L1 | Infrastructure (consumed by this repo) |
| `sovaia-ai-services` | L3 | AI Services (consumed by workflows/orchestrators) |
| `sovaia-web-core` | L5 | CMS (may trigger renderers) |
| `sovaia-deployments` | -- | Helm values for deployment |
