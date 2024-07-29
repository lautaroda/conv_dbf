# Convertidor de DBF a Excel

Este proyecto proporciona un script en Python para convertir archivos DBF a archivos Excel. Es útil para importar datos en Odoo 15 u otras aplicaciones que aceptan archivos Excel.

## Requisitos

- Python 3.x
- `pandas` biblioteca
- `simpledbf` biblioteca

## Instalación

1. Clona este repositorio o descarga los archivos.

2. Instala las bibliotecas necesarias usando `pip`:

    ```bash
    pip install pandas simpledbf
    ```

## Uso

1. Asegúrate de que tus archivos DBF están en la ruta especificada en el script.

2. Modifica las rutas de los archivos en el script `convert_dbf_to_excel.py` según sea necesario:

    ```python
    dbf_file_path = 'ruta/a/tu/archivo/ .dbf'
    excel_file_path = 'ruta/a/tu/archivo/ .xlsx'
    ```

3. Ejecuta el script desde la línea de comandos:

    ```bash
    python convert_dbf_to_excel.py
    ```

