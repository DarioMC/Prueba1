#programa números curiosos
def menu_principal():
    print('Menu Principal \n a.Propiedades \n b.Acerca de \n c.Salir')
    val = input('Digite una opcion :')
#    return val
    if validar_opcion1(val):
        return val
    else:
        print('error')
        return menu_principal()


def validar_opcion1(val):
    if val == 'a' or val == 'b' or val == 'c' :
        return True
    else :
        return False


    

def distribuyeFuncion(val):
    if val == 'a':
        sub_ejecucion()
    else:
        if val == 'b':
            PantallaAcercaDe()
        else:
            PantallaSalir()


def PantallaAcercaDe():
    print('Autor: Darío Monestel Corella\n carné : 2014073400  \n Fecha: 03/09/15 \n Descrición del programa : Menú que ofrece al usuario la ejecucion de programas de numeros curiosos \n Observaciones del programa: este programa necesita ser optimizado')

'''
prueba
>>> main_program()
Menu Principal 
 a.Propiedades 
 b.Acerca de 
 c.Salir
Digite una opcion :b
Autor: Darío Monestel Corella
 carné : 2014073400  
 Fecha: 03/09/15 
 Descrición del programa : Menú que ofrece al usuario la ejecucion de programas de numeros curiosos 
 Observaciones del programa: este programa necesita ser optimizado
>>> 
'''

    
def PantallaSalir():
    print('gracias por usar este programa ')


##########################################################################
'''
Programa :  Números amigos
Descripción : Dos números amigos son dos números enteros positivos m y n tales que la suma de los divisores propios
                      de uno es igual al otro número y viceversa.
Pruebas:
#1
>>> main_program()
Menu Principal 
 a.Propiedades 
 b.Acerca de 
 c.Salir
Digite una opcion :a
a.Números Amigos 
 b.Número Perfecto 
 c.Número Malvado 
 d.Regresar
Digite una opcion :a
ingrese primer valor numerico220
ingrese segundo valor numerico284
los numeros 220 y 284 son amigos
>>> 
#2
>>> main_program()
Menu Principal 
 a.Propiedades 
 b.Acerca de 
 c.Salir
Digite una opcion :a
a.Números Amigos 
 b.Número Perfecto 
 c.Número Malvado 
 d.Regresar
Digite una opcion :a
ingrese primer valor numerico284
ingrese segundo valor numerico298
los numeros 284 y 298 no son amigos

                      
'''
def amigo1(n): #funcion que retorna la suma de los divisores propios de n ,sea  n, numero positivo
        suma = 0
        i = 1
        while i < n :
                if n % i == 0:
                        suma += i
                i += 1
        return suma
        
        
     

def amigo2(m): #funcion que retorna la suma de los divisores propios de m ,sea  m, numero positivo
        suma = 0
        i = 1
        while i < m :
                if m % i == 0:
                        suma += i
                i += 1
        return suma
        
     
def numAmigos(): #funcion encargada de recibir dos valores numericos positivos  
    n = int(input('ingrese primer valor numerico'))
    m = int(input('ingrese segundo valor numerico'))
    
    if amigo1(n) == m and amigo2(m) == n: #condicional encargado de comparar el valor retornado de la funcion amigo1 y amigo 2
                                                                       #con los valores de entrada para verificar si la pareja de numeros es par
        print ('los numeros %d y %d son amigos' %(n,m) )
    else:
        print ('los numeros %d y %d no son amigos' %(n,m) )



