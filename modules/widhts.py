import random

def get_widths(dim):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    ----------
    Return:
    ----------
    widths: list
        Listado de referencias a anchos de fila
    '''
    widths = [
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim), 
        random.randint(0,dim)
    ]

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # widths = [2,9,1,4]
    return widths