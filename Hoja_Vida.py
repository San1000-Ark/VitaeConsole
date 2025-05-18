import json
from datetime import datetime

hojas_vida = []

def registro_hoja_vida():
    nombre = input("Ingresa el nombre completo: ").strip()
    while len(nombre.split()) < 2:
        print("Por favor, ingresa el nombre completo (mínimo dos palabras).")
        nombre = input("Ingresa el nombre completo: ").strip()
    
    while True:
        documento_id = input("Ingresa el documento de identidad (10 dígitos): ").strip()
        if documento_id.isdigit() and len(documento_id) == 10:
            break
        else:
            print("El documento de identidad debe contener exactamente 10 números.")
    
    direccion = input("Ingresa la dirección: ").strip()
    
    while True:
        telefono = input("Ingresa tu teléfono (10 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 10:
            break
        else:
            print("El teléfono debe contener exactamente 10 números.")
    
    correo = input("Ingresa el correo electrónico (debe contener '@' y terminar en .com o .co): ").strip()
    while ('@' not in correo) or (not (correo.endswith(".com") or correo.endswith(".co"))):
        print("El correo debe contener '@' y terminar en '.com' o '.co'.")
        correo = input("Ingresa el correo electrónico: ").strip()

    
    while True:
        fecha_nacimiento = input("Ingresa la fecha de nacimiento (DD/MM/AAAA): ").strip()
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha incorrecto o fecha inválida. Usa DD/MM/AAAA.")
    
    formacion = []
    while True:
        print("\n====== FORMACIÓN ACADÉMICA ======")
        institucion = input("Institución educativa: ").strip()
        titulo = input("Título obtenido: ").strip()
        experiencia_anos = input("Años cursados: ").strip()
        formacion.append({
            'institucion': institucion,
            'titulo': titulo,
            'experiencia': experiencia_anos
        })
        if input("¿Deseas ingresar otra formación? (s/n): ").strip().lower() != 's':
            break
    
    experiencia = []
    while True:
        print("\n====== EXPERIENCIA LABORAL ======")
        empresa = input("Nombre de la empresa (deja vacío si no tienes experiencia): ").strip()
        if empresa == "":
            break
        cargo = input("Cargo desempeñado: ").strip()
        funciones = input("Funciones realizadas: ").strip()
        while True:
            duracion = input("Duración de la experiencia en meses: ").strip()
            if duracion.isdigit() and int(duracion) > 0:
                break
            else:
                print("Por favor, ingresa un número válido de meses (entero positivo).")
        experiencia.append({
            'empresa': empresa,
            'cargo': cargo,
            'funciones': funciones,
            'duracion': duracion
        })
        if input("¿Deseas ingresar otra experiencia? (s/n): ").strip().lower() != 's':
            break
    
    referencia_personales = []
    while True:
        print("\n====== REFERENCIAS PERSONALES/LABORALES ======")
        nombre_ref = input("Nombre de la referencia: ").strip()
        parentesco = input("Relación (Laboral/Personal): ").strip()
        while True:
            telefono_ref = input("Teléfono de la referencia (10 dígitos): ").strip()
            if telefono_ref.isdigit() and len(telefono_ref) == 10:
                break
            else:
                print("El teléfono de la referencia debe contener exactamente 10 números.")
        referencia_personales.append({
            'nombre_ref': nombre_ref,
            'parentesco': parentesco,
            'telefono_ref': telefono_ref
        })
        if input("¿Deseas ingresar otra referencia? (s/n): ").strip().lower() != 's':
            break
    
    habilidades = []
    while True:
        print("\n====== HABILIDADES ======")
        habilidad = input("Describe una habilidad: ").strip()
        habilidades.append(habilidad)
        if input("¿Deseas ingresar otra habilidad? (s/n): ").strip().lower() != 's':
            break
    
    hoja_vida = {
        'nombre': nombre,
        'documento_id': documento_id,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'fecha_nacimiento': fecha_nacimiento,
        'formacion': formacion,
        'experiencia': experiencia,
        'referencia_personales': referencia_personales,
        'habilidades': habilidades
    }
    
    hojas_vida.append(hoja_vida)
    print("\nHoja de vida registrada exitosamente.\n")

def consultar_hoja_vida():
    busqueda = input("Buscar por (nombre/documento_id/correo): ").strip().lower()
    valor = input(f"Ingrese el {busqueda}: ").strip().lower()
    
    for hoja in hojas_vida:
        if busqueda == "nombre" and valor == hoja['nombre'].lower():
            mostrar_hoja(hoja)
            return
        elif busqueda == "documento_id" and valor == hoja['documento_id'].lower():
            mostrar_hoja(hoja)
            return
        elif busqueda == "correo" and valor == hoja['correo'].lower():
            mostrar_hoja(hoja)
            return
    print("\nNo se encontró la hoja de vida con ese dato.\n")

def mostrar_hoja(hoja):
    print("\n--- Hoja de vida encontrada ---")
    print(f"Nombre completo: {hoja['nombre']}")
    print(f"Documento de identidad: {hoja['documento_id']}")
    print(f"Dirección: {hoja['direccion']}")
    print(f"Teléfono: {hoja['telefono']}")
    print(f"Correo: {hoja['correo']}")
    print(f"Fecha de nacimiento: {hoja['fecha_nacimiento']}")
    
    if hoja['formacion']:
        print("\nFormación académica:")
        for f in hoja['formacion']:
            print(f" - {f['titulo']} en {f['institucion']} ({f['experiencia']} años)")
    else:
        print("\nNo tiene formación académica registrada.")
    
    if hoja['experiencia']:
        print("\nExperiencia laboral:")
        for e in hoja['experiencia']:
            print(f" - {e['cargo']} en {e['empresa']} ({e['duracion']} meses)")
            print(f"   Funciones: {e['funciones']}")
    else:
        print("\nNo tiene experiencia laboral registrada.")
    
    if hoja['referencia_personales']:
        print("\nReferencias personales:")
        for r in hoja['referencia_personales']:
            print(f" - {r['nombre_ref']} ({r['parentesco']}), Teléfono: {r['telefono_ref']}")
    else:
        print("\nNo tiene referencias personales registradas.")
    
    if hoja['habilidades']:
        print("\nHabilidades:")
        for h in hoja['habilidades']:
            print(f" - {h}")
    else:
        print("\nNo tiene habilidades registradas.")
    
    print("\n-----------------------------\n")

def exportar_json():
    with open("hojas_exportadas.json", "w", encoding="utf-8") as archivo:
        json.dump(hojas_vida, archivo, indent=4, ensure_ascii=False)
    print("Las hojas de vida fueron exportadas a 'hojas_exportadas.json'\n")

def main():
    while True:
        print("1. Registrar hoja de vida")
        print("2. Consultar hoja de vida")
        print("3. Exportar hojas de vida")
        print("4. Salir\n")

        op = input("Seleccione una opción: ").strip()
        
        if op == "1":
            registro_hoja_vida()
        elif op == "2":
            consultar_hoja_vida()
        elif op == "3":
            exportar_json()
        elif op == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

if __name__ == "__main__":
    main()
