import pickle


data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('nombres.pickle', 'wb') as f:
    lista =['Jose','M Mar','Lucia','Eva']
    pickle.dump(lista, f,pickle.HIGHEST_PROTOCOL)
    print("Fichero guardado")
    
with open('nombres.pickle', 'rb') as f:
    lista = pickle.load(f)
    print(lista)
    print("Fichero ledio")