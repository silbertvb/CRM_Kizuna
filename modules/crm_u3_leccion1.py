from datos_crm import influencers, PLATAFORMAS_VALIDAS

"""
CRM Kizuna — Unidad 3, Lección 1: Operaciones de tipos de datos

Ejercicios:
  1. Casting de tipos (int, float)
  2. Integración CSV sin duplicados (any, append)
  3. Indexación de cadenas ([0], [-1], split, upper)
  4. Slicing ([:3], [::-1], split("@"))
  5. List comprehension para filtrar
  6. Dict comprehension + .items()
  7. Elegir estructura correcta (tupla, dict, set)
  8. Informe final (set comprehension, sorted + lambda, sum)
"""
print("=" * 50)
print(" CRM Kizuna - U3: Operaciones de tipo de datos")
print("=" * 50)

# Siguiente paso
# CONTEXTO: Llega una importación CSV con nuevos influencers.
# PROBLEMA: todos los datos vienen como STRINGS porque así los lee Python cuando importa un CSV.
# Hay que limpiarlos y convertirlos antes de integrarlos al CRM.

importacion_csv = [
    ("Sofía Martinez", "Instagram", "92000", "5.1", "1350", "sofia@kizuna.com"),
    ("Diego Ramos", "Tiktok", "145000", "6.1", "2200", "diego_r@kizuna.com"),
    ("Carla Nunes", "Youtube", "68000", "4.3", "900", "carla@kizuna.com")
]

# --- Ejercicio 1 — Casting de tipos ---
# Los CSV importan todo como string. Convertimos seguidores a int, engagement a float, coste a int.
# Practica: int(), float(), type()
print("\n---- EJERCICIO 1 - Casting de tipos ----")

#crea un bucle con un nombre (inf) para recorrer y convertir los datos necesarios
for inf in importacion_csv:
    seguidores = int(inf[2])
    engagement = float(inf[3])
    coste = int(inf[4])
    
    print(f"1. Los datos de '{inf[0]}' son: {seguidores} {type(seguidores)} | {engagement} {type(engagement)} | {coste} {type(coste)}")


# --- Ejercicio 2 — Integrar CSV al CRM ---
# Añade los nuevos influencers si no existen (comparando por email). Descarta el coste (campo 4 del CSV).
# Practica: any(), append, casting dentro de la integración
print("\n---- EJERCICIO 2 — Integrar CSV al CRM ----")
for inf in importacion_csv:
    ya_existe = any(influencer[4] == inf[5] for influencer in influencers)
    
    if not ya_existe:
        nuevo = [inf[0], inf[1], int(inf[2]), float(inf[3]), inf[5]] #se descarta el coste (registro[4]) a propósito, porque el CRM no lo guarda.
        influencers.append(nuevo)
        
#enumeramos la tabla actualizada con los nuevos influencers incluidos a la lista
for i, inf in enumerate(influencers):
    print(f"{i+1}. {inf[0]:<18} | {inf[1]:<12} | {inf[2]:<8} | {inf[3]:<4} | {inf[4]}")
    
    
# --- Ejercicio 3 — Indexación de cadenas ---
# Genera código único: primera letra nombre + última apellido + primera plataforma
# Practica: [0], [-1], .split(), .upper()
print("\n---- EJERCICIO 3 — Indexación de cadenas ----")

for i, inf in enumerate(influencers):
    partes = inf[0].split()     #separa "nombre apellido" en ['nombre', 'apellido']
    nombre = partes[0]          #[0] corresponde a la primera parte (nombre)
    apellido = partes[1]        #[1] corresponde a la segunda parte (apellido)
    plataforma = inf[1]         #plataforma del influencer
    
    codigo = nombre[0] + apellido[-1] + "-" + plataforma[0]     #primera nombre + última apellido + primera plataforma
    print(f"{i+1}. {inf[0]:<14} -> Código: {codigo.upper()}")   #imprime alineado a la izquierda (:<) con código en mayúsc.


# --- Ejercicio 4 — Slicing de cadenas ---
# Extrae tag (3 primeras letras), nombre invertido y dominio del email
# Practica: [:3], [::-1], .split("@"), .lower()
print("\n---- EJERCICIO 4 — Slicing de cadenas ----")

for i, inf in enumerate(influencers):
    partes = inf[4].split("@")  #divido el correo en 2 partes (antes y despues del @)
    tag = inf[0].lower()        #con lower obtengo el 'Tag' de cada inf en minúscula
    invertido = inf[0]
    email = partes[0]           #no se usa y se podria quitar, lo dejo para que se distingan las partes del correo electronico
    dominio = partes[1]
    
    print(f"{i+1}. {inf[0]:<14} | Tag:{tag[:3]:<4} | Invertido: {invertido[::-1]:<14} | Dominio: {dominio}")
    
    
# --- Ejercicio 5 — List comprehension para filtrar ---
# Filtra influencers por seguidores, plataforma y engagement usando list comprehension
# Practica: [x for x in lista if condición]
print("\n---- EJERCICIO 5 — List Comprehension: filtrar influencers ----")

#para obtener los influencer con más de 100.000 seguidores
print(f"5.1 Perfiles con más de 100.000 seguidores: ")
top_influencers = [inf for inf in influencers if inf[2] > 100000]

for i, inf in enumerate(top_influencers):
    print(f"  {i+1}. {inf[0]:<16} | Seguidores: {inf[2]} ")

#para obtener los influencers con perfiles en instagram
print(f"\n5.2 Perfiles de Instagram: ")    
instagram_team = [inf for inf in influencers if inf[1] == "Instagram"]

