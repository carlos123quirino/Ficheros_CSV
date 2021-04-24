
import pandas as pd
print("BIENVENIDO")
numero=int(input ("Numeros de alumnos a regristrar\n"))

df=pd.DataFrame()
for i in range (numero):
    i=i+1
    print("Ingresa los datos del alumno a registrar")
    nombre = (input("Nombre:\t"))
    apellidos = (input("Apellidos:\t"))
    edad = int(input("Edad:\t"))
    grado = int(input("Grado:\t"))
    grupo = int(input("Grupo:\t"))
    correo = (input("Email:\t"))

    data = {'Nombre': [nombre],
        'Apellidos': [apellidos],
        'Edad': [edad],
        'Grado': [grado],
        'Grupo': [grupo],
        'Email': [correo]}
    
    save=int(input("<<Guardar y Salir>> \n 1.- Si \n 2.- No "))
    df=df.append(data,ignore_index=True)
    
    if (save == 1):
        df.to_csv('registros.csv')
    else:
        print("BUEN TRABAJO...GRACIAS POR LOS REGISTROS..!!")




