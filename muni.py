cabecera  = {
    "Lempira" : "Gracias" ,
    "Intibuca" : "La esperanza" ,
    "Choluteca" : "Choluteca" ,
    "El paraiso" : "Yuscaran" ,
    "Colon" : "Trujillo" ,
    "Olancho" : "Juticalpa"
}
try:
    print ("Cabeceras de Honduras")
    print ("Ingrese Nombre del Departamento")
    departamento = input("Ingresar depto.: ")
    print("La Cebecera de {} es  {} .".format(departamento, format(cabecera[departamento],)))
except KeyError:
    print("La cabecera no existe") 