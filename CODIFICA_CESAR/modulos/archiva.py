import pickle

def guarda(texto):
    fichero = open("datos.pkl", "wb")
    pickle.dump(texto, fichero)
    #print("Fichero guardado")
    fichero.close()

def carga():
    fichero = open("datos.pkl", "rb")
    dato = pickle.load(fichero)
    #print(dato)
    fichero.close()
    return dato

if __name__ == '__main__':
    guarda("Hola")
    carga()