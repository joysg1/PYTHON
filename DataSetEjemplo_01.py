import csv
import matplotlib.pyplot as plt
import pandas as pd




# Lista de sistemas operativos
operating_systems = ["Windows", "Android", "iOS", "OS X", "Unknown", "Linux", "Series 40",
                     "SymbianOS", "Samsung", "BlackBerry OS", "Chrome OS", "Nokia Unknown",
                     "Playstation", "Sony Ericsson", "KaiOS", "Xbox", "bada", "Tizen",
                     "LG", "Nintendo", "Other"]

# Lectura de datos desde el archivo CSV
data = {"Date": [], "Operating Systems": {}}

with open('os_worldwide_update_may_2024.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data["Date"].append(row["Date"])
        for os in operating_systems:
            if os not in data["Operating Systems"]:
                data["Operating Systems"][os] = []
            data["Operating Systems"][os].append(float(row[os]))

# Creación del gráfico
plt.figure(figsize=(12, 8))

for os in operating_systems:
    plt.plot(data["Date"], data["Operating Systems"][os], label=os)

plt.title('Market Share of Operating Systems Over Time')
plt.xlabel('Date')
plt.ylabel('Market Share (%)')
plt.xticks(data["Date"][::12], rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()




# dataset url: https://www.kaggle.com/datasets/michau96/operating-system-market-2009-2023


# video 102 1 h



