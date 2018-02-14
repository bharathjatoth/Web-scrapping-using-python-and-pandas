import pandas as pd
from pathlib import Path
pd.set_option('display.max_colwidth', -1)
pathlist = Path(pathlocation of list of files).glob('**/*.xlsx')
for path in pathlist:
    x = str(path)
    df = pd.read_excel(x,sheetname=None) #sheetname None So that I need to read all the workbooks in it
    print(path)
    print(df)
