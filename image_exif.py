from PIL import Image

file_path = r'C:\Users\oberdfer\Documents\python_aulas\teste.jpg'
im = Image.open( file_path)

size = (4096, 4096)

im.thumbnail(size, Image.ANTIALIAS)
exif = im.info['exif']
im.save('teste_2.jpg', exif=exif)
