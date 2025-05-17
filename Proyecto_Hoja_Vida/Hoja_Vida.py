
import json  # para guardar y cargar hojas de vida
# tabulate para agregar un formato a todos los datos de entrada ingresados por el usuario
from tabulate import tabulate
# Datos personales
hojas_vida = []

correos = set()


def registro_hoja_vida():

    nombre = input("Ingresa el nombre: ")
    documento_id = input("Ingresa el documento de identidad: ")
    direccion = input("Ingresa la direccion: ")
    telefono = input("Ingresa tu telefono: ")
    correo = input("Ingresa el correo electronico: ")
    
    while True:
        if correo.endswith("@gmail.com"):
            break
        else:
            print("Debes de ingresar un arroba y una extencion de correo electronico(gmail.com)... Intenta de nuevo")
            correo=input("Ingresa de nuevo el correo con las indicaciones anteriores... :")
             
    if correo in correos:
        print("Correo ya existente; ingresa uno  nuevo...")
        return
    else:
        correos.add(correo)

    fecha_nacimiento = input("Ingresa la fecha de nacimiento (DD/MM/AAAA)")

    validacion = (fecha_nacimiento, documento_id)

    formacion = []
    while True:
        institucion = input("Ingresa la institucion educativa: ")
        titulo = input("Ingresa el titulo obtenido: ")
        experiencia = input("Ingresa años cursados: ")

        formacion.append({'institucion': institucion,
                         'titulo': titulo, 'experiencia': experiencia})

        if input("Deseas ingresar otra formacion ? (s/n)").lower() != "s":
            break

    experiencia = []
    while True:
        empresa = input("Nombre de la empresa en la que laboraste: ")
        cargo = input("Nombre del cargo desempeñado: ")
        funciones = input("Ingresa las funciones realizadas: ")
        duracion = input("Ingresa el tiempo laborado: ")
        experiencia.append({'empresa': empresa, 'cargo': cargo,
                           'funciones': funciones, 'duracion': duracion})

        if input("Deseas ingresar otra experiencia ? (s/n)").lower() != "s":
            break

    referencia_personales = []
    while True:
        nombre_ref = input("Ingresa el nombre de la referencia: ")
        parentesco = input("Relacion (Laboral / Personal): ")
        telefono_ref = input("Telefono de la referencia: ")
        referencia_personales.append(
            {'nombre_ref': nombre_ref, 'parentesco': parentesco, 'telefono_ref': telefono_ref})

        if input("Deseas ingresar otra referencia ? (s/n)").lower() != "s":
            break

    habilidades = []
    while True:
        habilidad = input("Cuales son tus habilidades? ")
        habilidades.append(habilidad)

        if input("Deseas ingresar otra habilidad ? (s/n)").lower() != "s":
            break

    hoja_vida = {
        'nombre': nombre,
        'documento_id': documento_id,
        'direccion': direccion,
        'correo': correo,
        'fecha_nacimiento': fecha_nacimiento,
        'validacion': validacion,
        'formacion': formacion,
        'experiencia': experiencia,
        'referencia_personales': referencia_personales,
        'habilidades': list(habilidades)
    }

    hojas_vida.append(hoja_vida)
    print("La hoja de vida se añadio exitosamente")


def consultar_hoja_vida():
    busqueda = input("Buscar por (nombre/documento/correo)")
    valor = input(f"Ingrese el {busqueda}:  ")

    for hoja_vida in hojas_vida:
        if hoja_vida[busqueda] == valor:
            print(tabulate(hoja_vida.items(), headers=[
                  "Campo", "Valor"], tablefmt="grid"))
            return
    print("No se encontro la hoja de vida con ese tipo de busqueda...")


def exportar_json():
    with open("Hojas exportadas .json", "w", encoding="utf-8") as archivo:
        json.dump(hojas_vida, archivo, indent=4, ensure_ascii=False)
    print("Las hojas de vida fueron exportadas a 'hojas_exportadas.json'")


