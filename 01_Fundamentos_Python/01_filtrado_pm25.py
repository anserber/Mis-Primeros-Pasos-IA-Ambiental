"""
PROYECTO: Monitoreo de Calidad del Aire - PM2.5
ROL: AI Research Scientist (Future UNALM Engineer)
TEMA: Lógica de Programación y List Comprehensions
"""

# 1. Definición de la fuente de datos (Ejemplo: Estación Huancayo)
# Lecturas en microgramos por metro cúbico (µg/m3)
lecturas_huancayo = [12.5, 55.2, 48.0, 62.1, 10.5, 89.3, 44.7]

# 2. El Estándar Nacional (ECA) para 24 horas
ECA_LIMITE = 50.0

# 3. IMPLEMENTACIÓN OPTIMIZADA (List Comprehension)
# Esta es la forma "Senior" de filtrar datos en una sola línea.
# Se lee: "Guarda cada L si L es parte de LECTURAS y L es mayor al ECA"
excesos = [l for l in lecturas_huancayo if l > ECA_LIMITE]

# 4. Resultados para auditoría ambiental
print(f"--- REPORTE DE EXCESOS ---")
print(f"Total de mediciones analizadas: {len(lecturas_huancayo)}")
print(f"Lecturas que superan el ECA ({ECA_LIMITE} µg/m3): {excesos}")
print(f"Número de infracciones detectadas: {len(excesos)}")
