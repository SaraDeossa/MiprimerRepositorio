lista=({
    "nombre":"Ana",
    "edad":21,
    "riwipoints":10
},
{
    "nombre":"Sara",
    "edad":25,
    "riwipoints":12
},
{
    "nombre":"shirly",
    "edad":21,
    "riwipoints":14
},
{
    "nombre":"Marilyn",
    "edad":28,
    "riwipoints":9
},
{
    "nombre":"Juan",
    "edad":17,
    "riwipoints":22
    })

nombre=""
edad=""
riwipoints=""


menu=""""
(1) registrar un nuevo coder
(2) actualizar coder
(3) eliminar coders
(4) listar coders
(5) finalizar programa
"""

print(menu)

opcion=input("Ingrese una opcion -> ")
while True:
    if opcion=="1":
        nombre=input("ingrese el nombre del coder a registrar -> ")
        edad=int(input("ingrese la edad del coder -> "))
        riwipoints=float(input("ingrese los riwipoints del coder -> "))
        print ("EL CODER HA SIDO REGISTRADO") 

    if opcion=="2":
        lista=input("ingrese el nombre a modificar -> ")
        for opcion in menu:
            nombre=input("nuevo nombre -> ")
            edad=int(input("nueva edad ->"))
            riwipoints=float(input("nuevos riwipionts ->"))
            print ("EL CODER HA SIDO ACTUALIZADO")
            
    elif opcion=="3":
        lista=input("INGRESA EL NOMBRE DEL CODER A ELIMINAR -> ")
        print("EL CODER HA SIDO ELIMINADO")

    elif opcion=="4":
        for i in lista:
            print(f"{nombre},{edad},{riwipoints}") 




    elif opcion=="5":
        print("HASTA PRONTO")  





# istar_coders():
#     print("Lista de coders:")
#     for coder in coders:
#         print(f"Nombre: {coder.nombre}, Edad: {coder.edad}, Riwipoints: {coder.riwipoints}")


#  print("LISTA DE TODOS LOS CODERS") 
#         print("nombre, edad y riwipoints") 

# def agregar_codigo(nuevo):
#     global nombre,edad,riwipoints ,coders 
#     nombre =nuevo["nombre"] 
#     edad =nuevo["edad"]
#     riwipoints =nuevo["riwipoints"]
#     coders.append({"nombre":nombre,"edad":edad,"riwipoints":riwipoints})


