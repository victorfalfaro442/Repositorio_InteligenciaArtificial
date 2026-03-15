# Definición de la jerarquía de excepciones
class StudentsDataException(Exception):
    """Clase base para errores de datos de estudiantes."""
    pass

class BadLine(StudentsDataException):
    """Lanzada cuando una línea no tiene el formato correcto."""
    def __init__(self, linea):
        super().__init__(f"Error en línea: '{linea.strip()}'")

class FileEmpty(StudentsDataException):
    """Lanzada cuando el archivo existe pero no tiene contenido."""
    def __init__(self):
        super().__init__("Error: El archivo está vacío.")

def procesar_notas_jekyll():
    nombre_archivo = input("Introduce el nombre del archivo del profesor: ")
    notas_estudiantes = {}

    try:
        # 1. Intentar abrir el archivo
        with open(nombre_archivo, "rt", encoding="utf-8") as f:
            lineas = f.readlines()
            
            # 2. Comprobar si el archivo está vacío
            if not lineas:
                raise FileEmpty()

            # 3. Procesar cada línea
            for num_linea, linea in enumerate(lineas, 1):
                partes = linea.split()
                
                # Una línea válida debe tener exactamente: Nombre, Apellido, Puntos
                if len(partes) != 3:
                    raise BadLine(linea)
                
                nombre, apellido, puntos_str = partes
                llave_estudiante = f"{nombre} {apellido}"
                
                try:
                    puntos = float(puntos_str)
                except ValueError:
                    # Si los puntos no son un número, también es una línea incorrecta
                    raise BadLine(linea)
                
                # 4. Acumular puntos en el diccionario
                notas_estudiantes[llave_estudiante] = notas_estudiantes.get(llave_estudiante, 0.0) + puntos

        # 5. Imprimir informe ordenado alfabéticamente
        print("\n--- Informe del Profesor Jekyll ---")
        for estudiante in sorted(notas_estudiantes.keys()):
            print(f"{estudiante:<20} {notas_estudiantes[estudiante]}")

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except StudentsDataException as e:
        print(e)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    procesar_notas_jekyll()
