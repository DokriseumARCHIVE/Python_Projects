import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(result_name):
    pdf_writer = PdfFileWriter()
    root = tkinter.Tk()
    files = filedialog.askopenfilenames(parent=root,title='PDF auswählen')

    for file in root.tk.splitlist(files):
        pdf_reader = PdfFileReader(file)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

    print('PDF zusammengefügt')
    with open(result_name, 'wb') as out:
        pdf_writer.write(out)
        print('PDF erfolgreich erstellt')