import file_extract, pdf_analyse, doc_to_pdf_conv, get_users, face_detection
import os


# Rozpoznaje system i użytkowników
get_users.get_users('./mount')

# Ekstrakcja plików :
# Tu podać ścieżki do dysku (lub folderu z wypakowanym obrazem dyskowym):
file_extract.extract_files('./mount') #ścieżka do katalogu dysku

#Narzędzie do konwersji .docx -> .pdf, nie działa, poprawić
doc_to_pdf_conv.conv_2_pdf('./analysis_dir/docs/')

# Analiza plików .pdf
pdf_analyse.get_info('./analysis_dir/docs/')

# Ekstrakcja twarzy:
face_detection.face_detection('./analysis_dir/images')
