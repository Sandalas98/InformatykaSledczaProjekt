import file_extract, pdf_analyse, doc_to_pdf_conv
import os


# Tu podać ścieżki do dysku (lub folderu z wypakowanym obrazem dyskowym):
file_extract.extract_files('./mount')
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')



# Narzędzie do konwersji .doc -> .docx
#doc_to_pdf_conv.conv_2_pdf('./analysis_dir/docs/')



# Analiza plików .pdf
pdf_analyse.get_info('./analysis_dir/docs/')
