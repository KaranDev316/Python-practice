from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "notes.json"

def load_data():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)