def parse_expression(expression: str) -> dict:
    # Paso 1: Extraer el nombre de la función antes del primer "(")
    func_name = expression.split("(")[0]
    
    # Paso 2: Extraer los argumentos
    args_str = expression[len(func_name)+1 : -1]
    
    # Paso 3: Separar los argumentos por comas
    args = args_str.split(",")
    
    # (Faltaría: manejar espacios, validar errores y creo que ya)
    
    return {
        "func_name": func_name,
        "args": [arg.strip() for arg in args]  # Limpia espacios
    }