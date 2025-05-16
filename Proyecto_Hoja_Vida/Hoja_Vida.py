import json #para guardar y cargar hojas de vida
from tabulate import tabulate #tabulate para agregar un formato a todos los datos de entrada ingresados por el usuario
#Datos personales
hojas_vida=[]

correos=set()


def registro_hoja_vida():
    
    nombre=input("Ingresa el nombre: ")
    documento_id=input("Ingresa el documento de identidad: ")
    direccion=input("Ingresa la direccion: ")
    telefono=input("Ingresa tu telefono: ")
    correo=input("Ingresa el correo electronico: ")
    
    if correo in correos:
        print("Correo ya existente; ingresa uno  nuevo...")
        return
    else: 
        correos.add(correo)
    
    fecha_nacimiento=input("Ingresa la fecha de nacimiento (DD/MM/AAAA)")

    validacion=(fecha_nacimiento,documento_id)
    
    formacion=[]
    while True:
        institucion=input("Ingresa la institucion educativa: ")
        titulo=input("Ingresa el titulo obtenido: ")
        experiencia=input("Ingresa años cursados: ")
        
        formacion.append({'institucion':institucion,'titulo':titulo,'experiencia':experiencia})
        
        if input("Deseas ingresar otra formacion ? (s/n)").lower() != "s":
            break
        
    experiencia=[]
    while True:
        empresa=input("Nombre de la empresa en la que laboraste: ")
        cargo=input("Nombre del cargo desempeñado: ")
        funciones=input("Ingresa las funciones realizadas: ")
        duracion=input("Ingresa el tiempo laborado: ")
        experiencia.append({'empresa':empresa,'cargo':cargo,'funciones':funciones,'duracion':duracion})
        
        if input("Deseas ingresar otra experiencia ? (s/n)").lower() != "s":
            break

    referencia_personales=[]
    while True:
        nombre_ref=input("Ingresa el nombre de la referencia: ")
        parentesco=input("Relacion (Laboral / Personal): ")
        telefono_ref=input("Telefono de la referencia: ")
        referencia_personales.append({'nombre_ref':nombre_ref,'parentesco':parentesco,'telefono_ref':telefono_ref})
        
        if input("Deseas ingresar otra referencia ? (s/n)").lower() != "s":
            break
        
    habilidades=[]
    while True:
        habilidad=input("Cuales son tus habilidades? ")
        habilidades.append(habilidad)
        
        if input("Deseas ingresar otra habilidad ? (s/n)").lower() != "s":
            break
    
    hoja_vida={
        'nombre':nombre,
        'documento_id':documento_id,
        'direccion':direccion,
        'correo':correo,
        'fecha_nacimiento':fecha_nacimiento,
        'validacion':validacion,
        'formacion':formacion,
        'experiencia':experiencia,
        'referencia_personales':referencia_personales,
        'habilidades':list(habilidades)
    }

    hojas_vida.append(hoja_vida)
    print("La hoja de vida se añadio exitosamente")

def consultar_hoja_vida():
    busqueda=input("Buscar por (nombre/documento/correo)")
    valor=input(f"Ingrese el {busqueda}:  ")

    for hoja_vida in hojas_vida:
        if hoja_vida[busqueda]==valor:
            print(tabulate(hoja_vida.items(),headers=["Campo","Valor"],tablefmt="grid"))
            return
    print("No se encontro la hoja de vida con ese tipo de busqueda...")

def exportar_json():
    with open("Hojas exportadas .json","w",encoding="utf-8") as archivo:
        json.dump(hojas_vida,archivo,indent=4,ensure_ascii=False)
    print("Las hojas de vida fueron exportadas a 'hojas_exportadas.json'")

def reporte_experiencia():
    limite=int(input("Mostrar los candidatos con mas años de experiencia: "))
    candidatos=[]

    for hoja_vida in hojas_vida:
        total_meses=0
        for exp in hoja_vida["Experiencia"]:
            try:
                dur=int(exp["Duracion"].split()[0])
                total_meses += dur*(12 if "año" in exp["Duracion"]else 1)
            except:
                continue
            if total_meses>= limite*12:
                candidatos.append([hoja_vida["nombre"],hoja_vida["correo"],total_meses//12])

    print(tabulate(candidatos,headers=["Nombre","Correo","Años de experiencia"],tablefmt="grid"))

def main():
    while True:
        print()
        print("Bienvenido a VitaeConsole")
        print()
        print("1. Registrar hoja de vida")
        print("2. Consultar hoja de vida")
        print("3. Exportar hoja de vida")
        print("4. Generar reportes por experiencia")
        print("5. Salir")
        print()
        
        op=int(input("Seleccione una opcion: "))

        if op==1:
            registro_hoja_vida()
        elif op ==2:
            consultar_hoja_vida()
        elif op==3:
            exportar_json()
        elif op==4:
            reporte_experiencia()
        elif op==5:
            print("Saliendo del sistema...")
        else:
            print("Opcion no valida....")

main()



