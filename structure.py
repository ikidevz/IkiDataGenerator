from pathlib import Path
import json

# =========================================================
# CONFIG
# =========================================================

ROOT_DIR = r"./"

IGNORE = {
    ".git", "__pycache__", ".venv", "venv",
    "node_modules", ".idea", ".vscode",
    "bin", "base_provider.py", "__init__.py",
}

# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    root = Path(ROOT_DIR)

    mapping = {}

    for group_dir in sorted(root.iterdir()):
        if not group_dir.is_dir():
            continue
        if group_dir.name in IGNORE:
            continue

        group = group_dir.name

        for provider_file in sorted(group_dir.glob("*.py")):
            if provider_file.name in IGNORE:
                continue

            key_label = provider_file.stem
            mapping[key_label] = group

    print(json.dumps(mapping, indent=4))
