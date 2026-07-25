"""
CRM Kizuna — Unidad 1, Lección 1: Ficha de influencer
Certificación: IT Specialist Python (INF-303)

Ejercicios:
  1. Ficha de influencer — (variables, f-strings, alineación :<, separador de miles :,)
  2. Solicitud de datos por teclado — (input, conversión de tipos, str.replace)
"""

# --- Ejercicio/Lección 1 — Ficha de influencer ---
# Qué hace: declara los datos de un influencer y los muestra formateados por pantalla
# Practica: variables, f-strings, alineación (:<), separador de miles (:,)

nombre = "Laura Pérez"
plataforma = "Instagram"
seguidores = 85000
engagement = 4.2
email = "laura@ejemplo.com"

print("--------- CRM Kizuna ---------\n")
print(f"{' Nombre:':<12} {nombre}")              #con el uso de ":<12" rellena los espacios y alinea los datos 
print(f"{' Plataforma:':<12} {plataforma}")
print(f"{' Seguidores:':<12} {seguidores:,}")    # podemos añadir ',' para separar la cifra
print(f"{' Engagement:':<12} {engagement}%")     # sin indicar el tipo de dato, se asume que es un float y se añade el símbolo %
print(f"{' Email:':<12} {email}")
print("-" * 30)                                  # se usa "-" * X (veces que se repite el caracter)

# --- Ejercicio/Lección 2 — Solicitud de datos por teclado ---
# Qué hace: pide por teclado los datos de un influencer y convierte los tipos antes de mostrarlos
# Practica: input(), conversión de tipos (int, float), str.replace()
nombre1 = input("Introduce Nombre y Apellido: ")
plataforma1 = input("Introduce tu plataforma: ")
seguidores1 = input("Introduce tus seguidores: ")
seguidores1 = int(seguidores1.replace(",", "."))  #convertimos 'seguidores1' en int y se acepta tanto (.) como (,)
engagement1 = input("Introduce Engagement: ")
engagement1 = float(engagement1.replace(",", "."))  # Engagement1 — acepta 4.5 o 4,5
email1 = input("Introduce tu e-mail: ")

print(f"------ RESUMEN DATOS --------")
print(f"{' Nombre:':<12} {nombre1}")
print(f"{' Plataforma:':<12} {plataforma1}")
print(f"{' Seguidores:':<12} {seguidores1:,}")
print(f"{' Engagement:':<12} {engagement1}%")
print(f"{' Email:':<12} {email1}")
print(f'-'*30)