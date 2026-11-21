
import os
import pandas as pd

def procesar_datos():
    # Rutas configurables mediante variables de entorno
    ruta_entrada = os.getenv("INPUT_FILE", "/app/data/entrada.csv")
    ruta_salida = os.getenv("OUTPUT_FILE", "/app/output/resultado.csv")

    print("Iniciando procesamiento de datos...")

    # Leer archivo CSV
    df = pd.read_csv(ruta_entrada)

    print(f"Registros originales: {len(df)}")

    # Limpiar espacios en los nombres de columnas
    df.columns = df.columns.str.strip()

    # Eliminar registros duplicados
    df = df.drop_duplicates()

    # Eliminar filas con valores vacíos
    df = df.dropna()

    # Calcular estadísticas
    promedio_edad = df["edad"].mean()
    promedio_salario = df["salario"].mean()

    # Crear carpeta de salida si no existe
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    # Guardar datos procesados
    df.to_csv(ruta_salida, index=False)

    print("Procesamiento completado correctamente.")
    print(f"Registros finales: {len(df)}")
    print(f"Edad promedio: {promedio_edad:.2f}")
    print(f"Salario promedio: {promedio_salario:.2f}")
    print(f"Archivo generado: {ruta_salida}")


if __name__ == "__main__":
    procesar_datos()
