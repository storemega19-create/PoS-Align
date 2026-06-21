# Filtro ético: Inmunidad contra conceptos financieros
PROHIBITED_CONCEPTS = ["precio", "compra", "venta", "token", "valor_monetario", "pago"]

def validate_semantic_integrity(data: str):
    clean_data = data.lower()
    for concept in PROHIBITED_CONCEPTS:
        if concept in clean_data:
            return False, f"Incoherencia semántica: Concepto financiero '{concept}' detectado."
    return True, "Validación superada."
