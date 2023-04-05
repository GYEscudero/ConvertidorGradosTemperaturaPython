# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:37:26 2023

@author: Gerson Yaser Escudero

Convertidor de grados de temmperatura
"""

introduccion = """
Seleccione la unidad con la que va insertar los grados:
[c] Celsius.
[k] Kelvin.
[f] Farenheit."""

print (introduccion)
#------------------------------------------------------------------------------
def menucelcius (gra_cel):
    
    intro_celcius = """
    Seleccione la convercion:
    [1]Celcius a Kelvin
    [2]Celcius a Farenheit"""
    print (intro_celcius)
    
    op_celcius = input ( '' )
    if op_celcius == '1':
        
        celcius_a_kelvin = gra_cel + 273.15
        respuesta_cel = print ( '{}°K'.format( celcius_a_kelvin ) )
        
    
    elif op_celcius == '2':
        
        celcius_a_fare = ( gra_cel * (9 / 5) ) + 32
        respuesta_cel = print ( '{}°F'.format( celcius_a_fare ) )   
    
    else:
        
        respuesta_cel = print ('Opcion no valida.')
    
    return respuesta_cel
#------------------------------------------------------------------------------
def menukel (gra_kel):
    
    intro_kelvin = """
    Seleccione la convercion:
    [1]Kelvin a Celcius
    [2]Kelvin a Farenheit"""
    print (intro_kelvin)
    
    op_kelvin = input ( '' )
    
    if op_kelvin == '1':
        
        kelvin_a_celcius = gra_kel - 273.15
        respuesta_kel = print ( '{}°C'.format( kelvin_a_celcius ) )
        
    
    elif op_kelvin == '2':
        
        kelvin_a_fare = ( ( gra_kel - 273.15) * (9 / 5) ) + 32
        respuesta_kel = print ( '{}°F'.format( kelvin_a_fare ) )   
    
    else:
        
        respuesta_kel = print ('Opcion no valida.')
    
    return respuesta_kel
#------------------------------------------------------------------------------
def menufare (gra_faren):
    
    intro_faren = """
    Seleccione la convercion:
    [1]Farenheit a Celcius
    [2]Farenheit a Kelvin"""
    print (intro_faren)
    
    op_faren = input ( '' )
    
    if op_faren == '1':
        
        faren_a_celcius = ( gra_faren - 32 ) * ( 5 / 9 )
        respuesta_faren = print ( '{}°C'.format( faren_a_celcius ) )
        
    
    elif op_faren == '2':
        
        faren_a_kelvin = ( ( gra_faren - 32) * (5 / 9) ) + 273.15
        respuesta_faren = print ( '{}°K'.format( faren_a_kelvin ) )   
    
    else:
        
        respuesta_faren = print ('Opcion no valida.')
    
    return respuesta_faren
#------------------------------------------------------------------------------
def menu (op):

    if opcion == 'c' or opcion == 'C':
    
        #pass
        gradoscelcius = float ( input ( 'Ingrese los grados Celcius: ' ) )
        resu_cel = menucelcius ( gradoscelcius )
        print (resu_cel)
        

    elif opcion == 'k' or opcion == 'K':
        
        #pass
        gradoskelvin = float ( input ( 'Ingrese los grados Kelvin: ' ) )
        resu_kel = menukel ( gradoskelvin )
        print (resu_kel)
         
    elif opcion == 'f' or opcion == 'F':
        
        #pass
        gradosfarenheit = float ( input ( 'Ingrese los grados Farenheit: ' ) )
        resu_fare = menufare ( gradosfarenheit )
        print (resu_fare)
        
    else:
        
        print ( 'Ingreso una opcion invalida' )
           
#------------------------------------------------------------------------------
opcion = input ('' )
menu ( opcion  )


    



