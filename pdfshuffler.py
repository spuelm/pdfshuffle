from PyPDF4 import PdfFileReader, PdfFileWriter

def shuffle_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    # Rotate page 90 degrees to the right
    docPages=pdf_reader.numPages
    for pagenum in range(docPages//2):
        page= pdf_reader.getPage(pagenum)
        pdf_writer.addPage(page)
        page= pdf_reader.getPage(docPages-pagenum-1)
        pdf_writer.addPage(page)
    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)

shuffle_pages("doc20240105132221.pdf")