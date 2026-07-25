"""
CRM Kizuna — Unidad 2, Lecciones 2-7: Listas, tuplas, sets y literales

Lecciones:
  2. Creación de lista — (listas anidadas, append, pop, enumerate)
  3. Técnicas de manipulación — (concatenación, insert, copy, pop)
  4. Ordenar y buscar en listas — (métodos de cadenas: len, upper, lower, find, replace, split, join, in)
  5. Tuplas — (inmutabilidad, slicing, index, desempaquetado, conversión tupla-lista)
  6. Sets aplicados al CRM — (duplicados, add, update, discard, remove, operaciones de conjuntos)
  7. Literales aplicados al CRM — (hex, bin, multilínea, raw string, bool, None, float científico, complejo)
"""

# --- Lección 2 — Creación de lista ---
# Qué hace: crea una lista anidada de influencers, la muestra numerada, añade y elimina elementos
# Practica: listas anidadas, append(), pop(), enumerate(), f-strings

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
print(f"🗑️-Eliminado: {eliminado[0]}")

#Paso 5 - Muestra la lista final:
print("\n --------- Lista Final (2)---------")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12} | {influencer[2]:,} seg")
print(f"\nTotal influencers: {len(influencers)}")


# --- Ejercicio/Lección 3 — Técnicas de manipulación ---
# Qué hace: concatena listas, inserta en una posición concreta y crea una copia de seguridad antes de eliminar
# Practica: concatenación de listas (+), insert(), copy(), pop()


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
print("-" * 50)

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

# --- Lección 4 — Ordenar y buscar en listas ---
# Qué hace: aplica métodos de cadenas sobre los datos de un influencer para normalizar y consultar información
# Practica: len(), upper(), lower(), find(), replace(), split(), join(), operador in


# P1- Métodos de cadenas aplicados al CRM 
#Declaramos variables con los datos del primer influencer de la lista y aplicamos métodos de cadenas
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

# --- Lección 5 — Tuplas ---
# Qué hace: define las plataformas válidas como tupla, las valida y recorre, y desempaqueta los datos de un influencer
# Practica: tuplas inmutables, slicing, index(), desempaquetado, conversión tupla↔lista
                         
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
# comparamos el email del nuevo influencer con los emails de los influencers existentes para evitar duplicados
ya_existe = any(influencer[4] == nuevo_influencer[4] for influencer in influencers)
if not ya_existe:
    influencers.append(list(nuevo_influencer))  # Convertir tupla a lista para añadir a la lista de influencers
    print(f"\n9. Influencer '{nuevo_influencer[0]}' añadido a la lista de influencers.")

print("\n ===== Lista Final (6-Influencer añadido) ===== ")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12}  | {influencer[3]:<6} | {influencer[2]:,} seg")
    
print('-' * 50)

# --- Lección 6 — Sets aplicados al CRM ---
# Qué hace: elimina duplicados de plataformas y calcula intersección, diferencia y unión entre campañas
# Practica: set(), add(), update(), discard(), remove(), operadores &, -, |, pop()


#P1. Plataformas únicas de los influencers (eliminando duplicados)
plataformas_activas = ["Instagram", "Instagram", "Youtube", "Youtube"]
plataformas_unicas = set(plataformas_activas)  # Convertimos la lista a un set para eliminar duplicados

print(f"\n === Lección 6: Sets aplicados al CRM ===\n")
# TODO: los sets no garantizan orden -> el resultado de join(plataformas_unicas)
# puede salir en distinto orden en cada ejecución. Si algún día se necesita un
# orden fijo (ej. alfabético), usar sorted(plataformas_unicas) en vez de iterar el set directo.
print(
    f"1. Actualmente {len(plataformas_activas)} influencers operan en solo "
    f"{len(plataformas_unicas)} plataformas: {' y '.join(plataformas_unicas)}"
)

#P2. Añadir, actualizar, discartar y remover elementos de un set
#1. Anadir un nuevo elemento al set de plataformas únicas
nueva_plataforma = "Twitch"
plataformas_unicas.add(nueva_plataforma)  # Añadir una nueva plataforma
print(f"2. Se añadió '{nueva_plataforma}' a la lista. Quedando actualizada en: {' | '.join(plataformas_unicas)}")

