import platform
import os

def get_system_info():
    return platform.platform(), platform.processor()


# Funkcja zwracająca tablicę użtkotników (szuka folderu /home lub C:\Users)
# A następnie wypisuje jego zawartość.
def get_users(path):
    users = []
    sys = 'No system detected'
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == 'Users': # if True
                #print(root+dir)
                sys = 'Windows detected'

                for usr_root, usr_dirs, usr_files in os.walk(root +'/'+ dir):
                    print(usr_root)
                    for usr_dir in usr_dirs:
                        print(usr_dir)
                        users.append(usr_dir)
                break
            elif dir == 'home':
                #print(root+dir)
                if os.path.exists('{}/root'.format(path)):
                    sys = 'Linux detected'

                for usr_root, usr_dirs, usr_files in os.walk(root +'/'+ dir):
                    print(usr_root)
                    for usr_dir in usr_dirs:
                        print(usr_dir)
                        users.append(usr_dir)
                break


    print(users)
    return sys, users
