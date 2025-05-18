import json  # para guardar y cargar hojas de vida
# tabulate para agregar un formato a todos los datos de entrada ingresados por el usuario
from tabulate import tabulate

# Datos personales
hojas_vida = []
correos = set()

def es_numero_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def registro_hoja_vida():
    nombre = input("Ingresa el nombre: ")

    documento_id = input("Ingresa el documento de identidad (10 dígitos): ")
    while not es_numero_10_digitos(documento_id):
        print("❌ El documento debe tener exactamente 10 dígitos numéricos.")
        documento_id = input("Ingresa nuevamente el documento de identidad: ")

    direccion = input("Ingresa la direccion: ")

    telefono = input("Ingresa tu telefono (10 dígitos): ")
    while not es_numero_10_digitos(telefono):
        print("❌ El teléfono debe tener exactamente 10 dígitos numéricos.")
        telefono = input("Ingresa nuevamente tu telefono: ")

    correo = input("Ingresa el correo electronico: ")
    while not correo.endswith("@gmail.com"):
        print("❌ El correo debe terminar en '@gmail.com'.")
        correo = input("Ingresa de nuevo el correo electrónico: ")

    if correo in correos:
        print("❌ Correo ya existente; ingresa uno nuevo...")
        return
    else:
        correos.add(correo)

    fecha_nacimiento = input("Ingresa la fecha de nacimiento (DD/MM/AAAA): ")

    validacion = (fecha_nacimiento, documento_id)

    formacion = []
    while True:
        print("\n====== FORMACION ACADEMICA ======\n")
        institucion = input("Ingresa la institucion educativa: ")
        titulo = input("Ingresa el titulo obtenido: ")
        experiencia = input("Ingresa años cursados: ")
        formacion.append({'institucion': institucion, 'titulo': titulo, 'experiencia': experiencia})
        if input("Deseas ingresar otra formacion ? (s/n): ").lower() != "s":
            break

    experiencia = []
    while True:
        empresa = input("Nombre de la empresa en la que laboraste: ")
        cargo = input("Nombre del cargo desempeñado: ")
        funciones = input("Ingresa las funciones realizadas: ")
        duracion = input("Ingresa el tiempo laborado: ")
        experiencia.append({'empresa': empresa, 'cargo': cargo, 'funciones': funciones, 'duracion': duracion})
        if input("Deseas ingresar otra experiencia ? (s/n): ").lower() != "s":
            break

    referencia_personales = []
    while True:
        print("\n====== REFERENCIAS PERSONAL/LAORAL ======\n")
        nombre_ref = input("Ingresa el nombre de la referencia: ")
        parentesco = input("Relacion (Laboral / Personal): ")
        telefono_ref = input("Telefono de la referencia (10 dígitos): ")
        while not es_numero_10_digitos(telefono_ref):
            print("❌ El teléfono de la referencia debe tener exactamente 10 dígitos numéricos.")
            telefono_ref = input("Ingresa nuevamente el teléfono de la referencia: ")

        referencia_personales.append(
            {'nombre_ref': nombre_ref, 'parentesco': parentesco, 'telefono_ref': telefono_ref})

        if input("Deseas ingresar otra referencia ? (s/n): ").lower() != "s":
            break

    habilidades = []
    while True:
        print("\n====== FORMACION ACADEMICA ======\n")
        habilidad = input("Cuales son tus habilidades? ")
        habilidades.append(habilidad)
        if input("Deseas ingresar otra habilidad ? (s/n): ").lower() != "s":
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
        'habilidades': list(habilidades)
    }

    hojas_vida.append(hoja_vida)
    print("✅ La hoja de vida se añadió exitosamente")