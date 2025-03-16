def validate_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("El valor debe ser mayor a 0. Intenta nuevamente.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")
