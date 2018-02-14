import pandas as pd
from pathlib import Path
pd.set_option('display.max_colwidth', -1)
pathlist = Path(r'C:\Users\jatoth.kumar\Desktop\Iape').glob('**/*.xlsx')
for path in pathlist:
    x = str(path)
    df = pd.read_excel(x,sheetname=None)
    print(path)
    print(df)
