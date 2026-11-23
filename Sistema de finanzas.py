# SISTEMA DE FINANZAS PERSONALES

print("SISTEMA DE FINANZAS PERSONALES")

# Declaración de variables
ingresos = 0
gastos = 0
ahorro = 0

# Solicitar ingresos del usuario
ingresos = float(input("Ingresa tus ingresos: $"))

# Solicitar gastos
gastos = float(input("Ingresa tus gastos: $"))

# Calcular ahorro
ahorro = ingresos - gastos

# Mostrar ahorro
print("Tu ahorro es: $", ahorro)

# Capturar datos financieros
capital = float(input("Cantidad ahorrada: $"))
tasa = float(input("Tasa de interés (%): "))
tiempo = int(input("Tiempo en años: "))

# Convertir porcentaje a decimal
tasa = tasa / 100

# Calcular interés simple
interes = capital * tasa * tiempo

# Mostrar resultado final
print("Interés ganado: $", interes)
