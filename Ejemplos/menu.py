import Ejemplos.ciclo_while as CW
def ejemploWhile():
  
  iniciar=True
  while iniciar:
    numero=int(input("digite el número a multiplicar y para salir digite cero 0 "))
    if numero!=0:
     #CW.ciclo_while1(numero)
     #CW.ciclo_while2(numero)
     CW.ciclo_while3(numero)
    else:
      iniciar=False