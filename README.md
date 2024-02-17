# Package has been deleted. If you want to use then you can download the code and use it.

This package enables the generation of a DataFrame with Change Data Capture (CDC) flags ('I' for Insert, 'U' for Update, and 'D' for Delete) by comparing historical and source data files

## Installation

Use the package manager `pip` to install pycdc.

```bash
pip install pycdc
```

## Usage
This package enables the generation of a DataFrame with Change Data Capture (CDC) flags ('I' for Insert, 'U' for Update, and 'D' for Delete) by comparing historical and source data files.It achieves this by comparing the structures of historical and source data files to ensure they share the same column structure.
```python
import pandas as pd
from pycdc import CDCGenerator

def read_file(filePath):
    try:
        df=pd.read_csv(filePath)
        return df
    except FileNotFoundError as e:
        raise e

sourceDataFrame=read_file('data/sales_data.csv') # your current source file
previousDataFrame=read_file('history/sales_data.csv') # your history file

cdcDataframe=CDCGenerator(
    keyColumn=['ProductID','Date'],
    sourceDataframe=sourceDataFrame,
    previousDataframe=previousDataFrame).perform_cdc()
print(cdcDataframe)
```
```
Output:-

| Date       | ProductID | Quantity | CDC_Flag |
|------------|-----------|----------|----------|
| 2023-02-03 | 1013      | 20       | I        |
| 2023-02-03 | 1014      | 20       | I        |
| 2023-01-02 | 1002      | 1500     | U        |
| 2023-02-03 | 1012      | 20       | D        |
```



## Contributing
Your contributions to this project are encouraged and valued! You have the autonomy to make modifications directly and merge them without the need for a formal review process. You have the freedom to utilize the code in any manner you deem fit. 
