import os
folder = input('Selecione a pasta onde será alterados os arquivos: ')
folderLink = r'{}\\'.format(folder)
name = input('Digite o novo nome do arquivo: ')
tipo = input('Digite o tipo do arquivo: ')
contador = 0
numaux = ''

for file_name in os.listdir(folderLink):
    contador += 1
    if(contador < 10):
        numaux = 0
    else:
        numaux = ''
    old_name = folderLink + file_name
    new_name = folderLink + f'{name}-{numaux}{contador}.{tipo}'
    os.rename(old_name, new_name)

print(os.listdir(folderLink))