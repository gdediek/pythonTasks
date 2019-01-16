# Procura por arquivos .jpg em uma pasta e reduz cada
# cada imagem pela metada de seu tamanho.

import os
import subprocess
import image_resize
from PIL import Image

def search_and_process(folder):
    #list files from a folder
    file_list = os.listdir(folder)
    print(folder)
    #print(file_list)

    number_of_files_founded = 0
    #process each file
    for file_name in file_list:
        # is jpg file?
        if file_name[-3:] == 'jpg':
            number_of_files_founded += 1
            image_resize.resize(folder+'\\'+file_name,2)
            #delete original
            #os.remove(file_name) testar isso 170815

    print('Processado',number_of_files_founded,'arquivos.')

#RUN FORREST, RUN!
#imagem = Image.open(r"C:\Users\oberdfer\Documents\python_aulas\IMG_20170630_110037.jpg")
#imagem.close()
#execute with current folder
search_and_process(r"C:\Users\oberdfer\Documents\python_aulas")

