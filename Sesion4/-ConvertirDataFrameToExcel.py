import pandas as pd

# Datos proporcionados
data = {
    'ID': list(range(1, 21)),
    'Edad': [25, 30, 22, 40, 35, 28, 50, 45, 38, 27, 
             26, 32, 36, 29, 34, 33, 42, 48, 44, 31],
    'Salario': [2000, 2200, 2100, 3000, 2800, 2500, 3500, 3300, 2900, 2400,
                2300, 2600, 2700, 2550, 2750, 2650, 3100, 3400, 3200, 2350]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Especificar el nombre del archivo Excel
excel_file = 'datos_empleados.xlsx'

# Guardar el DataFrame en el archivo Excel
df.to_excel(excel_file, index=False)

print(f"Archivo Excel '{excel_file}' creado correctamente.")
