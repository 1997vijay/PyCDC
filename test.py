import pandas as pd
from pycdc import CDCGenerator

def read_file(filePath):
    try:
        df=pd.read_csv(filePath)
        return df
    except FileNotFoundError as e:
        raise e

sourceDataFrame=read_file('data/sales_data.csv')
previousDataFrame=read_file('history/sales_data.csv')

cdcDataframe=CDCGenerator(keyColumn=['ProductID','Date'],sourceDataframe=sourceDataFrame,previousDataframe=previousDataFrame).perform_cdc()
print(cdcDataframe)