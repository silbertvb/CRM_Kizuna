# ============================================
# LECCIÓN 2: Creacion de lista 
# ============================================


#Paso1- Definición de una Lista anidada de influencers 
"""Cada influencer es una lista con 5 datos dentro de la lista principal
Esto se llama lista anidada."""
influencers = [
    ["Laura Pires", "Instagram", 85000, 3.4, "laura@ejemplo.com"],
    ["Fernando Silva", "Facebook", 815000, 2.7, "fernando@ejemplo.com"],
    ["Pedro Pascal", "Instagram", 285000, 5.4, "pedro@ejemplo.com"]
]

#Paso2 - Muéstralos numerados
print(" === CRM Kizuna - Influencers (Lección inicial) === ")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12} | {influencer[2]:,} seg")
    
print("-" * 50)

#Paso3 - Añade un nuevo influencer
nuevo_influencer = ["Manuel Vega", "Youtube", 1285000, 9.4, "manuel@ejemplo.com"]
influencers.append(nuevo_influencer)          # añadido al final de la lista
print(f"✅ Añadido: {nuevo_influencer[0]}")

#Paso4 - Elimina uno por indice:
eliminado = influencers.pop(1)  #elimina posición (1) Fernando 
print(f"🗑️ Eliminado: {eliminado[0]}")

#Paso 5 - Muestra la lista final:
print("\n --------- Lista Final (2)---------")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12} | {influencer[2]:,} seg")
print(f"\nTotal influencers: {len(influencers)}")


# ============================================
# LECCIÓN 3: Técnicas de manipulación
# ============================================

print(f"\n === Lección 3: Técnicas de manipulación CRM ===")
#P1- Concatenación de listas--
influencers_vip = [
    ["Ana García", "Youtube", 500000, 7.2, "ana@ejemplo.com"],
    ["Luís Martín", "Tiktok", 340000, 8.2, "luis@ejemplo.com"]
]

todos_influencers = influencers + influencers_vip
print("\n ===== Lista completa (concatenada) ===== ")
for i, inf in enumerate(todos_influencers):
    print(f"{i+1}. {inf[0]:<18} | {inf[1]:<12}  | {inf[3]:<6} | {inf[2]:,} seg")
print(f"\nTotal: {len(todos_influencers)} influencers")
print("-" * 50)


#P2- Insert: añadir en posición específica de la lista original --
influencers.insert(0, ["Estrella Nova", "Instagram", 999000, 9.9, "estrella@ejemplo.com"])
print(f"\nInsertado en posición 1 de la lista inicial: {influencers[0][0]}")

print("\n ===== Lista Final (3-con backup) ===== ")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12} | {influencer[2]:,} seg")
print(f"\nTotal influencers: {len(influencers)}")


#P3- Copia de seguridad antes de eliminar --
influencers_backup = influencers.copy()
print(f"📋Backup conserva: {len(influencers_backup)} influencers")
print("-" * 50)

influencers.pop(0) #eliminamos a Estrella de la original

print("\n ===== Lista Final (4-Estrella eliminada) ===== ")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12} | {influencer[2]:,} seg")
print(f"\nTotal influencers: {len(influencers)}")

print(f"📋Original tiene: {len(influencers)} influencers")
print("-" * 50)

#P4 - Verificar que el backup está intacto 
print("\n ===== Lista Final (5-Conteo tras eliminación) ===== ")
print(f"\n 1.Primer influencer en backup: {influencers_backup[0][0]}")
print(f" 2.Primer influencer original: {influencers[0][0]}")
print("-" * 50)

#=====================================================
# LECCIÓN 4: Ordenar y buscar en listas
#=====================================================

# P1- Métodos de cadenas aplicados al CRM 
influencer = influencers[0]     # primer influencer de la lista
nombre = influencer[0]          # Laura Pires
plataforma = influencer[1]      # Youtube
email = influencer[4]           # laura@ejemplo.com

print(f"\n === Lección 4: Métodos de cadenas aplicados al CRM ===\n")

#len() - longitud de nombre
print(f"1. El nombre del influencer '{nombre}' tiene {len(nombre)} caracteres.")

#upper() y lower() - mayusculas y minusculas (normalización de datos)
print(f"2. Nombre en minúsculas: {nombre.lower()}")
print(f"3. Plataforma en mayúsculas: {plataforma.upper()}")

#find() - buscar subcadena y devuelve posicion
posicion = nombre.find("Pires")
print(f"4. El apellido empieza en la posición: {posicion}")

#replace() - corregir o actualizar datos
email_actualizado = email.replace("ejemplo.com", "kizuna.com")
print(f"5. Email actualizado: {email_actualizado}")

#split() - separar nombre y apellidos (dividir una cadena en subcadenas)
nombre_separado = nombre.split(" ")
print(f"6. Nombre y apellidos dividido: {nombre_separado}")

#join() - contruir etiqueta para el CRM
etiqueta = " | ".join([nombre, plataforma, str(influencer[2]), email_actualizado])
print(f"7. Etiqueta para el CRM: {etiqueta}")


#membresia - verificar si el email pertenece al dominio de la empresa
dominio = "kizuna.com"
print(f"8. ¿El email {email_actualizado} pertenece al dominio de la empresa?\n"
      f"   {'Sí' if dominio in email_actualizado else 'No'}")

#otra forma de verificar el dominio del email de forma mas segura:
if email_actualizado.endswith("@kizuna.com"):
    print(f"9. El email {email_actualizado} pertenece al dominio de la empresa.")
    
print("-" * 50)
