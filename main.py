from validator import validate_semantic_integrity
        from engine import SemanticEngine

def run():
    print("--- PoS-Align Nodo Iniciado ---")
    engine = SemanticEngine()
    test_data = "Necesito comida en Zaragoza"
    
    is_valid, msg = validate_semantic_integrity(test_data)
    
    if is_valid:
        print(f"Estado: {msg}")
        print(f"Engine: {engine.find_alignment('Ayuda Básica', 'Recurso Local')}")
    else:
        print(f"ALERTA: {msg}")

if __name__ == "__main__":
    run()
