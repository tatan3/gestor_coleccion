import json
from pathlib import Path

RUTA_CONFIG = Path(__file__).parent.parent / "datos/configuracion.json"

def generar_id():
    try:
        with open(RUTA_CONFIG, 'r+') as f:
            config = json.load(f)
            nuevo_id = config.get("ultimo_id", 0) + 1
            config["ultimo_id"] = nuevo_id
            f.seek(0)
            json.dump(config, f, indent=2)
            return f"{nuevo_id:04d}"
    except Exception:
        return "0001"