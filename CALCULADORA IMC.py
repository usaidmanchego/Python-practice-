"""
imc.py
Calcula el IMC en adultos y muestra la categoría.
"""

def calcular_imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura)
    except Exception:
        return "Error: ingresa valores numéricos válidos."

    if peso <= 0 or altura <= 0:
        return "Error: peso y altura deben ser mayores que 0."

    imc = peso / (altura * altura)

    # Clasificación OMS simplificada
    if imc < 18.5:
        return f"IMC: {imc:.2f} → Bajo peso"
    elif 18.5 <= imc <= 24.9:
        return f"IMC: {imc:.2f} → Normal"
    elif 25 <= imc <= 29.9:
        return f"IMC: {imc:.2f} → Sobrepeso"
    else:
        return f"IMC: {imc:.2f} → Obesidad"

def main():
    print("Medidor de IMC en adultos")
    p = input("Tu peso en kg: ")
    h = input("Tu altura en metros: ")
    resultado = calcular_imc(p, h)
    print(resultado)

if __name__ == "__main__":
    main()