for i, inf in enumerate(instagram_team):
    print(f"  {i+1}. {inf[0]:<16} | Team: {inf[1]} ")

#para obtener los inf con Engagement superiores a 5    
print(f"\n5.3 Perfiles con Engagement > 5: ")    
alta_engagement = [inf for inf in influencers if inf[3] > 5]

for i, inf in enumerate(alta_engagement):
    print(f"  {i+1}. {inf[0]:<16} | Eng: {inf[3]} %")
    
    
# --- Ejercicio 6 — Dict comprehension ---
# Crea diccionarios para búsqueda rápida: nombre→seguidores y nombre→plataforma
# Practica: {clave: valor for x in lista}, .items(), desempaquetado
print("\n---- EJERCICIO 6 — Dict. Comprensión ----")

#para obtener un Dict por nombre y cantidad de seguidores
print(f"6.1 Filtrar por por nombre y cantidad de seguidores: ")
seguidores_dict = {inf[0]:inf[2] for inf in influencers}

for i, (nombre, seguidores) in enumerate(seguidores_dict.items()): #en este Desempaqueto (nombre, seguidores) es más legible
    print(f"  {i+1}. {nombre:<14} -> {seguidores:,} seg.")
    
#para obtener un Dict por nombre y red social
print(f"\n6.2 Filtrar por por nombre y red social: ")
perfiles_dict = {inf[0]: inf[1] for inf in influencers}

for i, inf in enumerate(perfiles_dict.items()):  #en este utilizamos indice en vez de desempaquetar (se obtiene el mismo resultado pero menos legible) 
    print(f"  {i+1}. {inf[0]:<14} -> {inf[1]}")  #aunque en el CRM la plataforma corresponde al indice [2] en un dict solo exist [0] y [1]
    
    
    
# --- Ejercicio 7 — Elegir la estructura de datos correcta ---
# Para cada caso se elige tupla, dict o set según la necesidad: inmutabilidad, búsqueda o unicidad
# Practica: tupla para constantes, dict para clave:valor, set para eliminar duplicados
print("\n---- EJERCICIO 7 — Elegir la estructura de datos correcta ----")

#7.1Plataformas donde opera Kizuna. No se repiten, no importa el orden ¿Lista, tupla o set?
#nombramos la variable que se IMPORTA al inicio directamente dentro del print
print(f"\n7.1 Las plataformas donde opera Kizuna: ", " | ".join(PLATAFORMAS_VALIDAS))

#7.2 y 7.3 Límites del CRM (valores fijos que no deben cambiar nunca) ¿Tupla, lista o dict?
#la tupla en este caso nos permite asegurarnos que estos datos no se cambiaran 
MAX_INFLUENCERS = 500
MAX_CAMPANIAS = 50

limites_crm = (MAX_INFLUENCERS, MAX_CAMPANIAS)
print(f"\n7.2 El CRM tiene como limite trabajar con: {MAX_INFLUENCERS} influencers.")
print(f"\n7.3 El CRM tiene como límite trabajar con: {MAX_CAMPANIAS} campañas.")

#7.4 Buscar el email de un influencer por nombre rápidamente. ¿Lista, dict o set?
buscar_email = {inf[0]: inf[4] for inf in influencers}  #Se necesita una estructura clave:valor
print(f"\n7.4 Email de Laura Pires: {buscar_email['Laura Pires']}")

#7.5 Países donde opera Kizuna sin repetidos: España, México, Brasil
#repetido Brasil (a propósito). ¿Lista o set?
paises = ["España", "Brasil", "México", "Brasil"]
paises_unicos = set(paises)   #convierto con 'set' para eliminar duplicados
print(f"\n7.5 Los países donde opera Kizuna son:", ", ".join(paises_unicos))



# --- Ejercicio 8 — Informe de integración completo (RETO) ---
# Combina todo lo anterior: set comprehension, sum(), sorted() con lambda, list comprehension
# Genera: resumen, tabla con códigos, top 3 por seguidores, alertas de bajo engagement

#se crea una variable nueva para almacenar las redes activas
plataformas_activas = {inf[1] for inf in influencers}  #set comprehension

#para obtener la media de engagement 
media = sum(inf[3] for inf in influencers) / len(influencers)

print(f"\n=========  INFORME FINAL LECCION 1. CRM KIZUNA =========")
print(f"\nRESUMEN:")
print(f"  Total influencers: {len(influencers)}")
print(f"  Plataformas activas: {', '.join(plataformas_activas)}") 
print(f"  Media engagement: {media:.2f} %") 
print(f"\nTABLA COMPLETA:")
for i, inf in enumerate(influencers):
    partes = inf[0].split()
    nombre = partes[0]
    apellido = partes[1]
    plataforma = inf[1]
    
    codigo = nombre[0] + apellido[-1] + "-" + plataforma[0]
    tag = inf[0].lower()[:3]
    
    print(f"  {i+1}. {codigo.upper()} | {tag:<4} | {inf[0]:<16} | {inf[1]:<10} | {inf[2]:>10,} seg | {inf[3]}%") #seg. a la derecha (:>10)
    
print(f"\nTOP 3 POR SEGUIDORES:")
top3_influencers = sorted(influencers, key=lambda inf: inf[2], reverse=True)[:3]
for i, inf in enumerate(top3_influencers):
    print(f"  {i+1}. {inf[0]:<14} | {inf[2]:>10,} seg")
    
    
print(f"\n⚠️  NECESITAN ATENCIÓN (engagement < 5.0):")
bajo_engagement = [inf for inf in influencers if inf[3] < 5]

for i, inf in enumerate(bajo_engagement):
    print(f"  {i+1}. {inf[0]:<14} | Eng: {inf[3]} %")
