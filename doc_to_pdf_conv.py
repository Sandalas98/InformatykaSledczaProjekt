from docx2pdf import convert
import os, pandas as pd
import comtypes.client
import sys, os

def conv_2_pdf(path):
    pdf_name = 'from_doc_'
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith('.docx') or file.endswith('.DOCX')):
                file_name = file[:-5]
                print(path+pdf_name+file_name+'.pdf')
                convert(path+file, path+'from_doc'+file_name+'.pdf')