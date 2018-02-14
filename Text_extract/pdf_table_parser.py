# It only extracts the tables from the pdf file The text extraction is given in pdf_parser.py file please find it there
import pdfquery
pdf = pdfquery.PDFQuery(pathto_pdf_file)
pdf.load()
pdf.tree.write(pathto_pdf_file, pretty_print=True)
name_element = pdf.pq('LTPage[pageid=\'1\'] LTTextLineHorizontal:contains("Col1")')[0]
print(name_element.text)
x = float(name_element.get('x0'))
y = float(name_element.get('y0'))
# Here we see the length of the tables and extracting those. We start with the first cell and increase the distance and get the text from it.
cells = pdf.extract( [
         ('with_parent','LTPage[pageid=\'1\']'),
         ('cells', 'LTTextLineHorizontal:in_bbox("%s,%s,%s,%s")' % (x, y-50, x+50, y))
    ])
print(cell.text.strip()) for cell in cells['cells']
