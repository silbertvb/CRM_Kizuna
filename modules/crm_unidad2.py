#Paso1- Definición de una Lista anidada de influencers 
"""Cada influencer es una lista con 5 datos dentro de la lista principal
Esto se llama lista anidada."""
influencers = [
    ["Laura Pires", "Instagram", 85000, 3.4, "laura@ejemplo.com"],
    ["Fernando Silva", "Facebook", 815000, 2.7, "fernando@ejemplo.com"],
    ["Pedro Pascal", "Instagram", 285000, 5.4, "pedro@ejemplo.com"]
]


#Paso2 - Muéstralos numerados
print("----------- CRM Kizuna - Influencers -----------")
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
print("\n --------- Lista Final ---------")
for i, influencer in enumerate(influencers):
    print(f"{i+1}. {influencer[0]:<18} | {influencer[1]:<12} | {influencer[2]:,} seg")
print(f"\nTotal influencers: {len(influencers)}")

