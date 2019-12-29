import os
dir = os.getcwd()


def rem_site_adrs():
    """
    removes website address from begining of the file.
    Ex: "www.3MovieRulz.com - Dhrusti (2019).mkv" ->  "Dhrusti (2019).mkv"
    """
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.name.startswith('www.') and entry.is_file():
                name = ""
                ss = entry.name.split('-')
                ss.pop(0)
                name = '-'.join(ss)
                name.strip()
                os.rename(dir+"\\"+entry.name, dir+"\\"+name)
                print(entry.name)


def rem_zip_files():
    """
    removes all zip files in the given directory.
    """
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.name.endswith('.zip') and entry.is_file():
                os.remove(dir+"\\"+entry.name)
                print(entry.name)


print('This gonna modify files in this "'+dir+'" directory.')
print('press "cd" to change directory or anything to modify files in "'+dir+'" directory.')
if input() == 'cd':
    print('Enter dir full path Ex: "E:\The Witcher US"(excluding double quotes ;)')
    tdir = input()
    if(os.path.isdir(tdir)):
        dir = tdir
        rem_site_adrs()
        rem_zip_files()
    else:
        print('"'+tdir+'" is not a Directory :|')

else:
    rem_site_adrs()
    rem_zip_files()


input()
