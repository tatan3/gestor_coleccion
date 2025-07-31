"""
GENERADOR DE IDs - SISTEMA SECUENCIAL
"""
import json
from pathlib import Path

RUTA_CONFIG = Path(__file__).parent.parent / "datos/configuracion.json"

def generar_id():
    """Genera IDs consecutivos (0001, 0002, etc.)"""
    try:
        with open(RUTA_CONFIG, 'r+') as f:
            config = json.load(f)
            nuevo_id = config.get("ultimo_id", 0) + 1
            config["ultimo_id"] = nuevo_id
            f.seek(0)
            json.dump(config, f, indent=2)
            return f"{nuevo_id:04d}"  # Formato 4 dígitos con ceros
    except Exception:
        return "0001"  # Valor por defecto si hay error