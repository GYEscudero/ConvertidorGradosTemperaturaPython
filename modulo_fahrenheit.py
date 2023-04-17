"""
Programa que reliza la converción de grados de temperatura
Autor: Gerson Yaser Ecudero Bejarano.
Fecha: 17 de Abril de 2023

Programa: Modulo Fahrenheit.
"""
#---------------------------------------------------------------------------------------------------
def fahrenheit_convertidor (gra_fahrenheit):

    menu_fahrenheit = """
    Escoge la conversión a realizar:
    [1] Fahrenheit a Ceisius.
    [2] Fahrenheit a Kelvin.
    [3] Salir del Programa"""
 
    print (menu_fahrenheit)
    opcion_fahrenheit = input("Elija una opcion: ")

    if  opcion_fahrenheit == '1': #Fahrenheit a Ceisius.
        #pass
        fahrenheit_a_celcius = ( gra_fahrenheit - 32 ) * ( 5 / 9 )
        return  print ( f"{ gra_fahrenheit}°F ={fahrenheit_a_celcius }°C" )
        
    elif opcion_fahrenheit == '2': #Fahrenheit a Kelvin.
        #pass
        fahrenheit_a_kelvin = ( ( gra_fahrenheit - 32) * (5 / 9) ) + 273.15
        return  print ( f"{ gra_fahrenheit}°F ={fahrenheit_a_kelvin }°K" )

    elif opcion_fahrenheit == '3': #Salir del programa
        #pass
        print ("¡Hasta pronto!")
        return 0

    else: #Opción erronea
      print("Opcion erronia, vuelva a intentarlo." )
      return fahrenheit_convertidor (gra_fahrenheit)

