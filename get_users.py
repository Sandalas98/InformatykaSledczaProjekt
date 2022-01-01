import os

def get_system_info():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        print('Wykryto system Linux')
    elif platform == "win32":
        print('Wykryto system Windows')


# Funkcja zwracająca tablicę użtkotników (szuka folderu /home lub C:\Users)
# A następnie wypisuje jego zawartość.
def get_users(path):
    users = []
    sys = ''
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == 'Users': # if True
                #print(root+dir)
                sys = 'Windows'

                for usr_root, usr_dirs, usr_files in os.walk(root +'/'+ dir):
                    print(usr_root)
                    for usr_dir in usr_dirs:
                        print(usr_dir)
                        users.append(usr_dir)
            elif dir == 'home':
                #print(root+dir)
                sys = 'Windows'

                for usr_root, usr_dirs, usr_files in os.walk(root +'/'+ dir):
                    print(usr_root)
                    for usr_dir in usr_dirs:
                        print(usr_dir)
                        users.append(usr_dir)
            else:
                sys = 'not detected'


    print(users)
    return sys, users
