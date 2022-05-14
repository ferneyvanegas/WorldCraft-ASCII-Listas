import random

def get_longs(dim):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    ----------
    Return:
    ----------
    longs: list
        Listado de referencias a largos de fila
    '''
    longs = [
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim)
    ]

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # longs = [5,2,2,1]
    return longs