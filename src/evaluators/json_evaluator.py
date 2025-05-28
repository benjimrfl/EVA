import json

def evaluate_json(expected_result, generated_result):
    """
    Evalúa si el campo 'pattern' del JSON generado coincide con el del expected_result.
    Ambos parámetros pueden ser dicts o strings JSON.
    """
    # Asegurar que ambos parámetros son diccionarios
    if isinstance(expected_result, str):
        try:
            expected_result = json.loads(expected_result)
        except json.JSONDecodeError:
            return 'fail'
    
    if isinstance(generated_result, str):
        try:
            generated_result = json.loads(generated_result)
        except json.JSONDecodeError:
            return 'fail'
    
    # Extraer y comparar los campos 'pattern'
    expected_pattern = expected_result.get("pattern", "").strip().lower()
    generated_pattern = generated_result.get("pattern", "").strip().lower()
    if('method' in generated_pattern):
        generated_pattern = generated_pattern.replace('method', '')
    
    return 'pass' if expected_pattern == generated_pattern else 'fail'
