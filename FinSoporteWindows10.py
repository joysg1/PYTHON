import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Parámetros iniciales
start_date = datetime(2025, 8, 21)  # Fecha actual
end_of_support = datetime(2025, 10, 14)  # Fin de soporte de Windows 10
end_date = end_of_support + timedelta(days=365)  # Un año después del fin de soporte

# Crear rango de fechas mensuales
dates = pd.date_range(start=start_date, end=end_date, freq='M')

# Simulación de factores de riesgo
base_risk = 0.4  # Riesgo inicial (0 a 1)
popularity_factor = 1.3  # Windows 10 es muy común
industry_factor = 1.1  # Hotelería: atractivo medio para ransomware

# Función para calcular riesgo
def calculate_risk(date):
    # Si estamos antes del fin de soporte
    if date <= end_of_support:
        time_factor = 0.5  # aún recibe parches
    else:
        months_since_end = (date.year - end_of_support.year) * 12 + (date.month - end_of_support.month)
        time_factor = 1 + 0.1 * months_since_end  # riesgo sube cada mes sin soporte

    # Riesgo total
    risk = base_risk * popularity_factor * industry_factor * time_factor
    return min(risk, 1.0)  # límite en 1 (100%)

# Calcular riesgos mensuales
risks = [calculate_risk(date) for date in dates]

# Crear DataFrame
df = pd.DataFrame({'Fecha': dates, 'Riesgo de Ransomware': risks})

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(df['Fecha'], df['Riesgo de Ransomware'], color='red', linewidth=2)
plt.axvline(end_of_support, color='black', linestyle='--', label='Fin de soporte (Windows 10)')
plt.title('Predicción del Riesgo de Ransomware - Uso Continuado de Windows 10 en Hotelería')
plt.xlabel('Fecha')
plt.ylabel('Riesgo (0 a 1)')
plt.ylim(0, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
