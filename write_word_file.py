from mailmerge import MailMerge
from datetime import datetime
import json
doc = '1.docx'
document = MailMerge(doc)
x = [{'question':'bharath','answer':'kumar',"comment":'jatoth'},{'question':'bharath1','answer':'kumar1',"comment":'jatoth1'}]
x = json.dumps(x)
y = (json.loads(x))
document.merge_rows('question',y)
document.write('mailmerge.docx')