def reporte_experiencia():
    limite = int(input("Mostrar los candidatos con mas años de experiencia: "))
    candidatos = []

    for hoja_vida in hojas_vida:
        total_meses = 0
        for exp in hoja_vida["Experiencia"]:
            try:
                dur = int(exp["Duracion"].split()[0])
                total_meses += dur*(12 if "año" in exp["Duracion"]else 1)
            except:
                continue
            if total_meses >= limite*12:
                candidatos.append(
                    [hoja_vida["nombre"], hoja_vida["correo"], total_meses//12])

    print(tabulate(candidatos, headers=[
          "Nombre", "Correo", "Años de experiencia"], tablefmt="grid"))


def actualizar_hoja():
    print("\n--- Actualizar hoja de vida ---")
    criterio = input("Buscar por (documento/correo): ").lower()
    valor = input(f"Ingrese el {criterio}: ")

    for hoja in hojas_vida:
        if hoja[criterio] == valor:
            print(f"\n📝 Editando hoja de vida de: {hoja['nombre']}")

            print("¿Qué deseas actualizar?")
            print("1. Datos personales")
            print("2. Formación académica")
            print("3. Experiencia laboral")
            print("4. Referencias")
            print("5. Habilidades")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                hoja["nombre"] = input("Nuevo nombre completo: ")
                hoja["contacto"] = input("Nuevo teléfono de contacto: ")
                hoja["direccion"] = input("Nueva dirección: ")
                nuevo_correo = input("Nuevo correo electrónico: ")
                if nuevo_correo != hoja["correo"]:
                    if nuevo_correo in correos:
                        print(
                            " Este nuevo correo ya está registrado. No se actualizó.")
                    else:
                        correos.discard(hoja["correo"])
                        correos.add(nuevo_correo)
                        hoja["correo"] = nuevo_correo

            elif opcion == "2":
                hoja["formacion"] = []
                while True:
                    institucion = input("Institución educativa: ")
                    titulo = input("Título obtenido: ")
                    años = input("Años cursados (ej: 2015-2019): ")
                    hoja["formacion"].append({
                        "institucion": institucion,
                        "titulo": titulo,
                        "años": años
                    })
                    if input("¿Agregar otra formación? (s/n): ").lower() != 's':
                        break

            elif opcion == "3":
                hoja["experiencia"] = []
                while True:
                    empresa = input("Empresa: ")
                    cargo = input("Cargo desempeñado: ")
                    funciones = input("Funciones principales: ")
                    duracion = input("Duración (meses o años): ")
                    hoja["experiencia"].append({
                        "empresa": empresa,
                        "cargo": cargo,
                        "funciones": funciones,
                        "duracion": duracion
                    })
                    if input("¿Agregar otra experiencia? (s/n): ").lower() != 's':
                        break

            elif opcion == "4":
                hoja["referencias"] = []
                while True:
                    nombre_ref = input("Nombre de referencia: ")
                    relacion = input("Relación (laboral/personal): ")
                    telefono = input("Teléfono de referencia: ")
                    hoja["referencias"].append({
                        "nombre": nombre_ref,
                        "relacion": relacion,
                        "telefono": telefono
                    })
                    if input("¿Agregar otra referencia? (s/n): ").lower() != 's':
                        break

            elif opcion == "5":
                hoja["habilidades"] = []
                while True:
                    habilidad = input("Habilidad o certificación: ")
                    hoja["habilidades"].append(habilidad)
                    if input("¿Agregar otra habilidad? (s/n): ").lower() != 's':
                        break

            else:
                print("❌ Opción inválida.")

            print("✅ Hoja de vida actualizada.\n")
            return

    print(" No se encontró ninguna hoja de vida con ese criterio.\n")


def main():
    while True:
        print()

        print("1. Registrar hoja de vida")
        print("2. Consultar hoja de vida")
        print("3. Exportar hoja de vida")
        print("4. Generar reportes por experiencia")
        print("5. Actualizar hoja de vida")
        print("6. Salir\n")

        op = int(input("Seleccione una opcion: "))

        if op == 1:
            registro_hoja_vida()

        elif op == 2:
            consultar_hoja_vida()

        elif op == 3:
            exportar_json()

        elif op == 4:
            reporte_experiencia()

        elif op == 5:
            hojas_vida

        elif op == 6:
            print("Saliendo del sistema...")

        else:
            print("Opcion no valida....")


main()
