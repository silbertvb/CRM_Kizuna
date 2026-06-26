# CRM_Kizuna - Módulo 1
# Ficha de influencer

nombre = "Laura Pérez"
platoforma = "Instagram"
seguidores = 85000
engagement = 4.2
email = "laura@ejemplo.com"

print("--------- CRM Kizuna ---------\n")
print(f"{' Nombre:':<12} {nombre}")              #con el uso de ":<12" rellena los espacios y alinea los datos 
print(f"{' Plataforma:':<12} {platoforma}")
print(f"{' Seguidores:':<12} {seguidores:,}")    # podemos añadir ',' para separar la cifra
print(f"{' Engagement:':<12} {engagement}%")
print(f"{' email:':<12} {email}")
print("-" * 30)                                 # se usa "-" * X (veces que se repite el caracter)

# Tarea 2. Solicita por pantalla los datos del influencer con conversion de tipos
nombre1 = input("Introduce Nombre y Apellido: ")
plataforma1 = input("Introduce tu plataforma: ")
seguidores1 = input("Introduce tus seguidores: ")
seguidores1 = int(seguidores1.replace(",", "."))  #convertimos 'seguidores1' en int y se acepta tanto (.) como (,)
engagement1 = input("Introduce engagement: ")
engagement1 = float(engagement1.replace(",", "."))  # Engagement1 — acepta 4.5 o 4,5
email1 = input("Introduce tu e-mail: ")

print(f"------ RESUMEN DATOS --------")
print(f"{' Nombre:':<12} {nombre1}")
print(f"{' Plataforma:':<12} {plataforma1}")
print(f"{' Seguidores:':<12} {seguidores1:,}")
print(f"{' Engagement:':<12} {engagement1}%")
print(f"{' Email:':<12} {email1}")
print(f'-'*30)