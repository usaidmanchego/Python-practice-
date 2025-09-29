"""
tabla_multiplicar.py
Pide un número y muestra su tabla de multiplicar del 1 al 10.
"""

def mostrar_tabla(n):
    try:
        n = int(n)  # Convertimos la entrada a entero
    except Exception:
        return "Error: ingresa un número válido."

    tabla = []
    for i in range(1, 11):
        resultado = n * i
        tabla.append(f"{n} x {i} = {resultado}")
    return "\n".join(tabla)

def main():
    numero = input("Ingresa un número entero: ")
    salida = mostrar_tabla(numero)
    print(salida)

if __name__ == "__main__":
    main()
