"""
Programa que reliza la converción de grados de temperatura
Autor: Gerson Yaser Ecudero Bejarano.
Fecha: 17 de Abril de 2023

Programa: Modulo Kelvin.
"""
#---------------------------------------------------------------------------------------------------
def kelvin_convertidor (gra_kelvin):

    menu_kelvin = """
    Escoge la conversión a realizar:
    [1] Kelvin a Ceisius.
    [2] Kelvin a Fahrenheit.
    [3] Salir del Programa"""

    print (menu_kelvin)
    opcion_kelvin = input("Elija una opcion: ")

    if  opcion_kelvin == '1': #Kelvin a Ceisius.
        #pass
        kelvin_a_celcius = gra_kelvin - 273.15 
        return  print ( f"{ gra_kelvin}°K ={kelvin_a_celcius }°C" )
        
    elif opcion_kelvin == '2': #Kelvin a Fahrenheit.
        #pass
        kelvin_a_fahrenheit =( ( gra_kelvin - 273.15) * (9 / 5) ) + 32
        return  print ( f"{gra_kelvin}°K ={kelvin_a_fahrenheit }°F" )

    elif opcion_kelvin == '3': #Salir del programa
        #pass
        print ("¡Hasta pronto!")
        return 0

    else: #Opción erronea
      print("Opcion erronia, vuelva a intentarlo." )
      return kelvin_convertidor (gra_kelvin)

