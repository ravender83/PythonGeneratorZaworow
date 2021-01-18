import os

def liste(lista):
    for k, i in enumerate(lista):
        print(f"{k} => '{i}'")
    print('\n')
	
def slownik(lista):
    for k, i in lista.items():
        print(f"{k} => '{i}'")
    print('\n')
	
def czy_pliki_istnieja(lista_plikow):
    _brakujace = []
    for plik in lista_plikow:
        if not os.path.isfile(plik):
            _brakujace.append(os.path.basename(plik))
    return _brakujace