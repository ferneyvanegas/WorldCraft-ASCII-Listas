import random

def get_rows(dim):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    ----------
    Return:
    ----------
    rows: list
        Listado de referencias a filas
    '''
    rows = [
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim)
    ]

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # rows = [0,3,5,6]
    return rows