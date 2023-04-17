"""
Programa que reliza la converción de grados de temperatura
Autor: Gerson Yaser Ecudero Bejarano.
Fecha: 17 de Abril de 2023

Programa: Principal.
"""

#Protocolos de función
from modulo_celsius import celsius_convertidor
from modulo_kelvin import kelvin_convertidor
from modulo_fahrenheit import fahrenheit_convertidor

#---------------------------------------------------------------------------------------------------
def main ():

    grados = float (input("Ingrese los grados con los que se trabajara:  "))

    
    
    menu_principal = """
    Escoge el tipo de grados con los que deseas a trabajar la conversión:
    [1] Ceisius
    [2] Kelvin
    [3] Fahrenheit
    [4] Salir del Programa"""

    print ( menu_principal  )
    opcion = input("Elija una opcion: ")

    if  opcion == '1': #Grados Celsius
        #pass
        resultado = celsius_convertidor (grados)
        
        if resultado == 0:
            return 0
        
        else: 
            resultado 
        
    elif opcion == '2': #Grados Kelvin
        #pass
        resultado = kelvin_convertidor (grados)
        
        if resultado == 0:
            return 0
            
        else: 
            resultado 

    elif opcion == '3': #Grados Fahrenheit
        #pass
        resultado = fahrenheit_convertidor (grados)
        
        if resultado == 0:
            return 0
        
        else: 
            resultado 

    elif opcion == '4': #Salir del programa
        #pass
        print ("¡Hasta pronto!")
        return 0

    else: #Opción erronea
      print("Opcion erronia, vuelva a intentarlo." )
      return main()
#---------------------------------------------------------------------------------------------------

if  __name__ == "__main__":

    main  ()