#2. Actualizar el set con varias plataformas nuevas (desordenadas y no se repiten)
plataformas_nuevas = {"Linkedin", "Tiktok"}
plataformas_unicas.update(plataformas_nuevas)
print(
    f"3. Se añadieron 2 nuevas plataformas: {' y '.join(plataformas_nuevas)}.\n"
    f" - Quedando actualizada en: {' | '.join(plataformas_unicas)}")

#3. Discard: eliminar un elemento del set (si existe, si no, no hace nada)
plataforma_a_eliminar = "Facebook" #eliminamos un elemento que NO existe usando discard (evitando error)

if plataforma_a_eliminar in plataformas_unicas:
    plataformas_unicas.discard(plataforma_a_eliminar)
    print(f"4. Se eliminó '{plataforma_a_eliminar}' del set.")
else:
    plataformas_unicas.discard(plataforma_a_eliminar)  # no hace nada, y no da error
    print(f"4. '{plataforma_a_eliminar}' no estaba en el set — discard() no dio error.")

#4. Remove: eliminar un elemento del set (si no existe, da error)
plataforma_a_eliminar = "Twitch" #eliminamos un elemento que SI existe
plataformas_unicas.remove(plataforma_a_eliminar)
print(
    f"5. Se eliminó '{plataforma_a_eliminar}' de la lista.\n"
    f" - Quedando actualizada en: {' | '.join(plataformas_unicas)}")


#5. Operaciones entre camcapanas (objetivo: identificar influencers que participan en varias campañas)
campania_verano = {"Laura Pires", "Pedro Pascal", "Manuel Vega"}
campania_navidad = {"Pedro Pascal", "Manuel Vega", "Jorge Rojas"}

repitores_campanias = campania_verano & campania_navidad  #otra opcion seria: campania_verano.intersection(campania_navidad)
print(
    f"\n6. Los influencers que participaron en ambas campañas son: \n"
    # el espacio va dentro de cada elemento (no en el separador) para que
    # el "1." quede  con la misma sangría que el resto de las líneas
    # 'u' es el usuario (nombre del influencer), 'i' es el índice de la enumeración
    f"{'\n'.join([f' {i+1}.{u}' for i, u in enumerate(repitores_campanias)]) if repitores_campanias else ' Ninguno'}")

no_repitieron = campania_verano - campania_navidad  #otra opcion seria: campania_verano.difference(campania_navidad)
print(
    f"\n7. Los influencers que solo participaron en la campaña de verano son: \n"
    f"{'\n'.join([f' {i+1}.{u}' for i, u in enumerate(no_repitieron)]) if no_repitieron else ' Ninguno'}")

todos = campania_verano | campania_navidad  #otra opcion seria: campania_verano.union(campania_navidad)
print(
    f"\n8. Los influencers que participaron en al menos una de las campañas son: \n"
    f"{'\n'.join([f' {i+1}.{u}' for i, u in enumerate(todos)]) if todos else ' Ninguno'}")



#6. Membership: verificar si un elemento pertenece al set
usuario_buscado = "Laura Pires"
if usuario_buscado in campania_navidad:  #la variable que se indica despues de 'in' debe ser donde se busca el elemento (en este caso, el set de la campaña de navidad)
    print(f"\n9. '{usuario_buscado}' participó en la campaña de navidad.")
else:
    print(f"\n9. '{usuario_buscado}' no participó en la campaña de navidad.")

#6. (bonus) - funcionalidad de pop() y creación de un set con tuplas dentro
mercados = {("Instagram", "ES"), ("Youtube", "MX"), ("Tiktok", "BR")}

# mercados es un set (sin orden ni índices), por eso no se puede usar mercados[0]/mercados[1];
# para numerar cada tupla hay que iterar con enumerate() dentro de una list comprehension
print(
    f"\n10. Actualmente hay {len(mercados)} mercados activos:\n "
    + "\n ".join([f"{i+1}.{t[0]} ({t[1]})" for i, t in enumerate(mercados)])
)

mercado_eliminado = mercados.pop()  # pop() elimina un elemento aleatorio del set
print(f"\n11. Se eliminó el mercado: {mercado_eliminado[0]} ({mercado_eliminado[1]})")

