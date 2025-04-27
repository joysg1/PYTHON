import matplotlib.pyplot as plt

# Características de OpenMediaVault
features = [
    'Gestión de almacenamiento',
    'Gestión de usuarios',
    'Servicios de red (SMB/NFS/FTP)',
    'RAID software',
    'Sistema de plugins',
    'Monitorización',
    'Actualizaciones automáticas'
]

# Imaginemos una "importancia" relativa de cada característica
importance = [9, 7, 8, 8, 6, 7, 6]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.barh(features, importance, color='skyblue')
plt.xlabel('Importancia (1-10)')
plt.title('Características principales de OpenMediaVault')
plt.gca().invert_yaxis()  # Invertir el eje para que la más importante esté arriba
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
