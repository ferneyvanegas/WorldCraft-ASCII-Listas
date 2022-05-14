import random

def get_columns(dim):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    ----------
    Return:
    ----------
    columns: list
        Listado de referencias a columnas
    '''
    columns = [
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim)
    ]

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # columns = [1,3,11,12]
    return columns