import pandas as pd
import violencia_obstetrica.utils.paths as path

""" 
Function to read excel 
files as dataframes
"""
def load_file(file="filename", sheet="sheet_name"):
    df = pd.read_excel(file, index_col=None, sheet_name=sheet)
    return df

"""
Function to convert 
columns into a list
"""
def load_columns(df):
    cols = df.columns
    return cols

# Inputs
data_cuba_pre = path.data_processed_dir("data_cuba_preprocessed.xlsx")
data_cuba = path.data_processed_dir("data_cuba_processed.xlsx")
data_directorio =  path.data_processed_dir("directorio_hospitales.xlsx")
data_testimonios =  path.data_processed_dir("testimonios_cuba.xlsx")
icon_image = path.assets_dir("icon.png")

# Outputs
data_processed = path.data_processed_dir()
tables =  path.outputs_tables_dir()
figures = path.outputs_figures_dir()
jsons = path.outputs_jsons_dir()