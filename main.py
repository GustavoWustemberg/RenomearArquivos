import os
folder = input('Selecione a pasta onde será alterados os arquivos: ')
folderLink = r'{}\\'.format(folder)
name = input('Digite o novo nome do arquivo: ')
tipo = input('Digite o tipo do arquivo: ')
contador = 0
numaux = ''
numinicial = int(input('Digite o valor inicial a ser acrescentado ao nome: '))

for file_name in os.listdir(folderLink):
    if(numinicial == 1):
        contador += 1
    else:
        contador = numinicial
        numinicial += 1
    if(contador < 10):
        numaux = 0
    else:
        numaux = ''
    old_name = folderLink + file_name
    new_name = folderLink + f'{name}-{numaux}{contador}.{tipo}'
    os.rename(old_name, new_name)

print(os.listdir(folderLink))