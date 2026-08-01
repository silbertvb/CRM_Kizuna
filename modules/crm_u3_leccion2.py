from datos_crm import influencers, PLATAFORMAS_VALIDAS

"""CRM Kizuna - Unidad 3, Lección 2: Operadores en expresiones

Ejercicios:
  1. Coste por seguidor y CPM — (/, *, round)
  2. Reparto de presupuesto — (//, %)
  3. Proyección de crecimiento — (**)
  4. Clasificación por tiers — (>, <, >=, !=)
  5. Simulador de presupuesto — (+=, -=, *=)
  6. Informe de rentabilidad (RETO) — (todos los operadores)
"""
print("=" * 50)
print(" CRM Kizuna - U3 L2: Operadores en expresiones")
print("=" * 50)

# ----- Ejercicio 1 — Coste por seguidor y CPM -----
# - Qué hace: Cada influencer cobra un precio por campaña. Calcula cuánto te cuesta alcanzar a cada seguidor, 
# - y cuánto cuesta alcanzar a 1.000 personas (CPM, la métrica estándar del marketing).
# - Practica: `/` (división), `*` (multiplicación), `round()`
print("\n---- EJERCICIO 1. El coste por seguidor y CPM es:\n")

COSTES_CAMPAÑA = [300, 1200, 5000, 2000]

for i, inf in enumerate(influencers):
    coste = COSTES_CAMPAÑA[i]                       # [i]hace que cada vuelta coja el coste que corresponde a ese influencer.
    seguidores = inf[2]                             # para obtener nº de seguidores
    precio_seguidor = coste/seguidores
    cpm = precio_seguidor * 1000
    nombre = inf[0]
    
    print(f"  {i+1}. {nombre:<14} | Coste: {precio_seguidor:<6.4f}$ x seg. | Nº seguidor: {seguidores:>10,} | CPM : {cpm:.2f} %")
    
     
# ----- Ejercicio 2 — Reparto de presupuesto -----
# - Qué hace: Tienes 10.000€ de presupuesto trimestral. Se Reparte equitativamente entre todos los influencers.
# - Calcula cuánto le toca a cada uno (sin decimales) y cuánto sobra. Verifica que lo repartido + el sobrante suma el total.
# - Practica: `//` (división entera), `%` (módulo), `*` y `+`
print("\n---- EJERCICIO 2. Reparto de presupuesto:\n")

presupuesto = 10000                 

partes = len(influencers)           #obtengo el nº de influencers dentro de la lista
pago = presupuesto // partes        #obtengo el importe correspondiente a cada inf
sobrante = presupuesto % partes
verificacion = (pago * partes) + sobrante == presupuesto

print(
    f"1. Presupuesto total: {presupuesto:,.2f}€\n"
    f"2. Pago por influencer: {pago:,.2f}€\n"
    f"3. Sobrante: {sobrante:.2f}€\n"
    f"4. Verificación: {presupuesto:.2f}€ {'✅' if verificacion else '❌'}"
)

# ----- Ejercicio 3 — Proyección de crecimiento -----
# - Qué hace: Proyecta los seguidores de cada influencer a 1, 2 y 3 años
# - suponiendo un crecimiento anual del 15%. La fórmula es: `seguidores * tasa ^ años` (crecimiento compuesto).
# - Practica: `**` (potencia), `*`, `int()` para redondear seguidores enteros
print("\n---- Ejercicio 3 — Proyección de crecimiento:\n")

tasa_anio = 1.15      

print(f"   Influencer   |     Actual |      Año 1 |      Año 2 |      Año 3")
for i, inf in enumerate(influencers):
    nombre = inf[0]
    seguidores = inf[2]
    anio1 = seguidores * tasa_anio      #se puede elevar a la potencia de 1 pero no es necesario, ya que cualquier número elevado a 1 es el mismo número.
    anio2 = seguidores * tasa_anio ** 2 #tasa_anio ** 2 (tasa_anio * tasa_anio), es decir, el crecimiento compuesto para el segundo año.
    anio3 = seguidores * tasa_anio ** 3 
    
    print(f"{i+1}. {nombre:<12} | {seguidores:>10,} | {int(anio1):>10,} | {int(anio2):>10,} | {int(anio3):>10,}")
    

# ---- Ejercicio 4 — Clasificación por tiers ----
# - Qué hace: Clasifica cada influencer según el estándar del sector:
#   - Mega:  > de 1.000.000 seguidores
#   - Macro: > de 100.000 seguidores
#   - Micro: <= 100.000 o menos

print("\n---- Ejercicio  4 — Clasificación por tiers:\n")

for i, inf in enumerate(influencers):
    nombre = inf[0]
    seguidores = inf[2]
    if seguidores > 1000000:
        tier = "⭐ Mega"
    elif seguidores > 100000:
        tier = "🔵 Macro"
    else:
        tier = "🟢 Micro"
    
    eng = inf[3]
    if eng >= 5:
        estado_eng = "✅ OK"
    else:
        estado_eng = "⚠️  Bajo"
        
    if inf[1] in PLATAFORMAS_VALIDAS:
        estado_plat = "Válido: True"
    else:
        estado_plat = "Válido: False"

    print(
        f"{i+1}. {nombre:<12} | {tier:<8} | {seguidores:>10} seg. | "
        f"Eng: {eng} % |  {estado_eng:<6} | {estado_plat}"
        )
    
    
