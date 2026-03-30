# sovaia-automations — Claude Code Instructions

## What This Repo Is

Workflows, orchestration, document renderers and templates for the Sovereign AI Platform (L2).
Contains both the document rendering pipeline and workflow/automation tooling.

## Key Components

### Document Renderer (existing)
- `src/pipeline.py` — Main rendering pipeline
- `config/brands/` — Per-brand configuration
- `config/document-types/` — Document type definitions (angebot, konzept, etc.)
- `examples/` — Example documents per brand

### Renderers (planned)
- `renderers/markdown-to-pdf/` — Markdown to PDF conversion
- `renderers/markdown-to-word/` — Markdown to DOCX conversion
- `renderers/markdown-to-pptx/` — Markdown to PowerPoint conversion

### Templates
- `templates/markdown-styles/` — Markdown style definitions
- `templates/renderer-templates/` — Output format templates (PDF, Word, PPTX)

### Workflows & Orchestration (planned)
- `workflows/` — N8N workflow definitions
- `orchestrators/` — Agent orchestrator, pipeline manager
- `monitors/` — Agent monitor, pipeline monitor

## Rules

1. Renderers are triggered via workflows or API — they are tools, not user-facing.
2. Templates belong with their renderers, not in data-packages.
3. Brand configs follow the pattern in `config/brands/{brand-key}/brand.yaml`.
