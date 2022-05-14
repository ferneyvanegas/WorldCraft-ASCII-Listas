'''
    Desarrollado por: Ferney Vanegas Hernández
    Misión TIC 2022
    Versión : 1.0.1
    Título: Reto 4
'''

import modules.rows as r
import modules.columns as c
import modules.widhts as w
import modules.longs as l
import modules.walls as wall

def main():
    dim = int(input('Ingresa un número para dimensionar el tablero (cuadrado Dim x Dim). Ej:2 (Para crear un tablero de 2x2\n'))
    # OBTENCIÓN DE LISTAS BASE
    # ============================
    # Cuando paso a dim como parámetros, le resto uno por la forma en la que se generan aleatorios en las funciones
    rows = r.get_rows(dim - 1)
    columns = c.get_columns(dim - 1)
    widths = w.get_widths(dim - 1)
    longs = l.get_longs(dim - 1)
    # ============================

    # OBTENCIÓN DE COORDENADAS
    coord_walls = wall.get_coord_walls(rows,columns, widths, longs, dim - 1)

    # CONTRUCCIÓN DE MAPA
    print(
        f'--------------------------------------------\n'
        f'+++      COORDENADAS DE CONSTRUCCIÓN     +++\n'
        f'--------------------------------------------\n'
        f'{coord_walls}\n'
        f'--------------------------------------------\n'
        f'+++                MAPA                  +++\n'
        f'--------------------------------------------\n'
    )
    wall.construct_walls(coord_walls, dim)

main()

 