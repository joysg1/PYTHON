# Para crear el entorno

# python -m venv <nombre_entono>

# Se creara una carpeta con el nombre del entorno, verla con 
# el comando ls (Linux) o cd (Windows)

# Para activar el entorno

# source <nombre_entorno>/bin/activate


# Una vez activo el entorno podemos instalar las bibliotecas

# Ejemplos:  
# pip install numpy
# pip install pandas (incluye numpy)
# pip install ipython
# pip install jupyter
# pip freeze (lista todas las dependencias instaladas)


# Cuando instalados dependencias es recomendable crear el archivo
# requirements.txt mediante el siguiente comando:
# pip freeze > requirements.txt

# para leer el archivo lo realizamos con cat requirements.txt

# Para desactivar un entorno se realiza mediante el comando:
# deactivate 

# Para instalar las dependencias de un entorno usamos el siguiente
# comando: pip install -r requirements.txt

# Para crear un entorno usando conda utilizamos el siguiente comando:
# conda create -n datos -y

# Para listar todos los entornos usamos el comando:
# conda env list

# Para activar un entorno de conda usamos:
# conda activate <nombre_entorno>

# Para instalar librerias en conda usamos:
# conda install <nombre_libreria>
# Ejemplo conda install tkinter

# Es recomendable crear entornos para cada proyecto
# Para evitar problemas de versiones y compatibilidad

# Es recomendable no usar la version de python 2.7

# Mediante el siguiente comando podemos listar las dependencias 
# instaladas:
# pip freeze

# Quede en el minuto -6.55

