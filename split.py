import os
from PyPDF2 import PdfFileReader, PdfFileWriter

pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

for filename in pdfFiles:
    infile = PdfFileReader(open(filename, 'rb'))

    for i in xrange(infile.getNumPages()):
        p = infile.getPage(i)
        outfile = PdfFileWriter()
        outfile.addPage(p)
        outfilename = str(filename).replace('.pdf','')+'-page-'+str(i)+'.pdf'
        with open(outfilename, 'wb') as f:
            outfile.write(f)
