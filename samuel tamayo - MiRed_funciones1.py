# red social de samuel tamayo y carolina paternina :)
#somos los mejores, tenemos unas ideas geniales y aun mas importante. todo que lo se ve en esta red esta hecho por parte de nosotros sin ningun plagio. :)


def diHola(nombre):     #funcion numero 1
  print("¿como estas!?")

  

def saludo(vijuego):    #funcion numero 2
    print(f"mi video juego favorito se llama {vijuego} ")


def gustanombre (apodo)     #funcion numero 3
    print ("gracias por confiar en nosostros:)", apodo)

def gen ( genero):
    print("su genero es:", genero)
    
def pais (paisnacimiento):
        print("su pais de nacimiento es:", paisnacimiento)
    



print("bienvenido a....")
print('''
  ######    ##   ##  ######    ##  ##   ######   ##       #####
##      ##  ##   ##  ##   ##   ##  ##   ##       ##       ##  ##
##      ##  ##   ##  ##   ##   ##  ##   ##       ##       ##  ##
##      ##  ##   ##  ##   ##   ######   ####     ##       #####
##      ##  ##   ##  #####     ##  ##   ##       ##       ##
##      ##  ##   ##  ##  ##    ##  ##   ##       ##       ##
  ######    #######  ##  ##    ##  ##   ######   ######   ##
''')

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a ourhelp")
print()
genero = input("por favor ingresa M si eres hombre, F si eres mujer o N si no te siente identificado con ser hombre o mujer")
print ()
diHola ("")    #primer llamado de la funcion
#segundo llamado de funcion 
vijuego= input ("ingresa el no,mbre de tu juego favorito:")

saludo ()

apodo = input("es muy importante para nosotros conectarnos con usted. por ende le pediremos en favor de que escriba aqui como le gusta que lo llamen: ")
print()

# Cálculo de edad
paisnacimiento= input(nombre, " ingrese ingrese el pais en el cual ha nacido:")
print
agneo = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2017-agneo-1
print()

# Cálculo de estatura
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Di­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))


                                                                                                                                                                                                                                                                                                                                                                                          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>| |   |   |   |   |   °>                                                                                                                  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
gen ()
print("Edad:    ", edad, "años")
pais ()

print("Estatura:", estatura_m, "metros y", estatura_cm, "centi­metros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con ourhelp tu red social aliada")
print()

#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje al publico en general
    ")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    #Código para la opción 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        print("--------------------------------------------------")
        print("Nombre:   ", nombre)
        print("Edad:     ", edad, "años")
        print("Estatura: ", estatura_m, "m y ", estatura_cm, "centí­metros")
        print("Amigos:   ", num_amigos)
        print("--------------------------------------------------")

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        #Repetimos el código para solicitar datos
        # Solicitud de nombre
        nombre = input("Para empezar, dime como te llamas. ")
        print()
        print("Hola ", nombre, ", bienvenido a Mi Red")
        print()

        # Cálculo de edad
        agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
        edad = 2017-agno-1
        print()

        # Cálculo de estatura
        estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dí­melo en metros. "))
        estatura_m = int(estatura)
        estatura_cm = int( (estatura - estatura_m)*100 )

        # Cantidad de amigos
        num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
        # Repetimos el código para mostrar los datos del usuario.
        print("--------------------------------------------------")
        print("Nombre:  ", nombre)
        print("Edad:    ", edad, "años")
        print("Estatura:", estatura_m, "metros y", estatura_cm, "centí­metros")
        print("Amigos:  ", num_amigos)
        print("--------------------------------------------------")
        print()

    #Código para la opción 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    #Código para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar Mi Red. ¡Hasta pronto!")
print()
#Llamado de la funcion para el apodo
gustanombre ()

