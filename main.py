import file_extract, pdf_analyse, doc_to_pdf_conv
import os


file_extract.extract_files('./mount')
doc_to_pdf_conv.conv_2_pdf('./analysis_dir/docs/')

# Tu podać ścieżki do dysku:
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')
#file_extract.extract_files('/media/sandalas/FCBC-D18E/')
pdf_analyse.get_info('./analysis_dir/docs/')
