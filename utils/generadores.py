"""
GENERADORES - CREA IDENTIFICADORES ÚNICOS
"""
import uuid

def generar_id():
    """Genera un ID único usando UUID4"""
    return str(uuid.uuid4())