"""
area_triangulo.py
Pide base y altura de un triángulo y calcula su área.
"""

def calcular_area(base, altura):
    try:
        base = float(base)
        altura = float(altura)
    except Exception:
        return "Error: ingresa valores numéricos válidos."

    if base <= 0 or altura <= 0:
        return "Error: la base y la altura deben ser mayores que 0."

    area = (base * altura) / 2
    return f"El área del triángulo es: {area}"

def main():
    print("Área del triángulo")
    b = input("Base: ")
    h = input("Altura: ")
    resultado = calcular_area(b, h)
    print(resultado)

if __name__ == "__main__":
    main()