print(
    f"\n12. La lista actualizada contiene {len(mercados)} mercados activos:\n "
    + "\n ".join([f"{i+1}.{t[0]} ({t[1]})" for i, t in enumerate(mercados)])
)

print("-" * 50)  

# --- Lección 7 — Literales aplicados al CRM ---
# Qué hace: muestra distintos tipos de literales de Python aplicados a datos del CRM
# Practica: hex, bin, strings multilínea, raw strings, booleanos/truthy-falsy, None, float científico, números complejos

print(f"\n === Lección 7: Literales aplicados al CRM ===\n")

#P1 - Literales numéricos: hexadecimal y binario
color_corporativo = 0xE84393     # color rosa Kizuna en hexadecimal
permisos_admin = 0b1111          # 4 permisos: leer|escribir|editar|borrar
permisos_becario = 0b0001        # solo 1 permiso: lectura

print(f"1. Color corporativo (hex 0xE84393) como entero: {color_corporativo}")
print(f"   Y de vuelta a hex para el diseñador: {hex(color_corporativo)}")
print(f"2. Permisos admin (0b1111) = {permisos_admin} | becario (0b0001) = {permisos_becario}")


# P2 - Literal multilínea: menú de bienvenida del CRM
# Guardamos el menú en una variable utilizando triple comilla para poder reutilizarlo en otras partes del programa
menu_crm = """
╔══════════════════════════════╗
║      CRM KIZUNA v1.0         ║
║  1. Ver influencers          ║
║  2. Añadir influencer        ║
║  3. Campañas activas         ║
║  4. Perfil                   ║
║  5. Salir                    ║
╚══════════════════════════════╝"""
print(f"3. El menú del CRM es:\n{menu_crm}")


# P3 - Raw string: ruta de exportación de informes
ruta_normal = "C:\nuevos_informes\tabla_influencers"  #sin r se rompe la ruta por el \n y \t (salto de línea y tabulación)
ruta_raw = r"C:\nuevos_informes\tabla_influencers"    #con r se toma la ruta tal cual (forma correcta)

print(f"4. Ruta SIN raw string:{ruta_normal} -- (ruta rota)")
print(f"   Ruta CON raw string (correcta): {ruta_raw}")


# P4 - Literales booleanos y truthy/falsy (ejercicio de los clientes):
#      → recorrer solo los activos
#      → "CON ventas"/"SIN ventas" usando la lista como condición

clientes = [
    ["GameZone", True, [1200.50, 850.00]],    # nombre, activo, lista de ventas
    ["TechShop", False, [500.00]],            # inactivo con ventas
    ["ModaStyle", True, []],                  # activo pero sin ventas
]

print("\n5. Informe de clientes activos:")
for nombre, activo, ventas in clientes:      # unpacking, como en la Lección 5
    if activo:                               # True/False directo como condición
        estado_ventas = "CON ventas" if ventas else "SIN ventas"   # lista como condición
        print(f"   - {nombre}: {estado_ventas}")

# - Suma de booleanos: sum() de True/False para contar cuántos clientes activos hay
print(f"\n   Clientes activos: {sum(activo for _, activo, _ in clientes)}")


# P5 - None: fecha_ultima_campania = None con 'is None'
fecha_ultima_campania = None  # None simula que aún no se ha lanzado ninguna campaña este trimestre

if fecha_ultima_campania is None:
    print("\n6. ⚠️: Aún no se ha lanzado ninguna campaña este trimestre.")
else:
    print(f"\n6. Última campaña: {fecha_ultima_campania}")

#P6 - Float científico: presupuesto anual
presupuesto = 1.5e6  #e6 significa los ceros que siguen al 1.5 x 1.000.000 (1.500.000)
print(f"\n7. Presupuesto anual de campañas: {presupuesto:,.2f} €")


# P7 - Complejo: demo de 44.76j (y por qué no lo usarás en el CRM)
numero_complejo = 44.76j
print(f"\n8. Literal complejo: {numero_complejo} | tipo: {type(numero_complejo).__name__}")
print("   (Los complejos sirven para ingeniería/señales, ❌ no para un CRM).")
print("-" * 50)