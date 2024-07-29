import pandas as pd
from dbfread import DBF, FieldParser, InvalidValue

class CustomFieldParser(FieldParser):
    def parseM(self, field, data):
        # Ignorar el campo memo
        return ""

def convert_dbf_to_excel(dbf_file_path, excel_file_path):
    try:
        # Leer el archivo DBF
        table = DBF(dbf_file_path, parserclass=CustomFieldParser, ignore_missing_memofile=True)
        
        # Convertir a DataFrame de pandas, asegurando que todos los datos sean cadenas
        df = pd.DataFrame(iter(table))
        df = df.astype(str)  # Convertir todos los datos a cadenas
        
        # Guardar el DataFrame en un archivo Excel
        df.to_excel(excel_file_path, index=False)
        print(f'Archivo Excel guardado en: {excel_file_path}')
    except Exception as e:
        print(f'Error al leer el archivo DBF: {e}')

if __name__ == "__main__":
    dbf_file_path = 'transpor.dbf'
    excel_file_path = 'transpor.xlsx'
    convert_dbf_to_excel(dbf_file_path, excel_file_path)
