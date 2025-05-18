import json
from tabulate import tabulate
import re
from datetime import datetime

hojas_vida = []
correos = set()

def validar_nombre_completo(nombre):
    return len(nombre.strip().split()) >= 2

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validar_correo(correo):
    return '@' in correo and (correo.endswith('.com') or correo.endswith('.co'))

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def registro_hoja_vida():
    while True:
        nombre = input("Ingresa el nombre completo: ")
        if validar_nombre_completo(nombre):
            break
        else:
            print("Debe ingresar nombre completo (mínimo dos palabras).")

    while True:
        documento_id = input("Ingresa el documento de identidad: ")
        if validar_telefono(documento_id):
            break
        else:
            print("El documento debe tener exactamente 10 dígitos numéricos.")

    direccion = input("Ingresa la direccion: ")

    while True:
        telefono = input("Ingresa tu telefono: ")
        if validar_telefono(telefono):
            break
        else:
            print("El teléfono debe tener exactamente 10 dígitos.")

    while True:
        correo = input("Ingresa el correo electrónico: ")
        if validar_correo(correo):
            break
        else:
            print("El correo debe contener '@' y terminar en .com o .co.")

    if correo in correos:
        print("Correo ya existente; ingresa uno nuevo...")
        return
    else:
        correos.add(correo)

    while True:
        fecha_nacimiento = input("Ingresa la fecha de nacimiento (DD/MM/AAAA): ")
        if validar_fecha(fecha_nacimiento):
            break
        else:
            print("Formato de fecha incorrecto. Debe ser DD/MM/AAAA.")

    validacion = (fecha_nacimiento, documento_id)

    formacion = []
    while True:
        print("\n====== FORMACION ACADEMICA ======\n")
        institucion = input("Ingresa la institucion educativa: ")
        titulo = input("Ingresa el titulo obtenido: ")
        experiencia = input("Ingresa años cursados: ")
        formacion.append({'institucion': institucion, 'titulo': titulo, 'experiencia': experiencia})

        if input("¿Deseas ingresar otra formación? (s/n): ").lower() != "s":
            break

    experiencia = []
    tiene_experiencia = input("¿Tienes experiencia laboral? (s/n): ").lower()
    if tiene_experiencia == "s":
        while True:
            empresa = input("Nombre de la empresa en la que laboraste: ")
            cargo = input("Nombre del cargo desempeñado: ")
            funciones = input("Ingresa las funciones realizadas: ")
            while True:
                duracion = input("Ingresa el tiempo laborado (en meses): ")
                if duracion.isdigit():
                    break
                else:
                    print("La duración debe estar en meses (número).")
            experiencia.append({'empresa': empresa, 'cargo': cargo, 'funciones': funciones, 'duracion': duracion})

            if input("¿Deseas ingresar otra experiencia? (s/n): ").lower() != "s":
                break
    else:
        experiencia = "Sin experiencia"

    referencia_personales = []
    while True:
        print("\n====== REFERENCIAS PERSONAL/LAORAL ======\n")
        while True:
            nombre_ref = input("Ingresa el nombre de la referencia: ")
            if validar_nombre_completo(nombre_ref):
                break
            else:
                print("Debe ingresar nombre completo (mínimo dos palabras).")
        parentesco = input("Relacion (Laboral / Personal): ")
        while True:
            telefono_ref = input("Telefono de la referencia: ")
            if validar_telefono(telefono_ref):
                break
            else:
                print("El teléfono debe tener exactamente 10 dígitos.")
        referencia_personales.append({'nombre_ref': nombre_ref, 'parentesco': parentesco, 'telefono_ref': telefono_ref})

        if input("¿Deseas ingresar otra referencia? (s/n): ").lower() != "s":
            break

    habilidades = []
    while True:
        print("\n====== HABILIDADES ======\n")
        habilidad = input("¿Cuáles son tus habilidades? ")
        habilidades.append(habilidad)

        if input("¿Deseas ingresar otra habilidad? (s/n): ").lower() != "s":
            break

    hoja_vida = {
        'nombre': nombre,
        'documento_id': documento_id,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'fecha_nacimiento': fecha_nacimiento,
        'validacion': validacion,
        'formacion': formacion,
        'experiencia': experiencia,
        'referencia_personales': referencia_personales,
        'habilidades': habilidades
    }

    hojas_vida.append(hoja_vida)
    print("La hoja de vida se añadió exitosamente.")

def consultar_hoja_vida():
    busqueda = input("Buscar por (nombre/documento_id/correo): ").strip().lower()
    valor = input(f"Ingrese el {busqueda}: ").strip().lower()

    for hoja_vida in hojas_vida:
        if str(hoja_vida.get(busqueda, "")).strip().lower() == valor:
            print(tabulate(hoja_vida.items(), headers=["Campo", "Valor"], tablefmt="grid"))
            return
    print("No se encontró la hoja de vida con ese criterio...")

def exportar_json():
    with open("hojas_exportadas.json", "w", encoding="utf-8") as archivo:
        json.dump(hojas_vida, archivo, indent=4, ensure_ascii=False)
    print("Las hojas de vida fueron exportadas a 'hojas_exportadas.json'.")

def reporte_experiencia():
    limite = int(input("Mostrar los candidatos con al menos X años de experiencia: "))
    candidatos = []

    for hoja_vida in hojas_vida:
        if isinstance(hoja_vida["experiencia"], str):  # "Sin experiencia"
            continue
        total_meses = 0
        for exp in hoja_vida["experiencia"]:
            try:
                dur = int(exp["duracion"])
                total_meses += dur
            except:
                continue
        if total_meses >= limite * 12:
            candidatos.append([hoja_vida["nombre"], hoja_vida["correo"], total_meses // 12])

    print(tabulate(candidatos, headers=["Nombre", "Correo", "Años de experiencia"], tablefmt="grid"))

def main():
    while True:
        print()
        print("1. Registrar hoja de vida")
        print("2. Consultar hoja de vida")
        print("3. Exportar hoja de vida")
        print("4. Generar reportes por experiencia")
        print("5. Salir\n")

        op = int(input("Seleccione una opción: "))

        if op == 1:
            registro_hoja_vida()
        elif op == 2:
            consultar_hoja_vida()
        elif op == 3:
            exportar_json()
        elif op == 4:
            reporte_experiencia()
        elif op == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida....")

main()
