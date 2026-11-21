#!/usr/bin/env python3
"""
Automated Skill Synchronizer for skills-library repository.
Use this script whenever a new skill is added in any conversation.
"""

import argparse
import os
import re
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
ROOT_README = REPO_ROOT / "README.md"

def build_skill_readme(skill_id, display_name, category, author, source_name, source_url, what_it_does, how_it_does, triggers):
    trigger_list = "\n".join([f"- `{t.strip()}`" for t in triggers if t.strip()])
    return f"""# {display_name} (`{skill_id}`)

> **Categoría**: {category}  
> **Autor / Creador**: {author}  
> **Fuente de origen**: [{source_name}]({source_url})

---

## 📌 ¿Qué hace este Skill?

{what_it_does}

---

## ⚙️ ¿Cómo lo hace?

{how_it_does}

---

## 🔗 Referencia a la Fuente

- **Origen**: {source_name}
- **Enlace oficial**: [{source_url}]({source_url})
- **Autoría**: {author}

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

{trigger_list}

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
"""

def add_skill(skill_id, src_path, display_name, category, author, source_name, source_url, what_it_does, how_it_does, triggers, git_push=True):
    target_dir = SKILLS_DIR / skill_id
    target_dir.mkdir(parents=True, exist_ok=True)
    src = Path(src_path)

    if not src.exists():
        raise FileNotFoundError(f"Source path {src_path} does not exist.")

    print(f"Copiando archivos desde {src} hacia {target_dir}...")
    if src.is_file():
        shutil.copy2(src, target_dir / "SKILL.md")
    else:
        for item in src.iterdir():
            if item.name in [".git", "__pycache__", "node_modules"]:
                continue
            dest = target_dir / item.name
            if item.is_dir():
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)

    # Ensure SKILL.md exists
    if not (target_dir / "SKILL.md").exists():
        for candidate in target_dir.glob("*.md"):
            if candidate.name.lower() == "skill.md":
                candidate.rename(target_dir / "SKILL.md")
                break

    # Write skill README
    readme_content = build_skill_readme(skill_id, display_name, category, author, source_name, source_url, what_it_does, how_it_does, triggers)
    with open(target_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"README.md generado para {skill_id}.")

    # Update Root README
    update_root_readme(skill_id, display_name, category, source_name, source_url, what_it_does)

    if git_push:
        print("Sincronizando con Git...")
        subprocess.run(["git", "add", "."], cwd=REPO_ROOT, check=True)
        commit_msg = f"feat(skills): add {skill_id} to library"
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_ROOT, check=True)
        print(f"✅ Skill {skill_id} subido exitosamente a GitHub.")

def update_root_readme(skill_id, display_name, category, source_name, source_url, what_it_does):
    content = ROOT_README.read_text(encoding="utf-8")
    
    # Check if already present
    if f"`{skill_id}`" in content:
        print(f"El skill {skill_id} ya se encuentra catalogado en el README principal.")
        return

    # Short summary
    full_desc = what_it_does.strip()
    sentences = re.split(r'\.\s+(?=[A-ZÁÉÍÓÚÑ0-9])', full_desc)
    desc_short = (sentences[0].rstrip('.') + '.') if sentences else full_desc
    desc_short = desc_short.replace('|', '\\|')

    new_row = f"| **`{skill_id}`** | {desc_short} | [{source_name}]({source_url}) | [Ver README](./skills/{skill_id}/README.md) |\n"

    # Search for Category section
    cat_header = f"### 📂 {category}"
    if cat_header in content:
        # Insert after table header
        parts = content.split(cat_header)
        table_part = parts[1]
        # Find separator line
        table_lines = table_part.split("\n")
        insert_idx = -1
        for idx, line in enumerate(table_lines):
            if line.startswith("| :---"):
                insert_idx = idx + 1
                break
        if insert_idx != -1:
            table_lines.insert(insert_idx, new_row.strip())
            new_table_part = "\n".join(table_lines)
            content = parts[0] + cat_header + new_table_part
    else:
        # Append new category before instructions section
        split_marker = "## 🚀 Cómo Usar e Instalar estos Skills"
        new_cat_section = f"### 📂 {category}\n\n| Skill | Descripción Breve | Fuente / Autor | Documentación |\n| :--- | :--- | :--- | :--- |\n{new_row}\n\n"
        if split_marker in content:
            content = content.replace(split_marker, new_cat_section + "---\n\n" + split_marker)
        else:
            content += "\n\n" + new_cat_section

    ROOT_README.write_text(content, encoding="utf-8")
    print("README.md principal actualizado.")

def main():
    parser = argparse.ArgumentParser(description="Add or update a skill in skills-library")
    parser.add_argument("--id", required=True, help="Skill identifier (folder name)")
    parser.add_argument("--path", required=True, help="Path to the skill directory or SKILL.md file")
    parser.add_argument("--display-name", required=True, help="Display title of the skill")
    parser.add_argument("--category", default="Community & Custom Skills", help="Category name")
    parser.add_argument("--author", default="Community / Open Source", help="Author name")
    parser.add_argument("--source-name", required=True, help="Source name (e.g. GitHub repo name)")
    parser.add_argument("--source-url", required=True, help="Source URL")
    parser.add_argument("--what-it-does", required=True, help="Summary of what the skill does")
    parser.add_argument("--how-it-does", required=True, help="Detailed technical summary of how it works")
    parser.add_argument("--triggers", nargs="+", default=[], help="Trigger keywords")
    parser.add_argument("--no-push", action="store_true", help="Do not git commit and push")

    args = parser.parse_args()
    add_skill(
        skill_id=args.id,
        src_path=args.path,
        display_name=args.display_name,
        category=args.category,
        author=args.author,
        source_name=args.source_name,
        source_url=args.source_url,
        what_it_does=args.what_it_does,
        how_it_does=args.how_it_does,
        triggers=args.triggers,
        git_push=not args.no_push
    )

if __name__ == "__main__":
    main()
