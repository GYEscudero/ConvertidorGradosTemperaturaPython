"""
Programa que reliza la converción de grados de temperatura
Autor: Gerson Yaser Ecudero Bejarano.
Fecha: 17 de Abril de 2023

Programa: Modulo Celsius.
"""
#---------------------------------------------------------------------------------------------------
def celsius_convertidor (gra_celsius):

    menu_celsius = """
    Escoge la conversión a realizar:
    [1] Ceisius a Kelvin.
    [2] Ceisius a Fahrenheit.
    [3] Salir del Programa"""

    print (menu_celsius)
    opcion_celsius = input("Elija una opcion: ")

    if  opcion_celsius == '1': #Ceisius a Kelvin.
        #pass
        celcius_a_kelvin = gra_celsius + 273.15 
        return  print ( f"{ gra_celsius}°C ={celcius_a_kelvin }°K" )
        
    elif opcion_celsius == '2': #Ceisius a Fahrenheit.
        #pass
        celcius_a_fahrenheit =( gra_celsius * (9 / 5) ) + 32
        return  print ( f"{ gra_celsius}°C ={celcius_a_fahrenheit }°F" )

    elif opcion_celsius == '3': #Salir del programa
        #pass
        print ("¡Hasta pronto!")
        return 0

    else: #Opción erronea
      print("Opcion erronia, vuelva a intentarlo." )
      return celsius_convertidor (gra_celsius)
