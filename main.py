import pandas as pd
from simpledbf import Dbf5

def convert_dbf_to_excel(dbf_file_path, excel_file_path):
    # Cargar el archivo DBF
    dbf = Dbf5(dbf_file_path)
    df = dbf.to_dataframe()
    
    # Guardar los datos en un archivo Excel
    df.to_excel(excel_file_path, index=False)
    print(f'Archivo Excel guardado en: {excel_file_path}')

if __name__ == "__main__":
    # Rutas de los archivos
    dbf_file_path = './transpor.dbf'
    excel_file_path = './transpor.xlsx'
    
    # Convertir DBF a Excel
    convert_dbf_to_excel(dbf_file_path, excel_file_path)
