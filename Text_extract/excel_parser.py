import pandas as pd
from pathlib import Path
pd.set_option('display.max_colwidth', -1) #pandas to display total text insted of displaying only part of the text
pathlist = Path(pathlocation of list of files).glob('**/*.xlsx')
list1 = []
#we iterate on each excel file in the directory
for path in pathlist:
    x = str(path)
    df = pd.read_excel(x,sheetname=None) #sheetname None So that I need to read all the workbooks in it
    df = pd.read_excel(x,sheetname='xxxxxx',skiprows=1) #only read from a particular sheet in each Excel sheet and skiprows you can adjust number of rows to skip
    list1 = (df['System /Functional Requirement Specification (Requirement Title)']) #specifing the column to extract
    print(path)
    print(df)
    print(list1)
