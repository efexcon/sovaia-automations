from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected mapping in YAML file: {path}")
    return data


def load_text(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def build_job(example_root: Path, config_root: Path) -> dict[str, Any]:
    meta = load_yaml(example_root / "meta.yaml")
    brand_key = example_root.parts[-3]
    doc_type = example_root.parts[-2]

    brand = load_yaml(config_root / "brands" / brand_key / "brand.yaml")
    doc_type_cfg = load_yaml(config_root / "document-types" / f"{doc_type}.yaml")

    content_path = example_root / "content.md"
    content = load_text(content_path) if content_path.exists() else ""

    items_path = example_root / "items.json"
    line_items = []
    if items_path.exists():
        with items_path.open("r", encoding="utf-8") as f:
            line_items = json.load(f)

    return {
        "job": {
            "id": meta.get("document_id"),
            "type": doc_type,
            "brand": brand_key,
            "output_formats": ["docx", "pdf"],
        },
        "metadata": meta,
        "brand": brand,
        "document_type": doc_type_cfg,
        "content": content,
        "line_items": line_items,
    }


def assemble_markdown(job_data: dict[str, Any]) -> str:
    meta = job_data["metadata"]
    lines: list[str] = []

    lines.append(f"# {meta.get('title', 'Untitled Document')}")
    lines.append("")
    lines.append(f"**Dokumenten-ID:** {meta.get('document_id', '')}")
    lines.append(f"**Datum:** {meta.get('date', '')}")
    lines.append("")

    sender = meta.get("sender", {}) or {}
    recipient = meta.get("recipient", {}) or {}

    if sender or recipient:
        lines.append("## Parteien")
        lines.append("")
        lines.append(f"**Absender:** {sender.get('company', '')}")
        lines.append(f"**Empfänger:** {recipient.get('company', '')}")
        lines.append("")

    if job_data.get("content"):
        lines.append("## Inhalt")
        lines.append("")
        lines.append(job_data["content"].strip())
        lines.append("")

    line_items = job_data.get("line_items", [])
    if line_items:
        lines.append("## Positionen")
        lines.append("")
        lines.append("| Pos. | Leistung | Menge | Einheit | Einzelpreis |")
        lines.append("| --- | --- | ---: | --- | ---: |")
        for item in line_items:
            lines.append(
                f"| {item.get('position', '')} | {item.get('description', '')} | {item.get('quantity', '')} | {item.get('unit', '')} | {item.get('unit_price', '')} |"
            )
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def run(example_root: str, config_root: str = "config", output_dir: str = "build") -> Path:
    example_path = Path(example_root)
    config_path = Path(config_root)
    build_path = Path(output_dir)
    build_path.mkdir(parents=True, exist_ok=True)

    job_data = build_job(example_path, config_path)
    assembled = assemble_markdown(job_data)

    output_path = build_path / f"{job_data['job']['id']}_assembled.md"
    output_path.write_text(assembled, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Assemble an example document job into markdown")
    parser.add_argument("example_root", help="Path to example job folder")
    parser.add_argument("--config-root", default="config", help="Path to config root")
    parser.add_argument("--output-dir", default="build", help="Path to build output directory")
    args = parser.parse_args()

    out = run(args.example_root, config_root=args.config_root, output_dir=args.output_dir)
    print(out)
