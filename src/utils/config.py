import subprocess

def ejecutar_comandos_desde_archivo(ruta_archivo):
    """
    Lee comandos desde un archivo y los ejecuta línea por línea.

    :param ruta_archivo: Ruta al archivo que contiene los comandos.
    :return: Lista de resultados, donde cada resultado es un diccionario con 'comando', 'salida', 'error' y 'codigo_salida'.
    """
    resultados = []

    try:
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                comando = linea.strip()  # Eliminar espacios y saltos de línea
                if not comando or comando.startswith("#"):  # Ignorar líneas vacías y comentarios
                    continue

                try:
                    # Ejecutar el comando
                    resultado = subprocess.run(
                        comando,
                        shell=True,
                        check=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )

                    # Agregar el resultado exitoso a la lista
                    resultados.append({
                        'comando': comando,
                        'salida': resultado.stdout.strip(),
                        'error': None,
                        'codigo_salida': resultado.returncode
                    })


                except subprocess.CalledProcessError as e:
                    # Capturar errores de comandos
                    resultados.append({
                        'comando': comando,
                        'salida': None,
                        'error': e.stderr.strip() if e.stderr else "Error desconocido",
                        'codigo_salida': e.returncode
                    })
                except Exception as e:
                    # Capturar otros errores inesperados
                    resultados.append({
                        'comando': comando,
                        'salida': None,
                        'error': str(e),
                        'codigo_salida': -1
                    })

    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

    return resultados

for out in ejecutar_comandos_desde_archivo("requirements.txt"):
    if out['error']:
        print(f"Error en el comando: {out['comando']}")
        print(f"Error: {out['error']}")
    else:
        print(f"Comando ejecutado correctamente: {out['comando']}")
