# sovaia-automations

Sovereign AI Platform — Workflows, Orchestration, Document Renderers & Templates (L2)

## Inhalt

| Verzeichnis | Zweck |
|-------------|-------|
| `src/` | Document Rendering Pipeline (bestehend) |
| `config/` | Brand- und Dokumenttyp-Konfigurationen |
| `renderers/` | Markdown-to-X Renderer (PDF, Word, PowerPoint) |
| `templates/` | Markdown Styles & Renderer-Templates |
| `workflows/` | N8N Workflow Definitions |
| `orchestrators/` | Agent Orchestrator, Pipeline Manager |
| `monitors/` | Agent Monitor, Pipeline Monitor |

## Document Renderer

Nimmt Markdown + Metadaten + strukturierte Daten aus beliebigen Quellen entgegen,
rendert daraus brand- und dokumenttypspezifische Ausgaben und legt die Ergebnisse
konfigurationsgesteuert an definierte Ziele ab.

```
config/brands/{brand}/brand.yaml    → Brand-spezifische Einstellungen
config/document-types/*.yaml        → Dokumenttyp-Definitionen
templates/markdown-styles/          → Markdown Style Definitionen
templates/renderer-templates/       → PDF, Word, PowerPoint Templates
```