# ---- Ejercicio 5 — Simulador de presupuesto ----

# - Qué hace -> Simula 3 campañas gastando el presupuesto: Arranco con 15.000€.
#   1. Manuel Vega: 5.000€
#   2. Pedro Pascal: 1.200€
#   3. (Bonificación: el cliente añade +10% al presupuesto restante)
#   4. Laura Pires: 300€

# - Lleva la cuenta del presupuesto restante, el total gastado y las campañas realizadas.
# - Practica: `-=` (restar y asignar), `+=` (sumar y asignar), `*=` (multiplicar y asignar)
    
print("\n---- EJERCICIO 5 — Simulador de presupuesto:\n")

presupuesto = 15000
total_gastado = 0
campanas = 0

print(f"Presupuesto inicial: {presupuesto:,.2f}€\n")

# Campaña 1
coste = 5000
presupuesto -= coste
total_gastado += coste
campanas += 1
print(f"1. Manuel Vega: {-coste:>8,}€ | Presupuesto restante: {presupuesto:>10,.2f}€ |"
      f" Total gastado: {total_gastado:,.2f}€ | Campañas realizadas: {campanas}")

# Campaña 2
coste = 1200
presupuesto -= coste
total_gastado += coste
campanas += 1
print(f"2. Pedro Pascal: {-coste:>7,}€ | Presupuesto restante: {presupuesto:>10,.2f}€ |"
      f" Total gastado: {total_gastado:,.2f}€ | Campañas realizadas: {campanas}")

#(bonificación adicional del 10% que se calcula sobre el presupuesto restante en este momento)
presupuesto *= 1.10
print(f"  💰 Bonificación del 10% | presupuesto restante: {presupuesto:>10,.2f}€")

# Campaña 3
coste = 300
presupuesto -= coste
total_gastado += coste
campanas += 1
print(f"3. Laura Pires: {-coste:>8,}€ | Presupuesto restante: {presupuesto:>10,.2f}€ |"
      f" Total gastado: {total_gastado:,.2f}€ | Campañas realizadas: {campanas}")

print(
    f"\nResumen final:\n" f" - Campañas realizadas: {campanas}\n" 
    f" - Presupuesto restante: {presupuesto:,.2f}€\n" 
    f" - Total gastado: {total_gastado:,.2f}€")

# ---- Ejercicio 6 — Informe de rentabilidad (RETO) ----
# - Qué hace: Calcula la rentabilidad de cada influencer según el coste de la campaña
# - practica: todos los operadores vistos hasta ahora. (/, *, round, //, %, **, >, <, >=, !=, +=, -=, *=)

#datos de campañas de marketing de cada influencer (coste, impresiones y ventas)
campanas = [
    {"influencer": "Manuel Vega", "coste": 5000, "impresiones": 920000, "ventas": 120},
    {"influencer": "Pedro Pascal", "coste": 1200, "impresiones": 185000, "ventas": 35},
    {"influencer": "Laura Pires", "coste": 300, "impresiones": 95000, "ventas": 8},
    {"influencer": "Jorge Rojas", "coste": 2000, "impresiones": 310000, "ventas": 45},
]

TICKET_MEDIO = 49.90  # € valor medio de cada venta
ventas = 0
presupuesto_total = 0
ingresos_total = 0

print("\n---- EJERCICIO 6 — Informe de rentabilidad:\n")

for i, camp in enumerate(campanas):
    nombre = camp["influencer"]
    coste = camp["coste"]
    impresiones = camp["impresiones"]
    ventas = camp["ventas"]
    ingresos = ventas * TICKET_MEDIO
    presupuesto_total += coste          #suma el coste de cada campaña al presupuesto total
    ingresos_total += ingresos          #se acumula el total de ingresos de todas las campañas

    # Cálculo de métricas
    cpm = (coste / impresiones * 1000) if impresiones > 0 else 0
    cpa = (coste // ventas) if ventas > 0 else float('inf')  # Evitar división por cero
    ingresos = ventas * TICKET_MEDIO
    roi = ((ingresos - coste) / coste) * 100 if coste > 0 else float('inf')
    beneficio = ingresos - coste if coste > 0 else float('inf')

    print(
        f"{i+1}.{nombre:<12}| Cost:{-coste:>10,.2f}€ | "
        f"Impres:{impresiones:>8} | Ventas:{ventas:>3} | "
        f"CPM:{cpm:>6,.2f}€ | CPA:{cpa:>6,.2f}€ | "
        f"Ingr:{ingresos:>10,.2f}€ | Benef: {beneficio:>6,.2f}€ | ROI:{roi:>6,.2f}% | "
        f"{'✅ Rentable' if roi > 0 else '❌ Pérdida'}"
    )
    
roi_global = ((ingresos_total - presupuesto_total) / presupuesto_total) * 100 if presupuesto_total > 0 else float('inf')

    
print(
     f"\nRESUMEN GLOBAL:\n - Coste total: {presupuesto_total:,.2f}€\n"
    F" - Ingresos totales: {ingresos_total:,.2f}€\n"
    f" - ROI total: {roi_global:,.2f}% | {'✅ Rentable' if roi_global > 0 else '❌ Pérdida'}"
)