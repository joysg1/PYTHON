import timeit
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import random
import pandas as pd

# Verificar si los archivos de NLTK están descargados
try:
    nltk.data.find('corpora/words')
except LookupError:
    print("Descargando archivos de NLTK...")
    nltk.download('words')

palabras = set(random.sample(nltk.corpus.words.words(), 1000))

def generar_texto_aleatorio(longitud):
    texto = []
    for _ in range(longitud):
        texto.append(random.choice(list(palabras)))
    return texto

# Número de iteraciones para concatenar
num_iteraciones = [100, 500, 1000]

# Función para concatenar con +
def concat_con_mas(texto):
    resultado = ""
    for palabra in texto:
        resultado += palabra + " "
    return resultado

# Función para concatenar con join
def concat_con_join(texto):
    return " ".join(texto)

# Medir tiempo de ejecución
datos = []

for n in num_iteraciones:
    texto_aleatorio = generar_texto_aleatorio(n)
    tiempo_mas = timeit.timeit(lambda: concat_con_mas(texto_aleatorio), number=1)
    tiempo_join = timeit.timeit(lambda: concat_con_join(texto_aleatorio), number=1)
    datos.append({
        'Número de Palabras': n,
        'Método': '+',
        'Tiempo (segundos)': tiempo_mas
    })
    datos.append({
        'Número de Palabras': n,
        'Método': 'join',
        'Tiempo (segundos)': tiempo_join
    })

df = pd.DataFrame(datos)

# Crear gráfica
sns.set()
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Número de Palabras', y='Tiempo (segundos)', hue='Método')
plt.title('Rendimiento de Concatenación de Cadenas')
plt.show()
