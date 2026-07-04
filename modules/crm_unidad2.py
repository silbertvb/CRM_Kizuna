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

# ============================================
# LECCIÓN 5: Tuplas 
# ============================================                          
print(f"\n === Lección 5: Tuplas ===\n")

#P1 - Definición de una Tupla aplicada al CRM (datos que no se cambiaran)
PLATAFORMAS_VALIDAS = ("Instagram", "Facebook", "Youtube", "Tiktok")

print(f"1. Plataformas válidas para el CRM: {(' | '.join(PLATAFORMAS_VALIDAS))}")
print(f"2. Total de plataformas existentes: {len(PLATAFORMAS_VALIDAS)}")

#P2 - Verificar si una plataforma es válida
plataforma_buscador = "Telegram"           # pongo "Telegram"para provocar que se imprima else 

if plataforma_buscador.lower() in [p.lower() for p in PLATAFORMAS_VALIDAS]:  
    print(f"3. La plataforma '{plataforma_buscador}' se encuentra en el CRM.")
else:
    print(f"3. La plataforma '{plataforma_buscador}' NO está registrada en el CRM.")
    
    
#P3 - Slicing: para obtener un rango o subtablas de plataformas existentes (por ejemplo, las 2 primeras)
print(f"4. Las 2 primeras plataformas registradas en el CRM son: {PLATAFORMAS_VALIDAS[:2]}")
print(f"5. La última plataforma registrada en el CRM es: {PLATAFORMAS_VALIDAS[-1]}")

#P4 - Índice y conteo 
plataforma_buscada = "Youtube"

if plataforma_buscada in PLATAFORMAS_VALIDAS:
    posicion = PLATAFORMAS_VALIDAS.index(plataforma_buscada)
    # posicion es el índice real de Python (empieza en 0); se suma 1 solo para
    # mostrarle al usuario por pantalla una numeración natural (empezando en 1)
    print(f"6. La plataforma '{plataforma_buscada}' se encuentra en la posición: {posicion + 1}")
else:
    print(f"6. La plataforma '{plataforma_buscada}' no está registrada en el CRM.")
    
    
#P5 - DESEMPAQUETADO de tupla con datos de un influencer (datos que no deben cambiarse)
nuevo_influencer = ("Jorge Rojas", "Youtube", 450000, 6.5, "jorge@kizuna.com")
print(f"\n7. Se agregó un nuevo influencer a la lista de influencers: {nuevo_influencer[0]}")

nombre_inf, plataforma_inf, seguidores_inf, engagement_inf, email_inf = nuevo_influencer
print(f"\n- Unpacking de la tupla del influencer: {nombre_inf}")
print(f"  - Plataforma: {plataforma_inf:<12}")
print(f"  - Seguidores: {seguidores_inf:<12}")
print(f"  - Engagement: {engagement_inf:<12}")
print(f"  - Email: {email_inf:<12}")

#P6 - Conversión de tupla a lista para poder modificar datos y reconvertir a tupla para proteger los datos
print(f"\n8. Modificando datos de la tupla del influencer: {nombre_inf}")
temporary_list = list(nuevo_influencer)   # Convertir tupla a lista
temporary_list[2] = 500000                # Modificar el número de seguidores 450 -> 500000
nuevo_influencer = tuple(temporary_list)  # Convertir de nuevo a tupla
print(f"  - Seguidores actualizado: {nuevo_influencer[2]:<12}") 

#P7 - Concatenar el nuevo influencer a la lista de influencers (evitando duplicados por email)
ya_existe = any(influencer[4] == nuevo_influencer[4] for influencer in influencers)
if not ya_existe:
    influencers.append(list(nuevo_influencer))  # Convertir tupla a lista para añadir a la lista de influencers
    print(f"\n9. Influencer '{nuevo_influencer[0]}' añadido a la lista de influencers.")

print("\n ===== Lista Final (6-Influencer añadido) ===== ")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12}  | {influencer[3]:<6} | {influencer[2]:,} seg")
    
print('-' * 50)