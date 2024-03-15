# 1.Crea un diccionario llamado persona con propiedades como nombre, edad y ciudad. 


personas={
    "nombre":"Sara",
    "edad":25,
    "ciudad":"Medellin"
}

# 2. Agrega una propiedad adicional al diccionario persona que represente su ocupación. 


personas["ocupacion"]="manicurista"

print(personas)



# 3. Accede a una propiedad del diccionario persona y muestra su valor en la consola.


print(personas["edad"])


# 4. Crea otro diccionario llamado libro con propiedades como título, autor y año de publicación. 

Libro={
    
    "titulo":"combres borrascosas",
    "autor":"Emily Bronte",
    "año de publicacion":1847

}

print(Libro)


# 5. Combina las propiedades de los diccionarios persona y libro en un nuevo diccionario llamado informacion. 


informacion=[personas|Libro]
print(informacion)

# 6. Cambia el valor de una propiedad en el diccionario persona. 


personas["nombre"]="melody"
print(personas)


# 7. Elimina una propiedad del diccionario libro.


del Libro ["año de publicacion"]
print(Libro)


# 8. Crea un diccionario llamado coche con propiedades como modelo, marca y año. 

coche={
    "modelo":"chevrolet orix",
    "marca":"chevrolet",
    "año":"2022"
}

# 9. Muestra todas las propiedades del diccionario coche en la consola.

print(coche)

# 10. Crea un diccionario llamado circulo con propiedades como radio y color.

radio=22
color="negro"

circulo={
    "radio":radio,
    "color":"negro"
}

# 11. Calcula el área del círculo utilizando la fórmula A = PI* R² y muestra el resultado.

AreaCirculo=(3.1416*(radio**2))
print(AreaCirculo)


# 12. Crea un diccionario llamado rectángulo con propiedades como ancho y alto.

rectangulo={
    "ancho":22,
    "alto":15
}


# 13. Calcula el perímetro del rectángulo utilizando la fórmula P = 2 * (ancho + alto) y muestra el resultado. 


PerimetroRectangulo=2*(rectangulo["ancho"]+rectangulo["alto"])
print("el perimetro es -> ", PerimetroRectangulo)


# 14. Combina las propiedades de los diccionarios circulo y rectángulo en un nuevo diccionario llamado formas. 

formas=[circulo|rectangulo]
print(formas)


# 15. Crea un diccionario llamado computadora con propiedades como marca, modelo y precio. 

computadora={
    "marca":"apple",
    "modelo":"2023",
    "precio":"2.500.000"

}

# 16. Muestra el precio de la computadora en la consola. 

print(computadora["marca"])

# 17. Agrega una propiedad al diccionario computadora que indique si tiene o no una tarjeta gráfica. 

computadora["tarjeta grafica"]="SI"
print(computadora)


# 18. Crea un diccionario llamado mascota con propiedades como nombre, especie y edad. 

mascotas={

    "nombre":"Mango",
    "especie":"criollo",
    "edad":1
}


# 19. Muestra en la consola la especie de la mascota en mayúsculas.

print(mascotas["especie"].upper())


# 20. Crea un diccionario llamado fruta con propiedades como nombre y color.



Fruta={

    "nombre":input("ingresa una fruta ->"),
    "color":input("ingresa un color ->")
}

# 21. Crea un diccionario llamado estudiante con propiedades como nombre, edad y calificaciones.


estudiante={

    "nombre":input("Ingresa tu nombre ->"),
    "edad":int(input("Ingresa tu edad->")),
    "calificacion1":int(input("Ingresa tu calificacion de ingles->")),
    "calificacion2":int(input("Ingresa tu calificacion de español->")),
    "calificacion3":int(input("Ingresa tu calificacion de religion->"))
    } 

# 22. Muestra en la consola el promedio de las calificaciones del estudiante.

calificaciones=estudiante["calificacion1"]+estudiante["calificacion2"]+estudiante["calificacion3"]
promedio=calificaciones/3

print("El promedio de tus notas es : ", promedio)

# 23. Agrega una propiedad al diccionario estudiante que indique si ha aprobado o no.

if calificaciones >=6:
    estado="APROBADO"

else:
    estado="NO APROBADO"

estudiante["estado"]=estado

print(estudiante)






num1=int(input("Ingresa el primer digito -"))
num2=int(input("ingresa el segundo digito ->"))

if(num1<=num2):
    print("El primer numero es menor")

if(num2<=num1):
    print("El segundo numero es menor")




# 1. ¿Es 35 mayor que 25? 


num1=int(input("por favor ingresa el primer numero ->"))
num2=int(input("por favor ingresa el segundo numero ->"))

if(num1>=num2):
    print("El primer numero es mayor")

if(num2>=num1):
    print("El segundo numero es mayor")