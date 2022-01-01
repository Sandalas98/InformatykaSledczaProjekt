import os
import shutil

def extract_files(path):

    if path == '':
        path = './mount'

    text_file_end = ['.txt', '.doc', '.pdf']
    image_file_ending = ['.png', '.jpg', '.bmp', '.gif']
    web_sites_ending = ['.html']
    music_files_ending = ['.wav', '.mp3']
    source_file_ending = ['.cpp', '.c', '.h', '.vba', '.exe', '.bin', '.EXE']

    # Usuwanie straego folderu wraz z plikami:
    try:
        shutil.rmtree('./analysis_dir')
        print('Usuwam folder analysis_dir')
    except OSError as e:
        print('Folder analysis_dir nie istnieje, nie ma co usuwać.')


    # Tworzenie folderów do których będą przypisywane różne pliki
    os.makedirs('./analysis_dir/docs')
    os.makedirs('./analysis_dir/images')
    os.makedirs('./analysis_dir/web_sites')
    os.makedirs('./analysis_dir/music')
    os.makedirs('./analysis_dir/source')
    os.makedirs('./analysis_dir/others')

    print('Utworzono foldery do ekstrakcji plików')

    for root, dirs, files in os.walk(path):
        for file in files:
            # Jeśli dany plik:

            # jest tekstem
            if file.endswith(text_file_end[0]) or file.endswith(text_file_end[1]) or file.endswith(text_file_end[2]):
                shutil.copyfile(src = f'{os.path.join(root, file)}', dst = f'./analysis_dir/docs/{file}')

            # jest zdjęciem:
            elif (file.endswith(image_file_ending[0]) or file.endswith(image_file_ending[1]) or 
            file.endswith(image_file_ending[2]) or file.endswith(image_file_ending[3])):
                shutil.copyfile(src = f'{os.path.join(root, file)}', dst = f'./analysis_dir/images/{file}')

            # jest stroną html
            elif file.endswith(web_sites_ending[0]):
                shutil.copyfile(src = f'{os.path.join(root, file)}', dst = f'./analysis_dir/web_sites/{file}')

            # jest muzyką
            elif file.endswith(music_files_ending[0]) or file.endswith(music_files_ending[1]):
                shutil.copyfile(src = f'{os.path.join(root, file)}', dst = f'./analysis_dir/music/{file}')


            # jest plikiem źródłowym lub wykonywalnym:
            elif (file.endswith(source_file_ending[0]) or file.endswith(source_file_ending[1]) or 
                file.endswith(source_file_ending[2]) or file.endswith(source_file_ending[3]) or 
                file.endswith(source_file_ending[4]) or file.endswith(source_file_ending[5]) or 
                file.endswith(source_file_ending[6])):
                shutil.copyfile(src = f'{os.path.join(root, file)}', dst = f'./analysis_dir/source/{file}')

            # inne pliki:
            else:
                shutil.copyfile(src = f'{os.path.join(root, file)}', dst = f'./analysis_dir/others/{file}')

    print('Zakończono kopiowanie plików')