#Esse script é chamado pelo programa 'search_and_resize_jpg.py'

from PIL import Image


def resize(name,factor):
    print(name)
    imagem = Image.open(name)
    largura,altura = imagem.size

    #copia dados exif
    exif = imagem.info['exif']
    
    print('Imagem:',name)
    print('tamanho original:',largura,'x',altura)

    #print(exif)

    # diminui a imagem 
    largura = largura/factor
    altura = altura/factor
    metade_imagem = imagem.resize((int(largura),int(altura)), Image.ANTIALIAS)
    print('novo tamanho:    ',largura,'x',altura)

    #cria nome (adiciona _resized)
    novo_nome = name[:-4] + '_resized' + name[-4:]
    print('Copia criada:',novo_nome)
    print(' ')

    #salva a copia com exif
    metade_imagem.save(name, exif=exif, quality=95)
