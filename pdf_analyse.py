import PyPDF2, os, pandas as pd
from docx2pdf import convert

def get_info(path):
    df = pd.DataFrame(columns=['Autor', 'Tytul', 'Lokalizacja'])



    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf'):
                with open(path+file, 'rb') as f:
                    pdf = PyPDF2.PdfFileReader(f)
                    info = pdf.getDocumentInfo()
                    number_of_pages = pdf.getNumPages()
                
                author = info.author
                #creator = info.creator
                #producer = info.producer
                #subject = info.subject
                title = info.title
                df = df.append({'Autor':author, 'Tytul':title, 'Lokalizacja':{path+file}}, ignore_index=True)
    df.to_csv('analiza_pdf.csv')