#######################################################################
'''
Programa :  Número perfecto
Descripción : cifra numerica positiva donde la suma de sus divisores propios es igual a la misma cifra
Pruebas:
#1
>>> main_program()
Menu Principal 
 a.Propiedades 
 b.Acerca de 
 c.Salir
Digite una opcion :a
a.Números Amigos 
 b.Número Perfecto 
 c.Número Malvado 
 d.Regresar
Digite una opcion :b
ingrese valor numerico positivo :6
el número 6 es perfecto

#2
>>> main_program()
Menu Principal 
 a.Propiedades 
 b.Acerca de 
 c.Salir
Digite una opcion :a
a.Números Amigos 
 b.Número Perfecto 
 c.Número Malvado 
 d.Regresar
Digite una opcion :b
ingrese valor numerico positivo :14
el número 14 no es perfecto
'''

        
def num_perfect(): #funcion encargada de recibir una entrada numerica e introducirla a un ciclo para obtener la suma de
                               # sus divisores propios y compararla si es igual a la varible num 
        num = int(input('ingrese valor numerico positivo :'))
        suma = 0
        i = 1
        while i < num :
                if num % i == 0:
                        suma += i
                i += 1
        if suma == num: #return suma y compara
            
            print ('el número %d es perfecto' %(num ))
        else:
                print ('el número %d no es perfecto' %(num ))



                


#########################################################################
'''
Programa :  Número malvado
Descripción : cifra en forma binaria en la cual se cumpla que su cantidad de unos es par es número malvado
Pruebas:
#1
>>> main_program()
Menu Principal 
 a.Propiedades 
 b.Acerca de 
 c.Salir
Digite una opcion :a
a.Números Amigos 
 b.Número Perfecto 
 c.Número Malvado 
 d.Regresar
Digite una opcion :c
ingresar valor numerico15
el número es malvado

#2

>>> main_program()
Menu Principal 
 a.Propiedades 
 b.Acerca de 
 c.Salir
Digite una opcion :a
a.Números Amigos 
 b.Número Perfecto 
 c.Número Malvado 
 d.Regresar
Digite una opcion :c
ingresar valor numerico7
número no es malvado 
'''

def convertir(num,posicion=0): #funcion que convierte de decimal a binario
    
    if num < 2 :
        return num * (10 ** posicion)
    else: 
        return (num % 2) * (10 ** posicion) + convertir(num//2,posicion + 1)

def contar_dyc(n,d=1): #funcion que cuenta unos en una cifra binaria y retorna su suma
    if  n == 0:
        return 0
    else:
        if n % 10 == d :
            return 1 + contar_dyc(n//10,d)
        else:
            return contar_dyc(n//10,d)

def esNumPar(n): #funcion que verifica si la cifra n es par o no  
    if n % 2 == 0 :
        print("el número es malvado")
    else :
        print("número no es malvado ")


def num_malvado():  #funcion principal que ejecuta si un numero es malvado   
    num = int(input('ingresar valor numerico'))
    n = convertir(num,posicion=0)  
    apolo =  contar_dyc(n,d=1)       
    comprobar = esNumPar(apolo)
    return comprobar
    




#######################################################################





def MenuPropiedades():
    print('a.Números Amigos \n b.Número Perfecto \n c.Número Malvado \n d.Regresar')
    val2 = input('Digite una opcion :')
    if validar_opcion2(val2):
        return val2
    else:
        print('error')
        return menu_principal()


    

def validar_opcion2(val2):
    if val2 == 'a' or val2 == 'b' or val2 == 'c'  or val2 == 'd' :
        return True
    else :
        return False

def distribuyeFuncion2(val2):
    if val2 == 'a':
        numAmigos()
    elif val2 == 'b':
        num_perfect()
    else:
        if val2 == 'c':
            num_malvado()
        else:
            menu_principal()#MenuPropiedades()
            
            



##################################################################################




    
def main_program():      #Funcion principal encargada de ejecutar el programa
    
    opcion = ''
    if opcion != 'c':
        opcion = menu_principal()
        distribuyeFuncion (opcion)
        
def sub_ejecucion():
    
    opcion2 = ''
    if opcion2 != 'd':
        opcion2 = MenuPropiedades()
        distribuyeFuncion2 (opcion2)
      



###################################################################################### 
