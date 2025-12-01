def calcular_imc(peso_kg, altura_m):
    """Calcula o Índice de Massa Corporal."""
    if altura_m <= 0: return 0
    return round(peso_kg / (altura_m ** 2), 2)

def calcular_agua(peso_kg):
    """Calcula meta de água (35ml por kg)."""
    return round(peso_kg * 0.035, 2)

def classificar_imc(imc):
    if imc < 18.5: return "Abaixo do peso"
    if imc < 24.9: return "Peso normal"
    if imc < 29.9: return "Sobrepeso"
    return "Obesidade"