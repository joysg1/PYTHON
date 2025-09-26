import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carga los datos desde un archivo CSV
def cargar_datos(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

# Crea el gráfico de tipo scatter matrix
def crear_scatter_matrix(df):
    try:
        sns.pairplot(df)
        plt.show()
    except Exception as e:
        print(f"Error al crear el gráfico: {e}")

# Main
def main():
    ruta_archivo = '/home/userlm/Documentos/WATER_MACHINE_LEARNING/water_potability.csv'  # Reemplaza con la ruta a tu archivo CSV
    df = cargar_datos(ruta_archivo)
    
    if df is not None:
        # Rellena los valores None para evitar errores
        df = df.fillna(df.mean(numeric_only=True))
        
        # Crea el gráfico de tipo scatter matrix
        crear_scatter_matrix(df)

if __name__ == "__main__":
    main()


